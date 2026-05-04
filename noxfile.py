import nox

nox.options.default_venv_backend = "uv"


@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    session.run("python", "scripts/fetch_narratives.py")
    with session.chdir("docs"):
        session.run("myst", "build", "--html")


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "requirements.txt")
    session.run("python", "scripts/fetch_narratives.py")
    with session.chdir("docs"):
        session.run("myst", "start")
