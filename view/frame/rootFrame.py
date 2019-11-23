#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Frame

__all__ = ['RootFrame',]

class RootFrame(Frame):
    #Appel du constructeur parent
    def __init__(self,root, *args, **kw):
        super(RootFrame, self).__init__(root, *args, **kw)