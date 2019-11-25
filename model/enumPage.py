#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from enum import Enum

__all__ =['Page',]

class Page(Enum):
    HOME = 1
    INSERT_USB = 2
    CONFIG_TIME = 3
    CONFIRM_ANALYSE =4
    REAL_TIME_GRAPH = 5
        
    @staticmethod
    def getPage(page:int):
        for p in Page:
            if p.value == page:
                return p
        return Page.HOME