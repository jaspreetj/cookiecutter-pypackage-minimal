from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

project = "{{ cookiecutter.package_name }}"
version = "{{ cookiecutter.package_version }}"
copyright = "2019, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"

master_doc = "index"
html_theme = "sphinx_rtd_theme"
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

source_parsers = {".md": CommonMarkParser}
source_suffix = [".rst", ".md"]

html_static_path = ["_static"]
htmlhelp_basename = project

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.linkcode",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_markdown_tables",
]

# Order members by source
autodoc_member_order = "bysource"


def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {"auto_toc_tree_section": "Contents", "enable_eval_rst": True},
        True,
    )
    app.add_transform(AutoStructify)


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return "{{ cookiecutter.package_url }}/blob/master/{}.py".format(filename)
