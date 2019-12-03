#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
import matplotlib
matplotlib.use("TkAgg")

from tkinter import TOP,BOTH
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.animation as animation

from random import randint

from .rootFrame import RootFrame

__all__ = ['GraphFrame',]

class GraphFrame(RootFrame):
    def __init__(self,*args,**kw):
        super(GraphFrame,self).__init__(*args,**kw)
        self.canevas.pack_forget()

        self.title = "Chroma graph"
        self.data = []

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.subPlot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    
    def getFigure(self):
        return self.figure

    def getSubPlot(self):
        return self.subPlot

    def setFigure(self,figure:Figure):
        self.canvas.get_tk_widget().pack_forget()
        self.canvas.get_tk_widget().destroy()

        self.figure = figure
        self.subPlot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    
    def setData(self,data):
        self.data = data
    
    def animate(self,i):
        #1. get data array values
        self.data =range(1,randint(1,20),1)

        #2. clear subplot
        self.subPlot.clear()
        self.subPlot.set_title(self.title)

        #3. display subplot
        self.subPlot.plot(self.data,self.data)

    def startAnimation(self):
        return animation.FuncAnimation(self.figure,self.animate, interval=1000)