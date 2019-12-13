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
        self.time = []

        self.vMax = 10
        self.duration = 600

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.subPlot = self.figure.add_subplot(111)
        self.subPlot.set_title(self.title)
        self.subPlot.set_xlabel("Temps (s)")
        self.subPlot.set_ylabel("Machine calibré à "+str(self.vMax))
        self.subPlot.set_xlim(0, self.duration)
        self.subPlot.set_ylim(0, self.vMax)

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
    
    def setTime(self,time):
        self.time.append(time)
    
    def setVMax(self,vMax):
        self.vMax = vMax

    def getVMax(self):
        return self.vMax
    
    def setDuration(self,duration):
        self.duration = duration*60 #convert in seconds
    
    def getDuration(self):
        return self.duration
    
    def animate(self,i):
        import platform
        if platform.system() == 'Windows':
            #1. get data array values
            self.data.append(randint(0,8))
            self.time.append(i)

        #2. clear subplot
        self.subPlot.clear()

        #set value
        self.subPlot.set_title(self.title)
        self.subPlot.set_xlabel("Temps (s)")
        self.subPlot.set_ylabel("Machine calibré à "+str(self.vMax))
        self.subPlot.set_xlim(0, self.duration)
        self.subPlot.set_ylim(0, self.vMax)

        #3. display subplot (adcValue,timeWhentheAdcValueIsRead)
        self.subPlot.plot(self.time,self.data)

    def startAnimation(self):
        return animation.FuncAnimation(self.figure,self.animate, interval=1000)