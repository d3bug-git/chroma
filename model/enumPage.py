#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from enum import Enum

__all__ =['Page',]

class Page(Enum):
    PAGE_CHANGED = 0
    HOME = 1
    INSERT_USB = 2
    CONFIG_TIME = 3
    CONFIRM_ANALYSE =4
    REAL_TIME_GRAPH = 5