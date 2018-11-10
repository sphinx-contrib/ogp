# -*- coding: utf-8 -*-

# -- Project information -----------------------------------------------------

project = 'Sphinx OGP support'
copyright = '2018, Takayuki Shimizukawa'
author = 'Takayuki Shimizukawa'

version = release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib_ogp',
]
og_site_url = 'http://sphinxcontrib-ogp.rtfd.io/'
og_twitter_site = '@shimizukawa'

source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
# html_theme_options = {}
