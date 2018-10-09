#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

AUTHOR = 'Marissa Utterberg'
SITENAME = 'My Pelican Playground'
SITESUBTITLE = 'A #100DaysOfCode Project'
SITEURL = 'https://mutterberg.github.io/pelican-playground'
SITELOGO = SITEURL + '/images/logo.png'

BROWSER_COLOR = '#3d4070'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = False

PATH = 'content'

TIMEZONE = 'America/New_York'
OC_LOCALE = 'en_US'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Utterberg Data & Development: Portfolio Site', 'https://utterbergdatadev.com'),
         ('Back to main DataDev #100DaysOfCode', 'https://datadev.me'),
         ('Source for this project on GitHub', 'https://github.com/mUtterberg/pelican-playground/'),)

# Social widget
SOCIAL = (('twitter', 'https://www.twitter.com/mutterberg'),
          ('github', 'https://github.com/mUtterberg/'),
          ('linkedin', 'https://www.linkedin.com/in/marissautterberg/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

LINKS_WIDGET_NAME = 'Other projects by Utterberg Data & Development'
SOCIAL_WIDGET_NAME = 'Connect'

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['always_modified',]

ALWAYS_MODIFIED = True
