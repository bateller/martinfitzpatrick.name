#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://martinfitzpatrick.name'
STATICURL = 'http://static.martinfitzpatrick.name'

DELETE_OUTPUT_DIRECTORY = True

PLUGIN_PATH = '/home/spenglr/pelican-plugins'

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

ARTICLE_URL = 'article/{slug}/'
PAGE_URL = '{slug}/'
AUTHOR_URL = 'author/{slug}/'
CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tag/{slug}/'
