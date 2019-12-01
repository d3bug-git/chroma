#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Label,RAISED,Spinbox,CENTER,Button

from .rootFrame import RootFrame

__all__ = ['ConfigTimeFrame',]

class ConfigTimeFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(ConfigTimeFrame,self).__init__(*args,**kw)
       
        #image de fond
        self.canevas.create_image(self.canevas_width/2,self.canevas_height/2,anchor=CENTER,image=self.photo)

        #label suivant
        self.labelSuivant =Label(self,text="Suivant",relief=RAISED)
        self.labelSuivant.configure(font=self.font,fg=self.colorOrange,bg="white")
        
        
        #time spinbox
        self.spinboxTime = Spinbox(self,from_=10, to=120,increment=10)
        self.spinboxTime.focus()
        self.spinboxTime.configure(font=self.font,fg=self.colorBlue,bg="white")
        

        #config time
        self.labelConfigTime =Label(self,text="Entrer la durée de l'analyse en minute")
        self.labelConfigTime.configure(font=self.font,fg=self.colorBlue,bg="white")

        #display
        self.labelConfigTime.pack(side="top")
        self.spinboxTime.pack(side="top")
        self.labelSuivant.pack(side="top")
    
    def getTimeConfigured(self):
        return int(self.spinboxTime.get())

    #this method is call by provider action
    def incrementTimeConfigured(self,event):
        self.spinboxTime.invoke('buttonup')
        
    #this method is call by provider action
    def decrementTimeConfigured(self,event):
        self.spinboxTime.invoke('buttondown')
