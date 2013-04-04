#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Martin Fitzpatrick'
AUTHOR_EMAIL = u'martin.fitzpatrick@gmail.com'
SITENAME = u'Game of Life Science'
SITESUBTITLE = u'Bioinformatics to Bedside'
SITEURL = 'http://golifescience.com'
FEED_DOMAIN = SITEURL

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PLUGINS = [
        'pelican.plugins.gravatar',
        'pelican.plugins.related_posts',
        'pelican.plugins.github_activity',
        'pelican.plugins.gzip_cache',   
        'pelican.plugins.sitemap',
        ]

# Blogroll
LINKS =  (
            ('OpenScience', 'http://openscience.org'),
            ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
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
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_ACTIVITY_FEED = 'https://github.com/mfitzp.atom'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DISQUS_SITENAME = 'golifescience'
GOOGLE_ANALYTICS = 'UA-341253-5'
GITHUB_URL = 'https://github.com/mfitzp'

TWITTER_USERNAME = 'golifescience'

THEME = 'theme'
