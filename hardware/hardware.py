#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from .broche import Broche,POSITION_FOR_CHANNEL_A0,POSITION_FOR_CHANNEL_A1,VMAX_FOR_CHANNEL_A0,VMAX_FOR_CHANNEL_A1
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

from  utils.require import require
require("pypubsub")

import threading 
import time 

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
        # Create an ADS1115 ADC (16-bit) instance.
        self.adc = Adafruit_ADS1x15.ADS1115()

        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Or pick a different gain to change the range of voltages that are read:
        #  - 2/3 = +/-6.144V
        #  -   1 = +/-4.096V
        #  -   2 = +/-2.048V
        #  -   4 = +/-1.024V
        #  -   8 = +/-0.512V
        #  -  16 = +/-0.256V
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        self.GAIN = 1
        self.CHANNEL_A0 =0
        self.CHANNEL_A1 =1
        self.CHANNEL_USED = None
        self.VMAX = None
        self.threadForReadAdc = threading.Thread(target = self.readAdcValueOfChannelAndSendMessage, args=(self.CHANNEL_USED,)) 

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

#********************************************** SELECTOR **********************************************

    def activateSelector(self):
        #selector in position 0.5
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_05.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_05.value,GPIO.RISING,callback=self.onTurnSelector,bouncetime=500)
        print("activate selector")
    
    def deactivateSelector(self):
        self.stopThreadForReadAdc()
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_05.value)
        print("deactivate selector")

#********************************************** END SELECTOR *******************************************
    
    def sendHardwareEvent(self,broche):
        pub.sendMessage("HARDWARE_EVENT",broche = broche)
        
    def onClickButton(self,button):
        self.sendHardwareEvent(Broche.getBroche(button))

    #think to do some thread who read all the 1s and send message
    def onTurnSelector(self,position):
        print("selector is turn")
        if position in POSITION_FOR_CHANNEL_A0 :
            self.CHANNEL_USED = self.CHANNEL_A0
            self.VMAX = VMAX_FOR_CHANNEL_A0[str(position)]
            self.startThreadForReadAdc()
            return
        if position in POSITION_FOR_CHANNEL_A1 :
            self.CHANNEL_USED = self.CHANNEL_A1
            self.VMAX = VMAX_FOR_CHANNEL_A1[str(position)]
            self.startThreadForReadAdc()
            return

    def readAdcValue(self):
        if(self.CHANNEL_USED==None):
            raise Exception("Erreur: CHANNEL_USED=None ")
        return self.adc.read_adc(self.CHANNEL_USED, gain=self.GAIN)
        
    def readAdcValueOfChannelAndSendMessage(self):
        start = time.time()
        seconds = 0
        while True:
            if (time.time()- start)> 1:
                adcValue=self.adc.read_adc(self.CHANNEL_USED, gain=self.GAIN)
                print("HARDWARE_ADC_VALUE_CHANNEL_A"+str(self.CHANNEL_USED))
                print("vMax=",self.VMAX," value=",adcValue," at t=",seconds)
                pub.sendMessage("HARDWARE_ADC_VALUE_CHANNEL_AX",adcInfo={'vMax':self.VMAX,'value':adcValue,'time':seconds})
                start = time.time()
                seconds+=1 
            self.stop_threads 
            if self.stop_threads : 
                break
            time.sleep(0.01)
    
    def startThreadForReadAdc(self):
        self.stopThreadForReadAdc()
        self.stop_threads  = False
        self.threadForReadAdc = threading.Thread(target = self.readAdcValueOfChannelAndSendMessage)
        self.threadForReadAdc.start() 
        print('thread start')

    def stopThreadForReadAdc(self): 
        self.stop_threads  = True
        if self.threadForReadAdc.is_alive():
            self.threadForReadAdc.join() 
            print('thread killed')  
