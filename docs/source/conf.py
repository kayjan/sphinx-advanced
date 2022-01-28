# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'sphinx-advanced'
copyright = '2022, Kay Jan WONG'
author = 'Kay Jan WONG'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "autodocsumm",
    "nbsphinx",
    "myst_parser",
    "sphinxcontrib.confluencebuilder",
]
autodoc_default_options = {
    'autosummary': True
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "classic"
html_theme_options = {
    "rightsidebar": "true",
    "relbarbgcolor": "black"
}
html_favicon = '../../assets/documentation-icon.svg'
html_logo = '../../assets/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    app.add_css_file('custom.css')


# Confluence setup
CONFLUENCE_KEY = os.environ.get("CONFLUENCE_KEY")
CONFLUENCE_USER = os.environ.get("CONFLUENCE_USER")
assert CONFLUENCE_KEY, "There is no API key for Confluence"

confluence_publish = True
confluence_space_key = 'SPHINXADVA'
confluence_server_url = 'https://kayjan.atlassian.net/wiki/'
confluence_server_user = CONFLUENCE_USER
confluence_server_pass = CONFLUENCE_KEY
confluence_parent_page = 'Sphinx Documentation'
confluence_page_hierarchy = True
