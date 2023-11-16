# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MicroGridsPy'
copyright = '2021, SESAM Polimi'
author = 'SESAM Polimi'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

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

def setup(app):
    app.add_css_file(None, body="""
    <style type="text/css">
        img {
            margin-bottom: 10px; /* Adds space below the image */
            display: block; /* Ensures the image is treated as a block-level element */
            margin-left: auto; /* Horizontally centers the image */
            margin-right: auto;
        }
    </style>
    """)
