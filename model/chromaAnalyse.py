#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
__all__ = ['ChromaAnalyse',]

class ChromaAnalyse:
    __instance =None

    @staticmethod
    def getInstance():
        if ChromaAnalyse.__instance == None:
            ChromaAnalyse()
        return ChromaAnalyse.__instance

    def __init__(self,**kw):
        if ChromaAnalyse.__instance != None:
            raise Exception("Cette classe est un Singleton")
        else:
            ChromaAnalyse.__instance = self
        
        self.duration = 10
        self.keyPath = ""

    def getDuration(self):
        return self.duration

    def setDuration(self,duration):
        self.duration = duration

    def getKeyPath(self):
        return self.keyPath

    def setKeyPath(self,keyPath):
        self.keyPath = keyPath