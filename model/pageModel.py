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
        
    def getPage(self):
        return  self.page
    
    def goToNextPage(self):
        page = self.page.getPage(self.page.value+1)
        self.__setPage(page)
    
    def goToPreviousPage(self):
        page = self.page.getPage(self.page.value-1)
        self.__setPage(page)