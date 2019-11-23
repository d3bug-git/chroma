#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Label,StringVar,RAISED

from .rootFrame import RootFrame

__all__ = ['HomeFrame',]

class HomeFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(HomeFrame,self).__init__(*args,**kw)
        self.configure(background="green")
        var = StringVar()
        self.label =Label(self,textvariable=var,relief=RAISED)
        var.set("HomeFrame")
        self.label.pack()