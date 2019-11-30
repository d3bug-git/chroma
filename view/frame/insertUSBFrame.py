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
        font = ('tahoma', 20, 'bold')
        textColor = '#e6482d'
            #commencer
        self.labelCommencer =Label(self,text="Suivant",relief=RAISED)
        self.labelCommencer.configure(font=font,fg=textColor,bg="white")
        self.labelCommencer.pack(side="bottom")
            #enregistreur
        self.labelEnregistreur =Label(self,text="Insérer une clé USB\npour stocker le résultat de l'analyse")
        self.labelEnregistreur.configure(font=font,fg='#0e1a28',bg="white")
        self.labelEnregistreur.pack(side="bottom")