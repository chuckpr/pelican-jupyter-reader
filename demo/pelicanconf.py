#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chuck Pepe-Ranney'
SITENAME = 'demo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# pelican-jupyter-settings
from pelican.plugins import pelican_jupyter_reader
PLUGINS = [pelican_jupyter_reader]
IGNORE_FILES = ['*checkpoint.ipynb']

# Instantiate a config object and call it NBCONVERT_CONFIG
from traitlets.config import Config
NBCONVERT_CONFIG = Config()

# This removes Jupyter input prompts
NBCONVERT_CONFIG.HTMLExporter.exclude_input_prompt = True

# This removes empty cells
NBCONVERT_CONFIG.RegexRemovePreprocessor.enabled = True
NBCONVERT_CONFIG.RegexRemovePreprocessor.patterns = ['\s*\Z']

# This makes Jupyter magic cells have proper code highlighting
# regardless of the language of the notebook kernel
NBCONVERT_CONFIG.HighlightMagicsPreprocessor.enabled = True

# This directs the NBConvert to a custom Jinja2 template
# names demo.tpl
NBCONVERT_CONFIG.HTMLExporter.template_path.append('.')
NBCONVERT_CONFIG.HTMLExporter.template_file = 'demo'

NBCONVERT_CONFIG.ExtractOutputPreprocessor.enabled = True
NBCONVERT_CONFIG.ExtractOutputPreprocessor.output_filename_template = \
    'images/{unique_key}_{cell_index}_{index}{extension}'
