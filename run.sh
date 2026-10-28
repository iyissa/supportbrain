#!/usr/bin/env bash
# SupportBrain Act 1: set up and run the baseline in one go.
# From this folder, in Terminal:  bash run.sh
set -euo pipefail
cd "$(dirname "$0")"

echo "== 1. Checking Python"
PY=""
for c in python3.13 python3.12 python3.11 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if (3,10) <= sys.version_info[:2] < (3,14) else 1)'; then
    PY="$c"; break
  fi
done
if [ -z "$PY" ]; then
  echo "Need Python 3.10 to 3.13. Install one with:  brew install python@3.12   then run this again."
  exit 1
fi
echo "Using $("$PY" --version)"

echo "== 2. Checking predictions"
if ! grep -qiE '^\| Q[0-9]+ \|.*\| *(yes|no|unsure) *\|' predictions.md; then
  echo "No predictions filled in. Act 1 runs without them by choice (decision B9)."
  echo "Write predictions before the Act 2 rerun and before unsealing the held-out set."
fi

echo "== 3. Freezing the corpus in git"
if ! git config user.email >/dev/null; then
  echo "Git doesn't know who you are yet. Run these two lines, then run this script again:"
  echo '  git config --global user.name "Your Name"'
  echo '  git config --global user.email "you@example.com"'
  exit 1
fi
[ -d .git ] || git init -q
git add -A
git commit -q -m "KB v1 frozen, labels and predictions before Act 1" || echo "Nothing new to commit."
if git rev-parse -q --verify refs/tags/kb-v1 >/dev/null; then
  echo "Tag kb-v1 already exists."
else
  git tag kb-v1 && echo "Tagged kb-v1."
fi

echo "== 4. Installing packages (first time takes a few minutes, mostly PyTorch)"
[ -d .venv ] || "$PY" -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null
if ! pip install -r requirements.txt; then
  echo "Pinned install failed. Retrying with whatever PyTorch version fits this Mac."
  sed 's/^torch==.*/torch/' requirements.txt > .requirements-fallback.txt
  pip install -r .requirements-fallback.txt
fi

echo "== 5. Running Act 1 (the first run downloads the BGE model, about 130 MB)"
python act1_baseline.py --kb ./kb --labels labels.csv --out results

echo "== 6. Committing results"
git add results
git commit -q -m "Act 1 baseline results" && echo "Results committed."
echo
echo "Done. The summary is in results/act1-*.md"
