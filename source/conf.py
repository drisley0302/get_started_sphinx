# -*- coding: utf-8 -*-
#
# 
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'Family Guide to Dementia Care'
copyright = u'2019, Dana Risley'
author = u'Dana Risley'


#version = u'1.0'
# The full version, including alpha/beta/rc tags.
#release = u'1.0'


language = None


pygments_style = 'sphinx'

#Here's where to find some themes: https://www.sphinx-doc.org/en/master/usage/theming.html?highlight=theme
#html_theme = 'default'
#html_theme = 'agogo'
#html_theme = 'alabaster'
#html_theme = 'bizstyle'
html_theme = 'classic'
#html_theme = 'haiku'
#html_theme = 'nature'
#html_theme = 'pyramid'
#html_theme = 'scrolls'
#html_theme = 'sphinxdoc'
#html_theme = 'traditional'

html_theme_options = {

  "footerbgcolor": "#002080",
  "sidebarbgcolor": "#30819c",
  "sidebarlinkcolor": "#000000",
  "relbarbgcolor": "#002080",
  "headtextcolor": "#002080",
  "linkcolor": "#30819c",
  "visitedlinkcolor": "#002080",

}

rst_epilog = """
.. include:: substitutions.txt
"""







