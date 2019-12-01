#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from .broche import Broche
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

        #Button Ok
        GPIO.setup(Broche.BUTTON_OK.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_OK.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)
        
        #Button Stop
        GPIO.setup(Broche.BUTTON_STOP.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_STOP.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)

        #Button Plus
        GPIO.setup(Broche.BUTTON_PLUS.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_PLUS.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)

        #Button moins
        GPIO.setup(Broche.BUTTON_MOINS.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_MOINS.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)

    def sendHardwareEvent(self,broche):
        pub.sendMessage("HARDWARE_EVENT",broche = broche)
        
    def onClickButton(self,button):
        self.sendHardwareEvent(Broche.getBroche(button))
