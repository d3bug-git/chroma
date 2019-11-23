#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Label,StringVar,RAISED

from .rootFrame import RootFrame

__all__ = ['ConfirmAnalyseFrame',]

class ConfirmAnalyseFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(ConfirmAnalyseFrame,self).__init__(*args,**kw)
        self.configure(background="yellow")
        var = StringVar()
        self.label =Label(self,textvariable=var,relief=RAISED)
        var.set("confirmAnalyseFrame")
        self.label.pack()