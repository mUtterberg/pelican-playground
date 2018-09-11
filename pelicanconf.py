#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marissa Utterberg'
SITENAME = 'My Pelican Playground'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

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
         ('Source for this project on GitHub', 'https://github.com/mUtterberg/pelican-playground/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('mUtterberg on Twitter', 'https://www.twitter.com/mutterberg'),
          ('mUtterberg on GitHub', 'https://github.com/mUtterberg/'),
          ('Marissa Utterberg on LinkedIn', 'https://www.linkedin.com/in/marissautterberg/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'notmyidea'
