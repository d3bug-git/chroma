#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from enum import IntEnum,unique

__all__ = ['Broche','POSITION_FOR_CHANNEL_A0',]


@unique
class Broche(IntEnum):

    BUTTON_OK = 11
    BUTTON_STOP = 15
    BUTTON_PLUS = 12
    BUTTON_MOINS = 16

    SELECTOR_VMAX_IN_POSITION_05 = 18 #means selector_0.5
    SELECTOR_VMAX_IN_POSITION_1 = 29
    SELECTOR_VMAX_IN_POSITION_2= 31
    SELECTOR_VMAX_IN_POSITION_5 = 33
    SELECTOR_VMAX_IN_POSITION_10 = 35

    I2C_SDA = 3
    I2C_SCL = 5

    MACHINE_1 = 36
    MACHINE_2 = 37

    @staticmethod
    def getBroche(broche:int):
        for b in Broche:
            if b.value == broche:
                return b
        raise Exception("la broche ",broche," n'existe pas dans Broche")

POSITION_FOR_CHANNEL_A0 = {
    Broche.SELECTOR_VMAX_IN_POSITION_05.value,
    Broche.SELECTOR_VMAX_IN_POSITION_1.value,
    Broche.SELECTOR_VMAX_IN_POSITION_2.value,
    Broche.SELECTOR_VMAX_IN_POSITION_5.value,
}
POSITION_FOR_CHANNEL_A1 = {
    Broche.SELECTOR_VMAX_IN_POSITION_10.value
}
VMAX_FOR_CHANNEL_A0 = {
    str(Broche.SELECTOR_VMAX_IN_POSITION_05.value):0.5,
    str(Broche.SELECTOR_VMAX_IN_POSITION_1.value):1,
    str(Broche.SELECTOR_VMAX_IN_POSITION_2.value):2,
    str(Broche.SELECTOR_VMAX_IN_POSITION_5.value):5,
}
VMAX_FOR_CHANNEL_A1 = {
    str(Broche.SELECTOR_VMAX_IN_POSITION_10.value):10
}