#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ############## General Settings #################
AUTHOR = 'Zach McCormick'
SITENAME = "Zach McCormick's Personal Blog"
SITEURL = 'https://z11k.com'
DESCRIPTION = 'My blog and stuff ...'
TIMEZONE = 'America/New_York'
# TODO come up with a better tagline
THEME = 'theme/elegant'
# TODO make theme responsive
PATH = 'content'

# TODO support spanish, translate articles
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# ############## URLS #################
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
RELATIVE_URLS = True

# ############## STATIC FILES #################
STATIC_PATHS = ['images', 'extras/favicon.png', 'extras/favicon.ico']
EXTRA_PATH_METADATA = {
    'extras/favicon.png': {'path': 'favicon.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'}
}

# ############## Markdown Settings #################
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Random theme settings

LANDING_PAGE_ABOUT = {'title': 'Zach McCormick',
                      'details': '<p>Zach is a software engineer and manager passionate about building and maintaining global-scale distributed systems. '
                                 'He has experience with distributed systems, web applications, and mobile applications across a variety of industries, '
                                 'including marketing automation, fintech, IoT, healthcare, and mobile cybersecurity, as well as across a variety of '
                                 'languages and technologies, including Python, Java, JavaScript, Ruby, PostgreSQL, MySQL, MongoDB, Redis, and '
                                 'others. He currently works for Braze managing the engineering team behind Canvas, a workflow engine for marketing '
                                 'automation that is responsible for orchestrating hundreds of millions of messages per day.</p>'
                      }
PROJECTS = [
    {
        'name': 'Django on Heroku',
        'url': 'https://github.com/ColossusInnovation/django-on-heroku',
        'description': 'Template for developing modern Django applications on Heroku '
                       'using Redis and Postgres for data stores and queues, and '
                       'using Celery for asynchronous tasks.',
    },
    {
        'name': 'Django GIS on Heroku',
        'url': 'https://github.com/ColossusInnovation/django-gis-on-heroku',
        'description': 'A guide and template for using GeoDjango - a Django '
                       'configuration with GIS support. This template also uses '
                       'Redis, Postgres, and Celery.',
    },
    {
        'name': 'Django React Multi-Page on Heroku',
        'url': 'https://github.com/ColossusInnovation/django-react-multi-page-on-heroku',
        'description': 'A template for combining Django with React by rendering individual '
                       'applications as Django pages (with initial state provided by the view). '
                       'Uses Redis, Postgres, and Celery.',
    },
    {
        'name': 'Django Related Select',
        'url': 'https://github.com/zachmccormick/django-related-select',
        'description': 'Adds AJAX-powered select fields to Django in a DRY way.',
    },
]

TWITTER_USERNAME = "zachmccormick"
GOOGLE_ANALYTICS = "UA-134718312-1"

PLUGIN_PATH = 'plugins'
PLUGINS = ['tipue_search', 'sitemap']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
