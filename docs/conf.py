# Configuration file for the Sphinx documentation builder.
import os, sys

# -- Project information

project = 'SBC Run Control'
copyright = '2024-2025 SBC Collaboration'
author = 'SBC Collaboration'

release = '0.4.2'
version = '0.4.2'

# -- General configuration

extensions = [
    "myst_parser",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

# Add icon
html_static_path = ['../resources']
html_favicon = '../resources/sbc_icon.png'

# Set each section is a chapter in pdf file
latex_toplevel_sectioning = 'chapter'

# Remove blank pages in pdf file
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

# set up mock imports
autodoc_mock_imports = ['red_caen', "ui", "resources_rc"]

sys.path.insert(0, os.path.abspath(".."))

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
