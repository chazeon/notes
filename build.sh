#!/usr/bin/env sh
set -eu

if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git fetch --unshallow --no-tags
fi

python3 -m pip install --disable-pip-version-check "uv==0.11.26"
uv sync --locked
uv run mkdocs build
