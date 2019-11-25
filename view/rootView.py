#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("tkinter")

from tkinter import Tk,Button

from .frame import HomeFrame

__all__ = ['RootView',]
#Singleton class
class RootView(Tk):

    __instance =None

    @staticmethod
    def getInstance():
        if RootView.__instance == None:
            RootView()
        return RootView.__instance

    def __init__(self):
        if RootView.__instance != None:
            raise Exception("Cette classe est un Singleton")
        else:
            RootView.__instance = self
            
        super(RootView,self).__init__()
        self.frame = HomeFrame(self)
        self.frame.pack(side="top", fill="both", expand = True) 
        #self.wm_attributes("-fullscreen",True)
        #button
        self.buttonOk = Button(self,text="Ok",command=self._generateEventOkButton)
        self.buttonOk.pack()
        self.buttonStop = Button(self,text="Stop",command=self._generateEventStopButton)
        self.buttonStop.pack()
    
    def _generateEventOkButton(self):
        self.event_generate('<<BUTTON_OK>>')

    def _generateEventStopButton(self):
        self.event_generate('<<BUTTON_STOP>>')


    def setFrame(self,frame):
        self.frame.pack_forget()
        self.frame.destroy()
        self.frame = frame
        self.frame.pack(side="top", fill="both", expand = True)