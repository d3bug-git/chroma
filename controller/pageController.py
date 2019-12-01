#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from  utils.require import require
require("pypubsub")

from pubsub import pub
from model import Page,PageModel,ChromaAnalyse
from view import RootView,ProviderFrame
from .providerActionForFrame import ProviderActionForFrame
from hardware import Broche

__all__ = ['PageController','convertPageToFrameName','convertBrocheToBrocheName']

class PageController:
    def __init__(self, pageModel:PageModel, rootView:RootView, providerFrame:ProviderFrame):
        self.pageModel = pageModel
        self.rootView = rootView 
        self.providerFrame = providerFrame
        self.chromaAnalyse = ChromaAnalyse.getInstance()
        self.providerActionForFrame = ProviderActionForFrame(self.chromaAnalyse)

        self.rootView.bind("<<"+convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",self.goToNextPage)
        self.rootView.bind("<<"+convertBrocheToBrocheName(Broche.BUTTON_STOP)+">>",self.goToPreviousPage)

        pub.subscribe(self.__pageChanged,"PAGE_CHANGED")
        pub.subscribe(self.__hardwareHandler,"HARDWARE_EVENT")
        
    def goToNextPage(self,event):
        self.providerActionForFrame.getActionWhenQuit(convertPageToFrameName(self.pageModel.getPage()))
        self.pageModel.goToNextPage()

    def goToPreviousPage(self,event):
        self.pageModel.goToPreviousPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(convertPageToFrameName(page))
        frame = self.providerActionForFrame.getActionWhenGoTo(convertPageToFrameName(page),frame)
        self.rootView.setFrame(frame)
    
    def __hardwareHandler(self,broche):
        self.rootView.event_generate("<<"+convertBrocheToBrocheName(broche)+">>")

    def getView(self):
        return self.rootView

#this func transform Page.VALUE to VALUE
def convertPageToFrameName(page: PageModel):
    return str(page)[5:]

#this func transform Broche.VALUE to VALUE
def convertBrocheToBrocheName(broche: Broche):
    return str(broche)[7:]
