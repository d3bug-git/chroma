#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("tkinter")

from tkinter import Tk,Button,PanedWindow

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

    def __init__(self,**kw):
        if RootView.__instance != None:
            raise Exception("Cette classe est un Singleton")
        else:
            RootView.__instance = self
            
        super(RootView,self).__init__(**kw)
        self.title("Chroma V0.1")
        self.frame = HomeFrame(self)
        self.frame.pack(side="top", fill="both", expand = True) 
        #self.wm_attributes("-fullscreen",True)
         
        #button
        self.panedWindow = PanedWindow()
        self.panedWindow.pack(side="bottom")
        self.buttonStop = Button(self.panedWindow,text="Stop",command=self._generateEventStopButton)
        self.panedWindow.add(self.buttonStop)
        self.buttonOk = Button(self.panedWindow,text="Ok",command=self._generateEventOkButton)
        self.panedWindow.add(self.buttonOk)
    
    def _generateEventOkButton(self):
        self.event_generate('<<BUTTON_OK>>')

    def _generateEventStopButton(self):
        self.event_generate('<<BUTTON_STOP>>')

    def setFrame(self,frame):
        self.frame.pack_forget()
        self.frame.destroy()
        self.frame = frame
        self.frame.pack(side="top", fill="both", expand = True)