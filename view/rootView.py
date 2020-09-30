#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from tkinter import Tk, Button, PanedWindow, StringVar, Label
from .frame import HomeFrame
from utils.require import require
require("tkinter")


__all__ = ['RootView', ]
# Singleton class


class RootView(Tk):

    __instance = None

    @staticmethod
    def getInstance():
        if RootView.__instance == None:
            RootView()
        return RootView.__instance

    def __init__(self, **kw):
        if RootView.__instance != None:
            raise Exception("Cette classe est un Singleton")
        else:
            RootView.__instance = self

        super(RootView, self).__init__(**kw)
        self.configure(bg="white")
        self.title("Chroma V0.1")
        self.frame = HomeFrame(self)
        self.frame.pack(side="top", fill="both", expand=True)
        # msg
        self.varInfo = StringVar()
        self.labelInfo = Label(self, textvariable=self.varInfo)
        self.labelInfo.configure(
            font=('tahoma', 20, 'bold'), fg="#ff0000", bg="white")
        self.varInfo.set("")
        self.labelInfo.pack(side="top")
        self.isFullScreen = False
        self.isShowDebugPanel = False

    def _generateEventOkButton(self):
        self.event_generate('<<BUTTON_OK>>')

    def _generateEventStopButton(self):
        self.event_generate('<<BUTTON_STOP>>')

    def toggleIsShowDebugPanel(self):
        self.isShowDebugPanel = not(self.isShowDebugPanel)

    def toggleShowDebugPanel(self):
        if not(self.isShowDebugPanel):
            self.panedWindow = PanedWindow()
            self.panedWindow.pack(side="bottom")
            self.buttonStop = Button(
                self.panedWindow, text="Stop", command=self._generateEventStopButton)
            self.panedWindow.add(self.buttonStop)
            self.buttonOk = Button(self.panedWindow, text="Ok",
                                   command=self._generateEventOkButton)
            self.panedWindow.add(self.buttonOk)
            buttonPlus = Button(self.panedWindow, text="Plus",
                                command=lambda: self.event_generate('<<BUTTON_PLUS>>'))
            self.panedWindow.add(buttonPlus)
            buttonMoins = Button(self.panedWindow, text="Moins",
                                 command=lambda: self.event_generate('<<BUTTON_MOINS>>'))
            self.panedWindow.add(buttonMoins)
            buttonFullScreen = Button(self.panedWindow, text="toggle fullscreen",
                                      command=lambda: self.toggleFullScreen())
            self.panedWindow.add(buttonFullScreen)
        else:
            self.panedWindow.pack_forget()
        self.toggleIsShowDebugPanel()

    def toggleFullScreen(self):
        self.isFullScreen = not(self.isFullScreen)
        self.wm_attributes("-fullscreen", not(self.isFullScreen))

    def setFrame(self, frame):
        self.frame.pack_forget()
        self.frame.destroy()
        self.frame = frame
        self.frame.pack(side="top", fill="both", expand=True)

    def getFrame(self):
        return self.frame

    def setLabelInfo(self, info):
        self.varInfo.set(info)
