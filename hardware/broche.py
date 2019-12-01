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
    BUTTON_STOP = 15
    BUTTON_PLUS = 12
    BUTTON_MOINS = 16

    @staticmethod
    def getBroche(broche:int):
        for b in Broche:
            if b.value == broche:
                return b
        raise Exception("la broche ",broche," n'existe pas dans Broche")