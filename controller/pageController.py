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

        pub.subscribe(self.__hardwareHandlerAdcValueOfChannelAX,"HARDWARE_ADC_VALUE_CHANNEL_AX")
        self.pageModel.goToPage(Page.HOME)

        pub.subscribe(self.handlerSurtension,"SURTENSION")

    def handlerSurtension(self,info):
        self.rootView.setLabelInfo("ATTENTION SURTENSION "+info)
    
    def goToNextPage(self,event):
        if self.pageModel.getPage() == Page.INSERT_USB :
            self.providerActionForFrame.getActionWhenQuit(self.convertPageToFrameName(self.pageModel.getPage()))
            if not self.rootView.getFrame().getUsb():
                return
        if self.pageModel.getPage() == Page.REAL_TIME_GRAPH:
            self.pageModel.goToPage(Page.INSERT_USB)
            return
        self.providerActionForFrame.getActionWhenQuit(self.convertPageToFrameName(self.pageModel.getPage()))
        self.pageModel.goToNextPage()

    def goToPreviousPage(self,event):
        self.providerActionForFrame.getActionWhenQuit(self.convertPageToFrameName(self.pageModel.getPage()))
        if self.pageModel.getPage() == Page.REAL_TIME_GRAPH:
            return
        self.pageModel.goToPreviousPage()

    def __pageChanged(self,page):
        frame = self.providerFrame.getFrame(self.convertPageToFrameName(page))
        frame = self.providerActionForFrame.getActionWhenGoTo(self.convertPageToFrameName(page),frame)
        self.rootView.setFrame(frame)
    
    def __hardwareHandler(self,broche):
        self.rootView.event_generate("<<"+self.convertBrocheToBrocheName(broche)+">>")
    
    def __hardwareHandlerAdcValueOfChannelAX(self,adcInfo):
        #if  in graphFrame set  adcInfo to view
        if self.pageModel.getPage() == Page.REAL_TIME_GRAPH:
            #read gain in hardware 4096->10 x->? beacuse in graphFrame i put vMax to 10
            value = (adcInfo['value']*adcInfo['vMax'])/32000
            #save adcInfo and set to graph
            ChromaAnalyse.getInstance().setAdcValue(value)
            ChromaAnalyse.getInstance().setTimeValue(adcInfo['time'])
            RootView.getInstance().getFrame().setData(ChromaAnalyse.getInstance().getAdcValue())
            RootView.getInstance().getFrame().setTime(ChromaAnalyse.getInstance().getTimeValue())
            RootView.getInstance().getFrame().setVMax(adcInfo['vMax'])
            print("receive analog data=",value," at t=",adcInfo['time'])

    def getView(self):
        return self.rootView

    #this func transform Page.VALUE to VALUE
    def convertPageToFrameName(self,page: PageModel):
        return str(page)[5:]

    #this func transform Broche.VALUE to VALUE
    def convertBrocheToBrocheName(self,broche: Broche):
        return str(broche)[7:]
