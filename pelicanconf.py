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
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/golifescience'),
          ('Facebook', 'https://facebook.com/research.abl.es'),
          ('Google+', 'https://plus.google.com/100813895193053083791'),
        )

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

ARTICLE_URL = '{slug}'
PAGE_URL = 'pages/{slug}'
AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'

DISQUS_SITENAME = 'golifescience'
GOOGLE_ANALYTICS = 'UA-341253-5'
GITHUB_URL = 'https://github.com/mfitzp'

TWITTER_USERNAME = 'golifescience'

THEME = 'theme'
