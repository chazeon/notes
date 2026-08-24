#!/usr/bin/env sh
set -eu

if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git fetch --unshallow --no-tags
fi

if command -v uv >/dev/null 2>&1; then
    uv sync --locked
    uv run mkdocs build
else
    python3 -m pip install --disable-pip-version-check "uv==0.11.26"
    python3 -m uv sync --locked
    python3 -m uv run mkdocs build
fi
