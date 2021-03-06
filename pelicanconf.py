#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Martin Fitzpatrick'
AUTHOR_EMAIL = u'martin.fitzpatrick@gmail.com'
AUTHOR_ABOUT = u"Python coder, postgraduate researcher and bioinformatician."
SITENAME = u'Martin Fitzpatrick'
SITESUBTITLE = u'Python coder, postgraduate researcher and bioinformatician.'
SITEURL = 'http://mfitzp.io'
SITEDESCRIPTION = u'''Python coder and postgraduate bioinformatician with a background in 
proteomics and metabolomics. Building online courses and writing books on data science and 
PyQt graphical application development. 
'''

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

from datetime import datetime
CURRENT_YEAR = datetime.now().year

AUTHOR_IDENTITIES = {
    'Martin Fitzpatrick':'https://plus.google.com/115539678583643563408',
}

SITE = {
    'owner': {'twitter':'mfitzp'},
}

MARKUP = ('md', 'rst', 'ipynb')

PLUGIN_PATHS = ['/Users/martin/repos/pelican-plugins',]
PLUGINS = [
        'gravatar',
        'related_posts',
        'sitemap',
        'summary',
        'series',
        'ipynb.markup',
        'related_posts',
        ]        


STATIC_PATHS = ['images',
                'extra/robots.txt',
                'extra/favicon.ico',
                'extra/.htaccess',]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},
    }

# Blogroll
LINKS =  (
            ('Pathomx', 'http://pathomx.org'),
            ('The Open Lab Book', 'http://theolb.readthedocs.org'),
            ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
            ('Python.org', 'http://python.org'),
        )

# Social widget
SOCIAL = ([
          ('Email', 'envelope-o', 'mailto:%s' % AUTHOR_EMAIL),
          ],[
          ('Github', 'github-alt', 'https://github.com/mfitzp'),
          ('StackOverflow', 'stack-overflow', 'http://stackoverflow.com/users/754456/mfitzp'),
          ],[
          ('Udemy', 'graduation-cap', 'https://www.udemy.com/u/martinfitzpatrick4/'),
          ('YouTube', 'youtube-play', 'https://www.youtube.com/channel/UCMW4KwSlygaDef0tgqPjbRQ'),
#          ('Teachable', 'graduation-cap', 'http://mfitzp.teachable.com/'),
#          ],[
#          ('Patreon', 'btc', 'https://www.patreon.com/mfitzp'),
#          ('PayPal', 'paypal', 'https://www.paypal.me/mfitzp/5'),
          ],[
          ('Codementor', 'code', 'https://www.codementor.io/mfitzp'),
#          ('hack.hands()', 'code', 'https://hackhands.com/mfitzp'),
          ],[
          ('Twitter', 'twitter', 'https://twitter.com/mfitzp'),
          ('LinkedIn', 'linkedin', 'https://uk.linkedin.com/in/martinfitzp'),
#          ('Facebook', 'facebook', 'https://www.facebook.com/martinfitzp'),
          ('Google+', 'google-plus', 'https://plus.google.com/115539678583643563408/?rel=author'),
          ],[
          ('ORCID', 'circle', 'http://orcid.org/0000-0002-0695-1988'),
          ('ResearchGate', 'list', 'https://www.researchgate.net/profile/Martin_Fitzpatrick/'),
          ],[
          ('RSS', 'rss', '%s/%s' % (FEED_DOMAIN, FEED_ATOM) ),
          ],
        )

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

TYPOGRIFY = True
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_ACTIVITY_FEED = 'https://github.com/mfitzp.atom'
WITH_FUTURE_DATES = False

AUTHOR_BIO = {
 'Martin Fitzpatrick':1,


}


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}


ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'


DISQUS_SITENAME = 'golifescience'
GOOGLE_ANALYTICS = 'UA-341253-5'
GITHUB_URL = 'https://github.com/mfitzp'

TWITTER_USERNAME = 'mfitzp'

THEME = 'theme'


SITEURL = 'http://localhost:8000'
STATICURL = 'http://localhost:8000'

DELETE_OUTPUT_DIRECTORY = True

ADDRESS = u"℅ Martin Fitzpatrick<br /> \
Utrecht<br /> \
Netherlands<br />"

# Special categories to show with descriptions + priority
SPECIAL_CATEGORIES = {
'publications': 'Academic publications, posters, abstracts and other materials.',
'books': 'Books, e-books and other written materials.',
'courses': 'Online courses, materials and guides for novice programmers.',
'apps': 'Software applications and command line tools developed by myself. Unless I have taken temporary leave of my senses all of it will be under the GPLv3 license.',
'libs': 'Software libraries developed by myself. Unless I have taken temporary leave of my senses all of it will be under the MIT/BSD license.',
'games': 'Games, mostly historic because I got all serious in my old age.',
#'Talks': 'Conference talks and presentations.'
#'pathomx': 'Updates, guides and videos relating to the Pathomx platform',
#'video': 'Instructional videos and guides.',
}

SPECIAL_PAGES = ['Hire']
CUSTOM_PAGES = [('Store','//store.mfitzp.io')]
SPECIAL = ['publications','books','courses','apps','libs','games']

#=============
# Twitter Card
#=============
# https://dev.twitter.com/cards
TWITTER_CARD_USE = (True) # (False)
TWITTER_CARD_SITE = '@mfitzp'  # The site's Twitter handle like @my_blog
TWITTER_CARD_CREATOR = '@mfitzp'  # Your twitter handle like @monkmartinez
TWITTER_CARD_DOMAIN = 'martinfitzpatrick.name'  # The site domain
GRAVARTAR_URL = ''

GOOGLE_PLUS_PUBLISHER = 'https://plus.google.com/115539678583643563408'
