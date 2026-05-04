# narratives

Companion repo to [2i2c-org/initiatives](https://github.com/2i2c-org/initiatives) containing narratives.
Nrratives are descriptions of problem spaces 2i2c is investing in, and a way to weave together many initiatives.
Each issue in this repository is a narrative.

**🚨 Experimental**: This is an experiment, and subject to change quickly.

## Documentation

We publish a small MyST site that exposes the issues of this repository (narratives) in an easy-to-reference way.
It is hosted on GitHub Pages at https://2i2c.org/narratives

Build it locally with these commands (the `gh` CLI will need to be installed as well):

```bash
nox -s docs       # build static site to docs/_build/html
nox -s docs-live  # start MyST dev server
```

Both sessions first run `scripts/fetch_narratives.py` to pull the latest open issues and generate per-narrative pages under `docs/narrative/`.
