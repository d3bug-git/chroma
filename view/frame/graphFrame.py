#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

from tkinter import TOP, BOTH, StringVar, Label
from .rootFrame import RootFrame
from random import randint
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib
from utils.require import require
require("tkinter")
matplotlib.use("TkAgg")


__all__ = ['GraphFrame', ]


class GraphFrame(RootFrame):
    TITLE_START = "Graphique\n"+"Machine calibrée à "

    def __init__(self, *args, **kw):
        super(GraphFrame, self).__init__(*args, **kw)
        self.canevas.pack_forget()
        self.data = []
        self.time = []

        self.vMax = 10
        self.duration = 600
        self.title = self.TITLE_START+"UNKNOW V"

        # msg
        self.varMsg = StringVar()
        self.labelMsg = Label(self, textvariable=self.varMsg)
        self.labelMsg.configure(font=self.font, fg=self.colorGreen, bg="white")
        self.varMsg.set("")
        self.labelMsg.pack()

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.subPlot = self.figure.add_subplot(
            111, xlim=[0, self.getDuration()], ylim=[0, self.getVMax()])

        self._updateSubPlot()

        # A tk.DrawingArea.
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def setMsg(self, msg):
        self.varMsg.set(msg)

    def getFigure(self):
        return self.figure

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getSubPlot(self):
        return self.subPlot

    def setData(self, data):
        self.data = data

    def setTime(self, time):
        self.time = time

    def setVMax(self, vMax):
        self.vMax = round(float(vMax), 2)
        self.setTitle(self.TITLE_START+str(self.vMax)+"V")
        self._updateSubPlot()

    def getVMax(self):
        return self.vMax

    def setDuration(self, duration):
        self.duration = int(duration*60)  # convert in seconds

    def getDuration(self):
        return self.duration

    def _updateSubPlot(self):
        #  clear subplot
        self.subPlot.clear()

        # set value
        self.subPlot.set_title(self.getTitle())
        self.subPlot.set_xlabel("Temps [s]")
        self.subPlot.set_xlim([0, self.getDuration()])
        self.subPlot.set_ylim([0, self.getVMax()])
        self.subPlot.set_yticks([])

    def animate(self, i):
        import platform
        if platform.system() == 'Windows':
            # 1. get data array values
            self.data.append(randint(0, 8))
            self.time.append(i)

        self._updateSubPlot()

        # 3. display 
        print("length time=",len(self.time),"length data=",len(self.data))
        
        self.subPlot.plot(self.time, self.data)
        

    def startAnimation(self):
        return animation.FuncAnimation(self.figure, self.animate,interval=1000)
