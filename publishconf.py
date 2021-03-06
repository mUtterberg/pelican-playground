#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://mutterberg.github.io/pelican-playground'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{ slug }.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
# Not necessary for project pages:
GOOGLE_ANALYTICS = "UA-111890368-6"
TWITTER_USERNAME = "mutterberg"
GITHUB_CORNER_URL = 'https://github.com/mUtterberg/pelican-playground'
MENUITEMS = [('My #100DaysOfCode Project Home', 'https://mutterberg.github.io/'),
            ('My Pelican Project Home', 'https://mutterberg.github.io/pelican-playground')]
