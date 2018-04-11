#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ############## General Settings #################
AUTHOR = 'Zach McCormick'
SITENAME = "Thoughts and Discoveries of z11k"
SITEURL = 'http://z11k.com'
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
                      'details': '<p>Zach graduated from Vanderbilt University with a BS in Computer Science and '
                                 'Mathematics in 2013. He has worked for a number of companies both as a FTE and '
                                 'consultant/contractor, and specializes in web applications, mobile applications, '
                                 'distributed systems, and software systems engineering. His main languages of choice '
                                 'are Python and Java, but has experience working on systems in JavaScript, '
                                 'Ruby, Groovy, and Scala as well.</p>'
                                 '<p>He currently works for Braze (formerly known as Appboy) as a Senior Software Engineer, working with '
                                 'technology like Ruby, Rails, Sidekiq, MongoDB, and more!</p>',
                      }
PROJECTS = [
    {
        'name': 'Django Heroku Template',
        'url': 'https://github.com/TrailblazingTech/django-heroku-template',
        'description': 'Template for developing modern Django applications on Heroku '
                       'using Redis and Postgres for data stores and queues, and '
                       'using Celery for asynchronous tasks.',
    },
    {
        'name': 'Django GIS Heroku Template',
        'url': 'https://github.com/TrailblazingTech/django-gis-heroku',
        'description': 'A guide and template for using GeoDjango - a Django '
                       'configuration with GIS support. This template also uses '
                       'Redis, Postgres, and Celery.',
    },
    {
        'name': 'Django Related Select',
        'url': 'https://github.com/zachmccormick/django-related-select',
        'description': 'Adds AJAX-powered select fields to Django in a DRY way.',
    },
]
