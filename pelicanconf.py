#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ############## General Settings #################
AUTHOR = 'Zach McCormick'
SITENAME = "Thoughts and Discoveries of Zach McCormick"
SITEURL = 'http://z11k.com'
DESCRIPTION = 'My blog and stuff ...'
TIMEZONE = 'America/New_York'
# TODO come up with a better tagline
THEME = 'theme/monospace'
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
