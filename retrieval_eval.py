"""SupportBrain retrieval evaluation, shared by Act 1 and Act 2 (retrieval only, no generation).

Act 1 settings are the defaults. Act 2 changes are switched on with flags, so the
baseline and the redesign run through identical scoring code.

Locked decisions (see run-decisions.md):
  - Fixed-size chunking: 256 tokens, 20 overlap, no awareness of headings
  - Frontmatter stripped, so no metadata reaches the index
  - BGE embeddings (BAAI/bge-small-en-v1.5), no query instruction
  - Fresh in-memory ChromaDB collection per run
  - Hit = a retrieved chunk overlaps the text of any labeled section
  - Reports hit-rate@3, hit-rate@5 and MRR@5, primary+alternates and primary-only
  - Coverage-gap questions are excluded from the scores and reported separately

Usage:
  Act 1:  python retrieval_eval.py --kb ./kb --labels ./labels.csv --out ./results --run-name act1
  Act 2:  python retrieval_eval.py --kb ./kb --labels ./labels.csv --out ./results --run-name act2 --chunking headings

The held-out questions must never be passed to this script.
"""

import argparse
import csv
import hashlib
import json
import platform
import re
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import chromadb
from llama_index.core import Document, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

CHUNK_SIZE = 256
CHUNK_OVERLAP = 20
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
KS = (3, 5)
TOP_K = max(KS)

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.S)
HEADING = re.compile(r"^## .*$", re.M)


def strip_frontmatter(text: str) -> str:
    match = FRONTMATTER.match(text)
    return text[match.end():] if match else text


def section_spans(slug: str, body: str):
    """Character span of every section, keyed by the section-index ID (slug#n)."""
    heads = list(HEADING.finditer(body))
    spans = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        spans.append((f"{slug}#{i + 1}", head.start(), end))
    return spans


def sections_for_chunk(start: int, end: int, spans):
    return [sid for sid, a, b in spans if start < b and a < end]


def pkg_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not installed"


