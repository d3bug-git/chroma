#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Label,StringVar,RAISED,NW

from .rootFrame import RootFrame

__all__ = ['InsertUSBFrame',]

class InsertUSBFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(InsertUSBFrame,self).__init__(*args,**kw)

        #image de fond
        self.canevas.create_image(0,0,anchor=NW,image=self.photo)

        #label
            #msg erreur usb
        self.varMsg = StringVar()
        self.labelMsg = Label( self, textvariable=self.varMsg)
        self.labelMsg.configure(font=self.font,fg=self.colorRed,bg="white")
        self.varMsg.set("")
        self.usb=False
        self.labelMsg.pack()
            #suivant
        self.labelSuivant =Label(self,text="Suivant",relief=RAISED)
        self.labelSuivant.configure(font=self.font,fg=self.colorOrange,bg="white")
        self.labelSuivant.pack(side="top")
            #insert USB
        self.labelInsertUsb =Label(self,text="Insérer une clef USB\npour stocker le résultat de l'analyse.")
        self.labelInsertUsb.configure(font=self.font,fg=self.colorBlue,bg="white")
        self.labelInsertUsb.pack(side="top")

    def setMsg(self,msg):
        self.varMsg.set(msg)

    def setUsb(self,usb):
        self.usb = usb

    def getUsb(self):
        return self.usb