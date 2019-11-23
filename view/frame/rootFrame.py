#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Frame,Label,StringVar,RAISED

__all__ = ['RootFrame',]

class RootFrame(Frame):
    #Appel du constructeur parent
    def __init__(self,root):
        super(RootFrame, self).__init__(root)
        var = StringVar()
        self.label =Label(self,textvariable=var,relief=RAISED)
        var.set("Welcome to Chroma project!")
        self.label.pack()