def load_corpus(kb_dir: Path):
    docs, spans, hashes, titles = [], {}, {}, {}
    for path in sorted(kb_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        if not FRONTMATTER.match(raw):
            continue  # only KB articles have frontmatter; skips notes and logs
        slug = path.stem
        body = strip_frontmatter(raw)
        hashes[slug] = hashlib.sha256(raw.encode()).hexdigest()[:12]
        spans[slug] = section_spans(slug, body)
        m = re.search(r'^title: "(.*)"$', raw, re.M)
        titles[slug] = m.group(1) if m else slug
        docs.append(Document(text=body, id_=slug, metadata={}))
    if not docs:
        raise SystemExit(f"No KB articles with frontmatter found in {kb_dir}")
    return docs, spans, hashes, titles


def load_labels(labels_path: Path):
    if "held" in labels_path.name.lower():
        raise SystemExit("Refusing to run: this looks like the held-out set.")
    with labels_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["gold_all"] = [s for s in [row["primary"]] + row["alternates"].split("|") if s]
        row["gold_primary"] = [row["primary"]] if row["primary"] else []
        row["is_gap"] = row["gap"].strip().lower() == "yes"
    return rows


def gold_share(chunk, gold, spans):
    """Fraction of a chunk's text that belongs to the gold sections (0 to 1)."""
    if not chunk["range"]:
        return 0.0
    a, b = chunk["range"]
    covered = sum(max(0, min(b, e) - max(a, s)) for sid, s, e in spans[chunk["article"]] if sid in gold)
    return round(covered / max(1, b - a), 3)


def first_hit_rank(retrieved, gold):
    for rank, chunk in enumerate(retrieved, start=1):
        if set(chunk["sections"]) & set(gold):
            return rank
    return None


def summarize(rows, key):
    n = len(rows)
    if n == 0:
        return {}
    ranks = [r[key] for r in rows]
    out = {f"hit_rate@{k}": round(sum(1 for x in ranks if x and x <= k) / n, 3) for k in KS}
    out[f"mrr@{TOP_K}"] = round(sum(1 / x for x in ranks if x) / n, 3)
    if key == "rank_all":
        shares = [r["first_hit_gold_share"] for r in rows if r["first_hit_gold_share"] is not None]
        out["mean_gold_share_of_first_hit"] = round(sum(shares) / len(shares), 3) if shares else None
    out["n"] = n
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kb", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("results"))
    parser.add_argument("--run-name", default="act1")
    parser.add_argument("--chunking", choices=["fixed", "headings"], default="fixed",
                        help="fixed = Act 1 (256-token length split); headings = one chunk per ## section")
    parser.add_argument("--title-prefix", action="store_true",
                        help="Prepend each article's title to its chunks before embedding")
    parser.add_argument("--mock-embeddings", action="store_true",
                        help="Pipeline test only: placeholder embeddings, scores are meaningless")
    args = parser.parse_args()

    docs, spans, hashes, titles = load_corpus(args.kb)
    labels = load_labels(args.labels)

    known = {sid for s in spans.values() for sid, _, _ in s}
    for row in labels:
        missing = set(row["gold_all"]) - known
        if missing:
            raise SystemExit(f"{row['qid']}: label points at unknown section(s) {sorted(missing)}")

    if args.chunking == "headings":
        nodes = MarkdownNodeParser().get_nodes_from_documents(docs)
    else:
        nodes = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP).get_nodes_from_documents(docs)
    for node in nodes:
        node.metadata = {}
        node.excluded_embed_metadata_keys = []
        node.excluded_llm_metadata_keys = []

    chunks = {}
    for node in nodes:
        slug = node.ref_doc_id
        rng = ((node.start_char_idx, node.end_char_idx)
               if node.start_char_idx is not None and node.end_char_idx is not None else None)
        secs = sections_for_chunk(*rng, spans[slug]) if rng else []
        if not secs:  # MarkdownNodeParser may drop char offsets; fall back to matching the text
            text = node.get_content().strip()
            body = next(d.text for d in docs if d.id_ == slug)
            pos = body.find(text[:200])
            if pos >= 0:
                rng = (pos, pos + len(text))
                secs = sections_for_chunk(*rng, spans[slug])
        chunks[node.node_id] = {"article": slug, "sections": secs, "range": rng, "text": node.get_content()}
        if args.title_prefix:
            node.set_content(f"{titles[slug]}\n\n{node.get_content()}")

    if args.mock_embeddings:
        from llama_index.core import MockEmbedding
        embed_model = MockEmbedding(embed_dim=384)
        print("WARNING: mock embeddings. This run tests the pipeline only; its scores mean nothing.")
    else:
        embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)
    client = chromadb.EphemeralClient()
    collection = client.get_or_create_collection(f"{args.run_name}_{datetime.now().strftime('%H%M%S%f')}")
    storage = StorageContext.from_defaults(vector_store=ChromaVectorStore(chroma_collection=collection))
    index = VectorStoreIndex(nodes, storage_context=storage, embed_model=embed_model)
    retriever = index.as_retriever(similarity_top_k=TOP_K)

    results = []
    for row in labels:
        hits = retriever.retrieve(row["question"])
        retrieved = [
            {
                "rank": i,
                "score": round(h.score, 4),
                "sections": chunks[h.node.node_id]["sections"],
                "text": chunks[h.node.node_id]["text"],
            }
            for i, h in enumerate(hits, start=1)
        ]
        results.append({
            "qid": row["qid"],
            "category": row["category"],
            "register": row.get("register", ""),
            "question_type": row.get("question_type", ""),
            "question": row["question"],
            "gold_all": row["gold_all"],
            "gold_primary": row["gold_primary"],
            "is_gap": row["is_gap"],
            "rank_all": first_hit_rank(retrieved, row["gold_all"]),
            "rank_primary": first_hit_rank(retrieved, row["gold_primary"]),
            "first_hit_gold_share": next((gold_share(chunks[h.node.node_id], row["gold_all"], spans)
                                          for h in hits if set(chunks[h.node.node_id]["sections"]) & set(row["gold_all"])), None),
            "strict_rank": next((i for i, h in enumerate(hits, start=1)
                                 if gold_share(chunks[h.node.node_id], row["gold_all"], spans) >= 0.5), None),
            "retrieved": retrieved,
        })

    scored = [r for r in results if not r["is_gap"]]
    summary = {
        "primary_and_alternates": summarize(scored, "rank_all"),
        "primary_only": summarize(scored, "rank_primary"),
        "strict_majority_gold": summarize(scored, "strict_rank"),
        "coverage_gaps_excluded": [r["qid"] for r in results if r["is_gap"]],
    }

    multi = sum(1 for c in chunks.values() if len(c["sections"]) > 1)
    run = {
        "run_name": args.run_name,
        "run_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": {
            "chunking": args.chunking,
            "chunk_size_tokens": CHUNK_SIZE if args.chunking == "fixed" else None,
            "chunk_overlap_tokens": CHUNK_OVERLAP if args.chunking == "fixed" else None,
            "splitter": ("SentenceSplitter (length-based, no heading awareness)" if args.chunking == "fixed"
                         else "MarkdownNodeParser (one chunk per heading section)"),
            "title_prefix": args.title_prefix,
            "frontmatter": "stripped",
            "embed_model": "MOCK (pipeline test only)" if args.mock_embeddings else EMBED_MODEL,
            "query_instruction": None,
            "vector_store": "ChromaDB, in-memory, fresh collection",
            "top_k": TOP_K,
        },
        "versions": {
            "python": platform.python_version(),
            **{p: pkg_version(p) for p in [
                "llama-index-core", "llama-index-embeddings-huggingface",
                "llama-index-vector-stores-chroma", "chromadb",
                "sentence-transformers", "torch",
            ]},
        },
        "corpus": {
            "articles": len(docs),
            "sha256_prefix": hashes,
            "chunks": len(chunks),
            "chunks_spanning_multiple_sections": multi,
        },
        "summary": summary,
        "questions": results,
    }

    args.out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    (args.out / f"{args.run_name}-{stamp}.json").write_text(json.dumps(run, indent=2), encoding="utf-8")
    (args.out / f"{args.run_name}-{stamp}.md").write_text(render_markdown(run), encoding="utf-8")
    with (args.out / f"{args.run_name}-{stamp}-chunks.jsonl").open("w", encoding="utf-8") as f:
        for cid, c in chunks.items():
            f.write(json.dumps({"chunk_id": cid, **c}) + "\n")

    print(render_markdown(run, brief=True))
    print(f"\nWrote results to {args.out.resolve()}")


