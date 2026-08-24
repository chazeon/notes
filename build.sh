#!/usr/bin/env sh
set -eu

if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git fetch --unshallow --no-tags
fi

if ! command -v uv >/dev/null 2>&1; then
    python3 -m pip install --disable-pip-version-check "uv==0.11.26"
    export PATH="$(python3 -m site --user-base)/bin:$PATH"
fi

uv sync --locked
uv run mkdocs build
