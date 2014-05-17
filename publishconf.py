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
ARTICLE_SAVE_AS = 'article/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'