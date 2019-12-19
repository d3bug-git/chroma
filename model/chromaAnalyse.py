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
        self.adcValue = []
        self.timeValue = []
        self.nameOfFile="unknow"

    def getDuration(self):
        return self.duration

    def getNameOfFile(self):
        return self.nameOfFile

    def setDuration(self,duration):
        self.duration = duration

    def getKeyPath(self):
        return self.keyPath

    def setKeyPath(self,keyPath):
        self.keyPath = keyPath

    def setAdcValue(self,value):
        self.adcValue.append(value)

    def setTimeValue(self,value):
        self.timeValue.append(value)
        
    def getAdcValue(self):
        return self.adcValue
    
    def getTimeValue(self):
        return self.timeValue

    def reset(self):
        self.duration = 10
        self.keyPath = ""
        self.adcValue = []
        self.timeValue = []
        self.nameOfFile="unknow"

    def saveDataToUsbKey(self):
        from datetime import datetime
        data = ""
        i=0
        numberOfDataSave  = len(self.adcValue)
        while i < numberOfDataSave:
            data = data +str(self.timeValue[i])+";"+str(self.adcValue[i])+"\n"
            i = i+1
        self.nameOfFile = str(datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss"))
        with open(self.keyPath+"analyse_"+self.nameOfFile+".xy", "w") as fichier:
            fichier.write(data)