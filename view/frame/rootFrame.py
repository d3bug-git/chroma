#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
from tkinter import Frame,Canvas
from PIL import Image, ImageTk
__all__ = ['RootFrame',]

class RootFrame(Frame):
    #Appel du constructeur parent
    def __init__(self,root, *args, **kw):
        super(RootFrame, self).__init__(root, *args, **kw)
        self.root = root
        self.configure(background="white")
        
        #image de fond
        photo =  ImageTk.PhotoImage(Image.open("yiec_min.jpg"))
        self.photo = photo

        #Canevas
        self.canevas_width = 478
        self.canevas_height = 456
        self.canevas = Canvas(self,width=self.canevas_width,height=self.canevas_height,bg="white")
        self.canevas.pack()
        