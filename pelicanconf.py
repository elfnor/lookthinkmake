#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'elfnor'
SITENAME = u'Look Think Make'
SITEURL = 'http://elfnor.github.io/lookthinkmake/'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

#THEME  = 'simple-bootstrap'
THEME = 'themes/pelican-simplegrey-efh'
#BOOTSTRAP_THEME = 'spacelab'
#PYGMENTS_STYLE = 'default'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()
"""
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (('on deviant art', 'http://elfnor.deviantart.com'),
          ('on thingiverse', 'http://www.thingiverse.com/elfnor'),)

DEFAULT_PAGINATION = False

# static paths will be copied under the same name
STATIC_PATHS = ["images"]


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
