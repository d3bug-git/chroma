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

__all__ = ['PageController',]

class PageController:
    def __init__(self, pageModel:PageModel, rootView:RootView, providerFrame:ProviderFrame):
        self.pageModel = pageModel
        self.rootView = rootView 
        self.providerFrame = providerFrame
        self.providerActionForFrame = ProviderActionForFrame()
        self.providerActionForFrame.setController(self)

        self.rootView.bind("<<"+self.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",self.goToNextPage)
        self.rootView.bind("<<"+self.convertBrocheToBrocheName(Broche.BUTTON_STOP)+">>",self.goToPreviousPage)

        pub.subscribe(self.__pageChanged,"PAGE_CHANGED")
        pub.subscribe(self.__hardwareHandler,"HARDWARE_EVENT")

        pub.subscribe(self.__hardwareHandlerAdcValueOfChannelA0,"HARDWARE_ADC_VALUE_CHANNEL_A0")
        pub.subscribe(self.__hardwareHandlerAdcValueOfChannelA1,"HARDWARE_ADC_VALUE_CHANNEL_A1")
        
    def goToNextPage(self,event):
        self.providerActionForFrame.getActionWhenQuit(self.convertPageToFrameName(self.pageModel.getPage()))
        self.pageModel.goToNextPage()

    def goToPreviousPage(self,event):
        self.pageModel.goToPreviousPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(self.convertPageToFrameName(page))
        frame = self.providerActionForFrame.getActionWhenGoTo(self.convertPageToFrameName(page),frame)
        self.rootView.setFrame(frame)
    
    def __hardwareHandler(self,broche):
        self.rootView.event_generate("<<"+self.convertBrocheToBrocheName(broche)+">>")
    
    def __hardwareHandlerAdcValueOfChannelA0(self,adcValue):
        #if  in graphFrame set  adcValue to view
        if self.pageModel == Page.REAL_TIME_GRAPH:
            #save adcValue and set to graph
            ChromaAnalyse.getInstance().setAdcValue(adcValue['value'])
            RootView.getInstance().getFrame().setData(ChromaAnalyse.getInstance().getAdcValue())
            RootView.getInstance().getFrame().setTime(adcValue['time'])
            pass 
        pass
    
    def __hardwareHandlerAdcValueOfChannelA1(self,adcValue):
        #if  in graphFrame set  adcValue to view 
        pass

    def getView(self):
        return self.rootView

    #this func transform Page.VALUE to VALUE
    def convertPageToFrameName(self,page: PageModel):
        return str(page)[5:]

    #this func transform Broche.VALUE to VALUE
    def convertBrocheToBrocheName(self,broche: Broche):
        return str(broche)[7:]
