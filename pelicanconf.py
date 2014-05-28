#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Martin Fitzpatrick'
AUTHOR_EMAIL = u'martin.fitzpatrick@gmail.com'
AUTHOR_ABOUT = u"A final-year PhD student working on the metabolomics of inflammatory diseases."
SITENAME = u'Martin Fitzpatrick'
SITESUBTITLE = u'Postgraduate Researcher in Metabolomics and Immunology '
SITEURL = 'http://martinfitzpatrick.name'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

from datetime import datetime
CURRENT_YEAR = datetime.now().year

AUTHOR_IDENTITIES = {
    'Martin Fitzpatrick':'https://plus.google.com/115539678583643563408',
}

PLUGIN_PATH = '/home/spenglr/pelican-plugins'
PLUGINS = [
        'gravatar',
        'related_posts',
        #'pelican_youtube',
        'sitemap',
        'summary',
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
SOCIAL = (
          ('Twitter', 'twitter', 'https://twitter.com/mfitzp'),
          ('Facebook', 'facebook', 'https://www.facebook.com/martinfitzp'),
          ('Github', 'github', 'https://github.com/mfitzp'),
          ('ResearchGate', 'list', 'https://www.researchgate.net/profile/Martin_Fitzpatrick/'),
          ('LinkedIn', 'linkedin', 'https://uk.linkedin.com/in/martinfitzp'),
          ('Google+', 'google-plus', 'https://plus.google.com/115539678583643563408/?rel=author'),
          ('ORCID', 'circle', 'http://orcid.org/0000-0002-0695-1988'),
          ('RSS', 'rss', '%s/%s' % (FEED_DOMAIN, FEED_ATOM) ),
        )

DEFAULT_PAGINATION = 12

TYPOGRIFY = True
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_ACTIVITY_FEED = 'https://github.com/mfitzp.atom'


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


SITEURL = 'http://localhost:8001'
STATICURL = 'http://localhost:8001'

DELETE_OUTPUT_DIRECTORY = True

PLUGIN_PATH = '/Users/mxf793/repos/pelican-plugins'

ADDRESS = u"℅ Centre for Translational Inflammation Research<br /> \
Queen Elizabeth Hospital<br /> \
University of Birmingham<br /> \
Birmingham<br /> \
United Kingdom<br /> \
B15 2TT<br />"

PROJECTS = [
{
    'title': 'Accuri2FCS',
    'description': 'Convert Accuri .c6 files to .fcs standard',
    'url': 'https://github.com/mfitzp/accuri2fcs',
},
{
    'title': 'BioCyc',
    'description': 'Python interface to the BioCyc Web API',
    'url': 'http://github.com/mfitzp/BioCyc',
},
{
    'title': 'GPML2SVG',
    'description': 'A command-line/Python GPML to SVG pathway renderer',
    'url': 'http://github.com/mfitzp/gpml2svg',
},
{
    'title': 'Icoshift (Python)',
    'description': 'A Python implmentation of the Icoshift algorithm',
    'url': 'https://github.com/mfitzp/icoshift',
},
{
    'title': 'mplstyler',
    'description': 'An API for assigning consistent marker styles to Matplotlib plots.',
    'url': 'https://github.com/mfitzp/mplstyler',
},
{
    'title': 'The Open Lab Book',
    'description': 'Freely available lab protocols under a CC license',
    'url': 'http://theolb.readthedocs.org',
},
{
    'title': 'MetaboHunter',
    'description': 'A Python interface to the MetaboHunter 1D NMR metabolite identification service',
    'url': 'http://github.com/mfitzp/metabohunter',
},
{
    'title': 'Pathomx',
    'description': 'Workflow-based metabolomic analysis tool',
    'url': 'http://pathomx.org',
},
{
    'title': 'PyQtConfig',
    'description': 'A PyQt config manager. Keep Qt widgets in sync with an config dictionary and/or QSettings object. ',
    'url': 'https://github.com/mfitzp/pyqtconfig',
},
{
    'title': 'QtIPy',
    'description': 'IPython Notebook automator',
    'url': 'http://github.com/mfitzp/qtipy',
},
]


#=============
# Twitter Card
#=============
# https://dev.twitter.com/cards
TWITTER_CARD_USE = (True) # (False)
TWITTER_CARD_SITE = '@mfitzp'  # The site's Twitter handle like @my_blog
TWITTER_CARD_CREATOR = '@mfitzp'  # Your twitter handle like @monkmartinez
TWITTER_CARD_DOMAIN = 'martinfitzpatrick.name'  # The site domain
GRAVARTAR_URL = ''
