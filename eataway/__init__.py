# -*- coding: utf-8 -*-

"""
===============
Eat Away Filter
===============

An image filter that slowly eats the content away.
"""

from __future__ import division, print_function, absolute_import
from importlib.metadata import version

from eataway.filter import (
    eat_image_away,
    merge_into_an_animation)

__author__ = 'Moodule'
__email__ = 'moodule@protonmail.com'
__version__ = version(__package__.split('.')[0])
__title__ = 'eataway'
__description__ = 'An image filter that slowly eats the content away'
__url__ = 'https://github/moodule/eataway'
__license__ = 'MIT license'

__all__ = [
    eat_image_away,
    merge_into_an_animation]
