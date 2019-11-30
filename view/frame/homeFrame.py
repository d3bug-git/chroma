#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter","PIL")
from tkinter import Label,Canvas,CENTER,RAISED

from .rootFrame import RootFrame

__all__ = ['HomeFrame',]

class HomeFrame(RootFrame):
    def __init__(self,root,*args,**kw):
        super(HomeFrame,self).__init__(root,*args,**kw)

        #image de fond
        self.canevas.create_image(self.canevas_width/2,self.canevas_height/2,anchor=CENTER,image=self.photo)

        #label
        font = ('tahoma', 20, 'bold')
        textColor = '#e6482d'
            #commencer
        self.labelCommencer =Label(self,text="Commencer",relief=RAISED)
        self.labelCommencer.configure(font=font,fg=textColor,bg="white")
        self.labelCommencer.pack(side="bottom")
            #enregistreur
        self.labelEnregistreur =Label(self,text="Bienvenue dans \nL'enregistreur de données")
        self.labelEnregistreur.configure(font=font,fg='#0e1a28',bg="white")
        self.labelEnregistreur.pack(side="bottom")
