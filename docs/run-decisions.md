# Act 1: decisions to fix before running

Settle these before the first run and log them in the decision log. Changing them after seeing results is fitting to the test.

## 1. Chunk size (the big one)

The articles are 400 to 780 words, about 550 to 1,050 tokens. LlamaIndex's default splitter uses 1,024-token chunks, so with true defaults most articles become **one chunk each**. Retrieval then only has to find the right article, never the right section, and the baseline says almost nothing about structure.

| Option | What it tests | Trade-off |
|---|---|---|
| A. Library default (1,024 tokens, 200 overlap) | The literal "default chunking" in the plan | Mostly one chunk per article, so it's a weak baseline |
| B. Fixed small size (e.g. 256 tokens, 20 overlap), ignoring headings | A common naive setup that splits mid-section | Shows the cut-off conditional and severed-sequence failures the checklist targets |

Recommendation: **B**, with the reason logged. It's still naive (fixed size, no awareness of headings), and it's the setup the Chunk-Safe Writing Checklist was built to defend against. If time allows, run A as well and report both.

## 2. Frontmatter in the naive baseline

"No metadata" can mean two things: strip the frontmatter, or leave it in the text as a raw dump. Stripping is cleaner. Leaving it in is more realistic for a careless pipeline, but the YAML gets embedded into the first chunk of every article.

Recommendation: **strip it**, so Act 1 measures the prose alone and Act 2's metadata is a clean addition.

## 3. Scoring rules

- **Hit:** a retrieved chunk counts as a hit if it overlaps the text of any labeled section (primary or alternate). Chunks that span two sections count for both.
- **k values:** report hit-rate@3 and @5, plus MRR (rank of the first hit).
- **Q14 (gap):** excluded from hit-rate and MRR, and reported separately with what it retrieved.
- **Primary-only:** also reported, as a stricter secondary number.

## 4. Models and versions

- Embeddings: one specific BGE model, named exactly (e.g. `BAAI/bge-small-en-v1.5`)
- Vector store: ChromaDB, fresh collection per run
- Record Python, LlamaIndex, ChromaDB and sentence-transformers versions in the results file
- Retrieval only for this run. Ollama and Llama 3 come in when answer quality is scored.

## 5. Freeze the corpus

Commit the seven articles and tag the commit (e.g. `kb-v1`) before running, so every result points at an exact version. Act 2 content changes go on top of that tag.

## 6. Keep the held-out set out of the run

Keep the 7 held-out questions in a separate file the script never reads. They stay sealed until the Act 2 redesign is frozen.
