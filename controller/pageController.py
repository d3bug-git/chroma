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
    def __init__(self, pageModel, rootView, providerFrame):
        self.pageModel = pageModel
        self.rootView = rootView
        self.providerFrame = providerFrame
        pub.subscribe(self.__pageChanged,"PAGE_CHANGED")
    
    def goToHome(self):
        self.pageModel.goToHomePage()
    
    def goToUSBPage(self):
        self.pageModel.goToUSBPage()
    
    def goToConfigTimePage(self):
        self.pageModel.goToConfigTimePage()
    
    def goToConfirmAnalysePage(self):
        self.pageModel.goToConfirmAnalysePage()
    
    def goToRealTimeGraph(self):
        self.pageModel.goToGraphPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(self.convertPageToFrameName(page))
        self.rootView.setFrame(frame)

    """this func transform Page.VALUE to VALUE """
    def convertPageToFrameName(self,page: PageModel): 
        return str(page)[5:]

    def getView(self):
        return self.rootView
