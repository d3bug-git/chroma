#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from  utils.require import require
require("pypubsub")

from pubsub import pub
from model import Page,PageModel
from view import RootView,ProviderFrame

__all__ = ['PageController',]

class PageController:
    def __init__(self, pageModel:PageModel, rootView:RootView, providerFrame:ProviderFrame):
        self.pageModel = pageModel
        self.rootView = rootView 
        self.providerFrame = providerFrame
        
        self.rootView.bind('<<BUTTON_OK>>',self.goToNextPage)
        self.rootView.bind('<<BUTTON_STOP>>',self.goToPreviousPage)

        pub.subscribe(self.__pageChanged,"PAGE_CHANGED")

    def goToNextPage(self,event):
        self.pageModel.goToNextPage()

    def goToPreviousPage(self,event):
        self.pageModel.goToPreviousPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(self.convertPageToFrameName(page))
        self.rootView.setFrame(frame)

    """this func transform Page.VALUE to VALUE """
    def convertPageToFrameName(self,page: PageModel): 
        return str(page)[5:]

    def getView(self):
        return self.rootView
