# slapec.hu

Source code for my personal website.

## Build

Build using the slpages commit pinned in `pyproject.toml` and `uv.lock`.

```sh
uv run --locked python build.py
```

If you have a local slpages checkout next to this repository at `../slpages`,
use it for local development. Changes in that checkout are picked up on the
next build, while the website's project configuration remains unchanged:

```sh
uv run --with-editable ../slpages python build.py
```

## Preview

Serve the generated site locally at <http://localhost:8000/>:

```sh
uv run --no-project python -m http.server --directory dist 8000
```
