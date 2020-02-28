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
        
        pub.subscribe(self.setDurationAnalyse,"DURATION_OF_ANALYSE")
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
        self.CHANNEL_A0 =0 #5v
        self.CHANNEL_A1 =1  #10v
        self.CHANNEL_A2 = 2 #surtension 5v
        self.CHANNEL_A3 = 3 #surtension 10V
        self.CHANNEL_USED = None
        self.VMAX = None
        self.threadForReadAdc = threading.Thread(target = self.readAdcValueOfChannelAndSendMessage) 
        self.threadForGetStateOfPin = threading.Thread(target= self.getStateOfPin)
        self.duration = 0

        GPIO.setmode(GPIO.BCM)
        #Button Ok
        GPIO.setup(Broche.BUTTON_OK.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_OK.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)
        
        #Button Stop
        GPIO.setup(Broche.BUTTON_STOP.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #Button Plus
        GPIO.setup(Broche.BUTTON_PLUS.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_PLUS.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)

        #Button moins
        GPIO.setup(Broche.BUTTON_MOINS.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(Broche.BUTTON_MOINS.value,GPIO.RISING,callback=self.onClickButton,bouncetime=500)
        
        #machine 
        #GPIO.setup(Broche.RELAY_MACHINE.value,GPIO.OUT,initial=GPIO.LOW)

        #switch machine_1
        GPIO.setup(Broche.SWITCH_MACHINE_1.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #switch machine_2
        GPIO.setup(Broche.SWITCH_MACHINE_2.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #selector in position machine_1
        GPIO.setup(Broche.SELECTOR_POSITION_MACHINE_1.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #selector in position machine_2
        GPIO.setup(Broche.SELECTOR_POSITION_MACHINE_2.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #selector Vmax
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_05.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_1.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_2.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_5.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Broche.SELECTOR_VMAX_IN_POSITION_10.value,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#********************************************** SHUTDOWN **********************************************
        GPIO.add_event_detect(Broche.BUTTON_STOP, GPIO.BOTH, callback=self.handleButtonStop, bouncetime=200)
    DURATION_OF_PRESS = 3
    def handleButtonStop(self):
        global start
        global end
        if GPIO.input(Broche.BUTTON_STOP) == GPIO.HIGH:
            start = time.time()
        if GPIO.input(Broche.BUTTON_STOP) == GPIO.LOW:
            end = time.time()
            elapsed = end - start
            print(elapsed)
            if elapsed >= self.DURATION_OF_PRESS :
                import os
                os.system("shutdown now -h")
            else:
                self.onClickButton(Broche.BUTTON_STOP.value)


#********************************************** SELECTOR **********************************************

    def activateSelectorVmax(self):
        #selector in position 0->0.5V
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_05.value,GPIO.RISING,callback=self.onTurnSelectorVmax,bouncetime=500)
        #selector in position 0->1V
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_1.value,GPIO.RISING,callback=self.onTurnSelectorVmax,bouncetime=500)
        #selector in position 0->2V
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_2.value,GPIO.RISING,callback=self.onTurnSelectorVmax,bouncetime=500)
        #selector in position 0->5V
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_5.value,GPIO.RISING,callback=self.onTurnSelectorVmax,bouncetime=500)
        #selector in position 0->10V
        GPIO.add_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_10.value,GPIO.RISING,callback=self.onTurnSelectorVmax,bouncetime=500)
        print("activate selector Vmax")

    
    def deactivateSelectorVmax(self):
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_05.value)
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_1.value)
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_2.value)
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_5.value)
        GPIO.remove_event_detect(Broche.SELECTOR_VMAX_IN_POSITION_10.value)
        print("deactivate selector Vmax")

    def activeSwitchMachine(self):
        GPIO.add_event_detect(Broche.SWITCH_MACHINE_1.value,GPIO.RISING,callback=self.detectSwitchMachine,bouncetime=500)
        GPIO.add_event_detect(Broche.SWITCH_MACHINE_2.value,GPIO.RISING,callback=self.detectSwitchMachine,bouncetime=500)
    
    def deactiveSwitchMachine(self):
        GPIO.remove_event_detect(Broche.SWITCH_MACHINE_1.value)
        GPIO.remove_event_detect(Broche.SWITCH_MACHINE_2.value)
    
    def detectSwitchMachine(self,switch_machine):
        if GPIO.input(Broche.SELECTOR_POSITION_MACHINE_1) and switch_machine == Broche.SWITCH_MACHINE_1.value:
            self.sendHardwareEvent(Broche.getBroche(Broche.BUTTON_OK.value))
            return
        self.sendHardwareEvent(Broche.getBroche(Broche.BUTTON_OK.value))

    def activateSelectorMachine(self):
        GPIO.add_event_detect(Broche.SELECTOR_POSITION_MACHINE_2.value,GPIO.RISING,callback=self.onTurnSelectorMachine,bouncetime=500)
        GPIO.add_event_detect(Broche.SELECTOR_POSITION_MACHINE_1.value,GPIO.RISING,callback=self.onTurnSelectorMachine,bouncetime=500)
        print("activate selector Machine")

    def deactivateSelectorMachine(self):
        GPIO.remove_event_detect(Broche.SELECTOR_POSITION_MACHINE_1.value)
        GPIO.remove_event_detect(Broche.SELECTOR_POSITION_MACHINE_2.value)
        print("deactivate selector Machine")

