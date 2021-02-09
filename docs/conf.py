import asyncclick as click
from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

import asyncclick._compat

# compat until pallets-sphinx-themes is updated
click._compat.text_type = str

# Project --------------------------------------------------------------

project = "AsyncClick"
copyright = "2014 Pallets, 2019 Matthias Urlichs"
author = "Pallets"
release, version = get_version("asyncclick", version_length=1)

# General --------------------------------------------------------------

master_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
    "sphinx_issues",
    "sphinx_tabs.tabs",
]
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}
issues_github_path = "python-trio/asyncclick"

# HTML -----------------------------------------------------------------

html_theme = "click"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("Donate to Pallets", "https://palletsprojects.com/donate"),
        ProjectLink("Click Website", "https://palletsprojects.com/p/click/"),
        ProjectLink("PyPI releases", "https://pypi.org/project/click/"),
        ProjectLink("Source Code", "https://github.com/pallets/click/"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/click/issues/"),
        ProjectLink("AsyncClick Fork", "https://github.com/python-trio/asyncclick/"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}
html_static_path = ["_static"]
html_favicon = "_static/click-icon.png"
html_logo = "_static/click-logo-sidebar.png"
html_title = f"AsyncClick Documentation ({version})"
html_show_sourcelink = False

# LaTeX ----------------------------------------------------------------

latex_documents = [(master_doc, f"AsyncClick-{version}.tex", html_title, author, "manual")]
