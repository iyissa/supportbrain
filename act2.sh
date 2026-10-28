#!/usr/bin/env bash
# SupportBrain Act 2: one change (heading-based chunking), same scoring as Act 1.
# From this folder, in Terminal:  bash act2.sh
set -euo pipefail
cd "$(dirname "$0")"
# shellcheck disable=SC1091
source .venv/bin/activate

echo "== 1. Re-scoring the Act 1 settings with the added strict measure (decision B10)"
python retrieval_eval.py --kb ./kb --labels labels.csv --out results --run-name act1-rescored --chunking fixed

echo "== 2. Act 2: one chunk per heading section, nothing else changed (decision B11)"
python retrieval_eval.py --kb ./kb --labels labels.csv --out results --run-name act2-headings --chunking headings

echo "== 3. Committing"
git add retrieval_eval.py act2.sh results
git commit -q -m "Act 2: heading-based chunking, plus strict scoring for both runs" && echo "Committed."
echo
echo "Done. Summaries are in results/act1-rescored-*.md and results/act2-headings-*.md"
