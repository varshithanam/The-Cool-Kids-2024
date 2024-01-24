extensions = ['sphinx_simplepdf', 
              'breathe', 
              'myst_parser', 
              'sphinx_rtd_theme' ]

# Read from rst and md files
source_suffix = ['.rst', '.md']

root_doc = 'index'

project = 'Untitled Project'
copyright = '2023'
author = 'Alexander Hooper, Ethan Timpe, Hana Tollossa, Jahcorian Ivery, Varshitha Thanam'
show_authors = True
version = '0.0.1'
release = 'test'

# HTML theming
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'titles_only': False,
    'navigation_depth': 2
}

def setup(app):
    app.add_css_file('theme.css')