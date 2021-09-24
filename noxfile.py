import sys

import nox


@nox.session
@nox.parametrize("django", ["2.2", "3.1", "3.2", "main"])
def test(session, django):
    if django == "main" and not sys.version_info.minor >= 8:
        session.skip()
    else:
        if django == "main":
            session.install("https://github.com/django/django/archive/main.tar.gz")
        else:
            session.install(f"django=={django}")
        session.run("python", "makemigrations.py")
        session.run("coverage", "run", "runtests.py")
        session.run("coverage", "report")
        session.run("coverage", "xml")
