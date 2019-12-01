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
            #suivant
        self.labelSuivant =Label(self,text="Suivant",relief=RAISED)
        self.labelSuivant.configure(font=self.font,fg=self.colorOrange,bg="white")
        self.labelSuivant.pack(side="top")
            #insert USB
        self.labelInsertUsb =Label(self,text="Insérer une clé USB\npour stocker le résultat de l'analyse")
        self.labelInsertUsb.configure(font=self.font,fg=self.colorBlue,bg="white")
        self.labelInsertUsb.pack(side="top")