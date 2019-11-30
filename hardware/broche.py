#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from enum import IntEnum,unique

__all__ = ['Broche']

@unique
class Broche(IntEnum):
    BUTTON_OK = 11
    BUTTON_STOP = 12
    BUTTON_PLUS = 13
    BUTTON_MOINS = 14