#********************************************** END SELECTOR *******************************************
    def setDurationAnalyse(self,duration):
        self.duration = duration*60 #convert in seconds
    
    def getDurationOfAnalyse(self):
        return self.duration
    def sendHardwareEvent(self,broche):
        pub.sendMessage("HARDWARE_EVENT",broche = broche)
    
    def getVMax(self):
        return self.VMAX
        
    def onClickButton(self,button):
        self.sendHardwareEvent(Broche.getBroche(button))

    #think to do some thread who read all the 1s and send message
    def onTurnSelectorVmax(self,position):
        if position in POSITION_FOR_CHANNEL_A0 :
            self.CHANNEL_USED = self.CHANNEL_A0
            self.VMAX = VMAX_FOR_CHANNEL_A0[str(position)]    
            return
        if position in POSITION_FOR_CHANNEL_A1 :
            self.CHANNEL_USED = self.CHANNEL_A1
            self.VMAX = VMAX_FOR_CHANNEL_A1[str(position)]
            return
    
    def onTurnSelectorMachine(self,machine):
        if machine == Broche.SELECTOR_POSITION_MACHINE_1.value:
            GPIO.output(Broche.RELAY_MACHINE.value, GPIO.LOW)
            print("machine 1 sélectionnée")
            return
        GPIO.output(Broche.RELAY_MACHINE.value, GPIO.HIGH)
        print("machine 2 sélectionnée")

    def readAdcValue(self):
        if(self.CHANNEL_USED==None):
            raise Exception("Erreur: CHANNEL_USED=None ")
        return self.adc.read_adc(self.CHANNEL_USED, gain=self.GAIN)
        
    def readAdcValueOfChannelAndSendMessage(self):
        start = time.time()
        seconds = 0
        while True and seconds < self.duration:
            if (time.time()- start)> 1:
                adcValue=self.adc.read_adc(self.CHANNEL_USED, gain=self.GAIN)
                #lecture pour surtension
                adcSurtension5V = self.adc.read_adc(self.CHANNEL_A2, gain=self.GAIN)
                adcSurtension10V = self.adc.read_adc(self.CHANNEL_A3, gain=self.GAIN)
                if adcSurtension5V >=5000:
                    pub.sendMessage("SURTENSION",info="5V")
                    break
                elif adcSurtension10V >=5000:
                    pub.sendMessage("SURTENSION",info="10V")
                    break
                print("HARDWARE_ADC_VALUE_CHANNEL_A"+str(self.CHANNEL_USED))
                print("vMax=",self.VMAX," value=",adcValue," at t=",seconds)
                pub.sendMessage("HARDWARE_ADC_VALUE_CHANNEL_AX",adcInfo={'vMax':self.VMAX,'value':adcValue,'time':seconds})
                start = time.time()
                seconds+=1 
            if self.stop_threads :
                break
            time.sleep(0.01)

    def getStateOfPin(self):
        while True:
            if GPIO.HIGH == GPIO.input(Broche.SELECTOR_POSITION_MACHINE_1.value):
                GPIO.output(Broche.RELAY_MACHINE.value, GPIO.LOW)
            if GPIO.HIGH == GPIO.input(Broche.SELECTOR_POSITION_MACHINE_2.value):
                GPIO.output(Broche.RELAY_MACHINE.value, GPIO.HIGH)

            for position in POSITION_FOR_CHANNEL_A0:
                if position == GPIO.HIGH:
                    self.onTurnSelectorVmax(position)
                    print("Selector ",self.VMAX,"V")
            if Broche.SELECTOR_VMAX_IN_POSITION_10.value ==GPIO.HIGH:
                self.onTurnSelectorVmax(Broche.SELECTOR_VMAX_IN_POSITION_10.value)
                print("Selector ",self.VMAX,"V")
            if self.stop_thread_getStateOfPin:
                break
            time.sleep(0.02)

    def startThreadGetStateOfPin(self):
        self.stopThreadGetStateOfPin()
        self.stop_thread_getStateOfPin = False
        self.threadForGetStateOfPin = threading.Thread(target= self.getStateOfPin)
        self.threadForGetStateOfPin.start()
        print("Thread get state of pin start")

    def stopThreadGetStateOfPin(self):
        self.stop_thread_getStateOfPin = True
        if self.threadForGetStateOfPin.is_alive():
            self.threadForGetStateOfPin.join()
            print("Thread get state of pin killed")

    
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
