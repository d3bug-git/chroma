#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("tkinter")
from tkinter import Tk

from frame.rootFrame import RootFrame

__all__ = ['RootView',]

class RootView(Tk):
    def __init__(self):
        super(RootView,self).__init__()
        self.frame = RootFrame(self)
        self.frame.pack()

    def setFrame(self,frame):
        self.frame = frame
        self.frame.pack()


if __name__ == "__main__":
    r = RootView()
    r.mainloop()