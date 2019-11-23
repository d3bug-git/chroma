#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("pypubsub")
from pubsub import pub

from .enumPage import Page

__all__= ['PageModel',]

class PageModel:
    def __init__(self):
        self.page = Page.HOME

    def __setPage(self, page):
        self.page = page
        pub.sendMessage("PAGE_CHANGED",page= page)

    def goToHomePage(self):
        self.__setPage(Page.HOME)

    def goToUSBPage(self):
        self.__setPage(Page.INSERT_USB)
    
    def goToConfigTimePage(self):
        self.__setPage(Page.CONFIG_TIME)
    
    def goToConfirmAnalysePage(self):
        self.__setPage(Page.CONFIRM_ANALYSE)
    
    def goToGraphPage(self):
        self.__setPage(Page.REAL_TIME_GRAPH)