def render_markdown(run, brief=False):
    s = run["summary"]
    lines = [f"# {run.get('run_name', 'act1')} retrieval results", ""]
    lines.append(f"Run at {run['run_at_utc']} | {run['corpus']['articles']} articles | "
                 f"{run['corpus']['chunks']} chunks ({run['corpus']['chunks_spanning_multiple_sections']} span more than one section)")
    lines += ["", "| Scoring | n | hit@3 | hit@5 | MRR@5 |", "|---|---|---|---|---|"]
    for name, key in [("Primary + alternates", "primary_and_alternates"), ("Primary only", "primary_only"),
                      ("Strict: chunk is at least half gold text", "strict_majority_gold")]:
        m = s.get(key)
        if m:
            lines.append(f"| {name} | {m['n']} | {m['hit_rate@3']} | {m['hit_rate@5']} | {m['mrr@5']} |")
    share = s["primary_and_alternates"].get("mean_gold_share_of_first_hit")
    if share is not None:
        lines.append(f"\nOn average, {round(share * 100)}% of the first matching chunk's text belongs to a correct section.")
    lines += ["", "| qid | rank (all) | rank (primary) | strict rank | gold share | top result's sections | gold |", "|---|---|---|---|---|---|---|"]
    for q in run["questions"]:
        top = ", ".join(q["retrieved"][0]["sections"]) if q["retrieved"] else "-"
        gold = "GAP" if q["is_gap"] else ", ".join(q["gold_all"])
        gs = q.get("first_hit_gold_share")
        lines.append(f"| {q['qid']} | {q['rank_all'] or 'miss'} | {q['rank_primary'] or 'miss'} | {q.get('strict_rank') or 'miss'} | {'-' if gs is None else gs} | {top} | {gold} |")
    if not brief:
        lines += ["", "## Config", "", "```json", json.dumps(run["config"], indent=2), "```",
                  "", "## Versions", "", "```json", json.dumps(run["versions"], indent=2), "```",
                  "", "## Corpus hashes", "", "```json", json.dumps(run["corpus"]["sha256_prefix"], indent=2), "```"]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
