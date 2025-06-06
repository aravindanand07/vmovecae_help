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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

#import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'VCollab-Document'
copyright = '2025, Visual Collaboration Technologies Inc.'
author = 'VCollab'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.video',

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
master_doc = 'index'

#master_doc = 'VCollabPresenter'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'sticky_navigation':False,
    'collapse_navigation': True,
    'navigation_depth': 4,
    'logo_only': True,
     'style_nav_header_background':'#EDEDED',
     'prev_next_buttons_location': 'top',


}


html_show_sphinx = False
html_show_sourcelink = False

#html_logo = '_static/VCollab-Logo-wt.png'

# Add any paths that contain custom static files (such as style sheets) here,

# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files =['css/Custom.css']

html_logo = "_static/VCollab-Logo-wt.png"
