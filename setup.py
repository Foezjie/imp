from setuptools import setup

setup(
    name = "imp",
    package_dir = {"" : "src" },
    packages = ["Imp.jinja2", "Imp.jinja2._markupsafe", "Imp.antlr3", "Imp.parser", "Imp.export", "Imp", "Imp.ast.constraint", "Imp.ast.statements", "Imp.ast", "Imp.plugins", "Imp.compiler", "Imp.execute", "Imp.agent", "Imp.server", "Imp.agent.plugins", "Imp.stats"],
    version = "0.2",
    description = "Infrastructure management platform",
    author = "Bart Vanbrabant",
    author_email = "bart.vanbrabant@cs.kuleuven.be",
    license = "LICENSE",

    scripts = ["bin/imp"],
    package_data = {"" : ["Imp/server/static/*", "Imp/server/template/*"]},
    include_package_data = True,
)
