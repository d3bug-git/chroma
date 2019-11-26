#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from .broche import *
import RPi.GPIO as GPIO

from  utils.require import require
require("pypubsub")

from pubsub import pub

__all__ = ['Hardware']

class Hardware:
    
    __instance = None
    
    @staticmethod
    def getInstance():
        if Hardware.__instance == None:
            Hardware()
        return Hardware.__instance

    def __init__(self):
        if Hardware.__instance != None:
            raise Exception("Cette classe est un Singleton")
        else:
            Hardware.__instance = self
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(BUTTON_OK,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(BUTTON_OK,GPIO.RISING,callback=self.my_call,bouncetime=500)
        
    def my_call(self,BUTTON_OK):
        print("btn OK pressé")
        pub.sendMessage("HARDWARE_EVENT",button = BUTTON_OK)
        
