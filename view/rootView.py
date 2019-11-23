#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("tkinter")

from tkinter import Tk

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

    def setFrame(self,frame):
        self.frame.pack_forget()
        self.frame = frame
        self.frame.pack(side="top", fill="both", expand = True)