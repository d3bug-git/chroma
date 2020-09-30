#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from enum import IntEnum, unique

__all__ = ['Broche', 'POSITION_FOR_CHANNEL_A0', ]


@unique
class Broche(IntEnum):

    BUTTON_OK = 24
    BUTTON_STOP = 6
    BUTTON_PLUS = 25
    BUTTON_MOINS = 5

    SELECTOR_VMAX_IN_POSITION_05 = 16  # means selector_0.5
    SELECTOR_VMAX_IN_POSITION_1 = 26
    SELECTOR_VMAX_IN_POSITION_2 = 8
    SELECTOR_VMAX_IN_POSITION_5 = 7
    SELECTOR_VMAX_IN_POSITION_10 = 20  # old position 1

    I2C_SDA = 2
    I2C_SCL = 3

    INPUT_VOLTAGE_SELECTOR_MACHINE = 22  # SURTENSION_10V = 22
    INPUT_VOLTAGE_SELECTOR_VMAX = 23  # SURTENSION_10V = 22
    #SURTENSION_5V = 23

    SWITCH_MACHINE_1 = 0
    SWITCH_MACHINE_2 = 19

    RELAY_MACHINE = 21
    SELECTOR_POSITION_MACHINE_1 = 27
    SELECTOR_POSITION_MACHINE_2 = 17

    @staticmethod
    def getBroche(broche: int):
        for b in Broche:
            if b.value == broche:
                return b
        raise Exception("la broche ", broche, " n'existe pas dans Broche")


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
    str(Broche.SELECTOR_VMAX_IN_POSITION_05.value): 0.5,
    str(Broche.SELECTOR_VMAX_IN_POSITION_1.value): 1,
    str(Broche.SELECTOR_VMAX_IN_POSITION_2.value): 2,
    str(Broche.SELECTOR_VMAX_IN_POSITION_5.value): 5,
}
VMAX_FOR_CHANNEL_A1 = {
    str(Broche.SELECTOR_VMAX_IN_POSITION_10.value): 10
}
