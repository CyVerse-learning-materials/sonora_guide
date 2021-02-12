#!/usr/bin/env python3
# Version 2.0, May 2020
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from misc.cyverse_sphinx_conf import *  # noqa

project = 'Sonora Discovery Environment Guide'
copyright = '2021, CyVerse'
author = 'CyVerse Documentation Team'
version = '0.1'
release = '0.1'

epub_title = Discovery Environment 2.0 Platform Guide
epub_author = Sriram Srinivasan, Ian McEwen, Ashley Ramsey, Sarah Roberts, Paul Sandoval, John Wregglesworth, Tina Lee, and Jason Williams
epub_publisher = CyVerse
epub_copyright = 2021

# html theme configuration -- see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme_options = {
# Table of Content options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
