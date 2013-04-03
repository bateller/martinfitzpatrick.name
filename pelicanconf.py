#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Martin Fitzpatrick'
SITENAME = u'Game of Life Science'
SITEURL = 'http://golifescience.com'
FEED_DOMAIN = SITEURL

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

ARTICLE_URL = '{slug}.html'
PAGE_URL = 'pages/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'

DELETE_OUTPUT_DIRECTORY = False
