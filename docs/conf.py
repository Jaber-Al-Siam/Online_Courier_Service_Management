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
import datetime
import django
from recommonmark.parser import CommonMarkParser

django_version = ".".join(map(str, django.VERSION[0:2]))
python_version = ".".join(map(str, sys.version_info[0:2]))

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Online_Courier_Service_Management.settings'

django.setup()

# -- Project information -----------------------------------------------------

# See https://pypi.org/project/sphinxcontrib-django/
project = 'Online Courier Service Management'
year = datetime.date.today().year
# copyright = '2021, Jaber Al Siam'
copyright = '2018-{}, The Developers'.format(year)
author = 'Jaber Al Siam'

# The full version, including alpha/beta/rc tags
release = '1.0'

# Auto-generate API documentation.
# os.environ['SPHINX_APIDOC_OPTIONS'] = "members,undoc-members,show-inheritance"
os.environ['SPHINX_APIDOC_OPTIONS'] = "members,show-inheritance"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.apidoc',  # runs sphinx-apidoc automatically as part of sphinx-build
    'sphinx.ext.autodoc',  # the autodoc extensions uses files generated by apidoc
    'sphinxcontrib_django',  # does some nicer django autodoc formatting, but:
    # https://github.com/edoburu/sphinxcontrib-django/issues/12
    'sphinx.ext.viewcode',  # enable viewing autodoc'd code
    'sphinx.ext.intersphinx',  # make links between different sphinx-documented packages
    'sphinx.ext.todo',  # TODO: figure out how to use this;-)
    'sphinx_markdown_tables',  # CommonMark doesn't do tables: This extensions does!
    'sphinxcontrib.confluencebuilder',  # supposedly installs docs on Confluence
    'sphinx.ext.graphviz',  # Support creating charts!
    'celery.contrib.sphinx',  # Celery improvements!
    'sphinx_autodoc_annotation',  # Parses Python 3 annotations
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]

source_parsers = {
    '.md': CommonMarkParser,
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

autosummary_generate = True  # Turn on sphinx.ext.autosummary

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'default'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # these are for sphinx_rtd_theme:
    'prev_next_buttons_location': 'both',
    'collapse_navigation': True,
    # these are for alabaster:
    # 'show_relbars': True,
    # 'fixed_sidebar': True,
    # 'sidebar_collapse': True,
}

# also for alabaster theme:
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

celery_task_prefix = '(task)'  # < default

# -- Extension configuration -------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = False

apidoc_module_dir = '../'
apidoc_output_dir = 'apidoc'
apidoc_excluded_paths = ['../migrations']
apidoc_separate_modules = True
apidoc_toc_file = False
apidoc_module_first = True
apidoc_extra_args = ['-f']

confluence_publish = True
confluence_server_url = os.environ.get('CONFLUENCE_SERVER', "https://confluence.columbia.edu")
confluence_space_name = os.environ.get('CONFLUENCE_SPACE', None)
confluence_parent_page = os.environ.get('CONFLUENCE_PARENT', None)
confluence_server_user = os.environ.get('CONFLUENCE_USER', None)
confluence_server_pass = os.environ.get('CONFLUENCE_PASS', None)

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/{}'.format(python_version), None),
    'django': ('https://docs.djangoproject.com/en/{}/'.format(django_version),
               'https://docs.djangoproject.com/en/{}/_objects/'.format(django_version)),
    # not sure why but the default lookup of objects.inv fails with None
    'djangorestframework-jsonapi': ('https://django-rest-framework-json-api.readthedocs.io/en/stable/',
                                    'https://django-rest-framework-json-api.readthedocs.io/en/stable/objects.inv'),
    # DRF doesn't use sphinx but rather mkdocs:-(
    # 'djangorestframework': ('https://django-rest-framework.org/', None),
}
