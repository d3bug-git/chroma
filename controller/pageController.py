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

__all__ = ['PageController',]

class PageController:
    def __init__(self, pageModel:PageModel, rootView:RootView, providerFrame:ProviderFrame):
        self.pageModel = pageModel
        self.rootView = rootView 
        self.providerFrame = providerFrame
        self.chromaAnalyse = ChromaAnalyse.getInstance()
        self.providerActionForFrame = ProviderActionForFrame(self.chromaAnalyse)

        self.rootView.bind('<<BUTTON_OK>>',self.goToNextPage)
        self.rootView.bind('<<BUTTON_STOP>>',self.goToPreviousPage)

        pub.subscribe(self.__pageChanged,"PAGE_CHANGED")
        pub.subscribe(self.__hardwareHandler,"HARDWARE_EVENT")
        
    def goToNextPage(self,event):
        self.providerActionForFrame.getActionWhenQuit(self.convertPageToFrameName(self.pageModel.getPage()))
        self.pageModel.goToNextPage()

    def goToPreviousPage(self,event):
        self.pageModel.goToPreviousPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(self.convertPageToFrameName(page))
        frame = self.providerActionForFrame.getActionWhenGoTo(self.convertPageToFrameName(page),frame)
        self.rootView.setFrame(frame)
    
    def __hardwareHandler(self,button):
        self.goToNextPage(button)

    """this func transform Page.VALUE to VALUE """
    def convertPageToFrameName(self,page: PageModel):
        return str(page)[5:]

    def getView(self):
        return self.rootView
