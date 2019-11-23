#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from .frame import HomeFrame,GraphFrame,InsertUSBFrame,ConfirmAnalyseFrame,ConfigTimeFrame

__all__ = ['ProviderFrame',]

class ProviderFrame(object):
    def __init__(self,viewParent,*args,**kw):
        super(ProviderFrame).__init__(*args,**kw)
        self.viewParent = viewParent
    
    def getFrame(self,frameName):
        """méthode qui selectionne le bon Frame """
        method_name = 'frame_'+frameName
        method = getattr(self, method_name, lambda: "Frame not found")
        return method()

    def frame_HOME(self):
        return HomeFrame(self.viewParent)

    def frame_INSERT_USB(self):
        return InsertUSBFrame(self.viewParent)
    
    def frame_CONFIG_TIME(self):
        return ConfigTimeFrame(self.viewParent)
    
    def frame_CONFIRM_ANALYSE(self):
        return ConfirmAnalyseFrame(self.viewParent)
    
    def frame_REAL_TIME_GRAPH(self):
        return GraphFrame(self.viewParent)
    
        

