#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from utils.require import require
require("tkinter")
import matplotlib
matplotlib.use("TkAgg")

from tkinter import TOP,BOTH,StringVar,Label
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.animation as animation

from random import randint

from .rootFrame import RootFrame

__all__ = ['GraphFrame',]

class GraphFrame(RootFrame):
    TITLE_START="Chroma graph\n"+"Machine calibrée "
    def __init__(self,*args,**kw):
        super(GraphFrame,self).__init__(*args,**kw)
        self.canevas.pack_forget()
        self.data = []
        self.time = []

        self.vMax = 10
        self.duration = 600
        self.title= self.TITLE_START+"UNKNOW V"

        #msg 
        self.varMsg = StringVar()
        self.labelMsg = Label( self, textvariable=self.varMsg)
        self.labelMsg.configure(font=self.font,fg=self.colorGreen,bg="white")
        self.varMsg.set("")
        self.labelMsg.pack()

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.subPlot = self.figure.add_subplot(111)
        self.subPlot.set_title(self.getTitle())
        self.subPlot.set_xlabel("Temps (s)")
        self.subPlot.set_xlim(0, self.duration)
        self.subPlot.set_ylim(0, self.vMax)
        self.subPlot.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def setMsg(self,msg):
        self.varMsg.set(msg)
    def getFigure(self):
        return self.figure
    
    def getTitle(self):
        return self.title
    
    def setTitle(self,title):
        self.title = title

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
        self.time = time
    
    def setVMax(self,vMax):
        self.vMax = vMax
        self.setTitle(self.TITLE_START+str(self.vMax)+"V")
        self._updateSubPlot()

    def getVMax(self):
        return self.vMax
    
    def setDuration(self,duration):
        self.duration = duration*60 #convert in seconds
    
    def getDuration(self):
        return self.duration
    
    def saveImageOfGraphWithName(self,name="unknow"):
        self.figure.savefig(name, dpi=self.figure.dpi)
    
    def _updateSubPlot(self):
        #2. clear subplot
        self.subPlot.clear()

        #set value
        self.subPlot.set_title(self.getTitle())
        self.subPlot.set_xlabel("Temps (s)")
        self.subPlot.set_xlim(0, self.getDuration())
        self.subPlot.set_ylim(0, self.getVMax())
        self.subPlot.set_yticks([])
    
    def animate(self,i):
        import platform
        if platform.system() == 'Windows':
            #1. get data array values
            self.data.append(randint(0,8))
            self.time.append(i)

        self._updateSubPlot()

        #3. display subplot (adcValue,timeWhentheAdcValueIsRead)
        self.subPlot.plot(self.time,self.data)

    def startAnimation(self):
        return animation.FuncAnimation(self.figure,self.animate, interval=1000)