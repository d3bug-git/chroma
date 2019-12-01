#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Label,RAISED,CENTER,StringVar

from .rootFrame import RootFrame

__all__ = ['ConfirmAnalyseFrame',]

class ConfirmAnalyseFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(ConfirmAnalyseFrame,self).__init__(*args,**kw)
        self.duration = '0'
        #image de fond
        self.canevas.create_image(self.canevas_width/2,self.canevas_height/2,anchor=CENTER,image=self.photo)

        #label config time
        self.textConfigTime = StringVar()
        self.textConfigTime.set("L'analyse est configurer pour durer "+self.duration+" minutes\nAppuyez sur le bouton OK pour lancer l'analyse")
        self.labelConfigTime =Label(self,textvariable=self.textConfigTime)
        self.labelConfigTime.configure(font=self.font,fg=self.colorBlue,bg="white")

        #label confirm
        self.labelConfirm =Label(self,text="Confirmer",relief=RAISED)
        self.labelConfirm.configure(font=self.font,fg=self.colorOrange,bg="white")

        #display
        self.labelConfigTime.pack(side="top")
        self.labelConfirm.pack(side="top")
    
    def setDuration(self,duration):
        self.duration = str(duration)
        self.textConfigTime.set("L'analyse est configurer pour durer "+self.duration+" minutes\nAppuyez sur le bouton OK pour lancer l'analyse\nStop pour modifier la durée")