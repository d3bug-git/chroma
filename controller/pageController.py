#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from  utils.require import require
require("pypubsub")

from pubsub import pub

from model.pageModel import PageModel
from model.enumPage import Page

__all__ = ['PageController',]

class PageController:
    def __init__(self):
        self.pageModel = PageModel()
        pub.subscribe(self.pageChanged,"PAGE_CHANGED")
    
    def goToHome(self):
        self.pageModel.goToHomePage()
    
    def goToUSBPage(self):
        self.pageModel.goToUSBPage()

    def pageChanged(self,page):
        print(page)
