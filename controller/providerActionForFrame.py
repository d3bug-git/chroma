#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils import require
require('tkinter')
from tkinter.messagebox import askretrycancel
from model import ChromaAnalyse
from view import RootView,ConfirmAnalyseFrame

__all__ = ['ProviderActionForFrame',]

class ProviderActionForFrame(object):
    def __init__(self,chromaAnalyse,*args,**kw):
        super(ProviderActionForFrame).__init__(*args,**kw)
        self.chromaAnalyse = chromaAnalyse

    def getChromaAnalyse(self):
        return self.chromaAnalyse
        
    def setChromaAnalyse(self,chromaAnalyse:ChromaAnalyse):
        self.chromaAnalyse = chromaAnalyse
    
    def getActionWhenQuit(self,frameName):
        """méthode qui selectionne la bonne action"""
        method_name = 'action_when_quit_'+frameName
        method = getattr(self, method_name,lambda:print("action_when_quit_not_found_for: "+frameName))
        return  method()

    def getActionWhenGoTo(self,frameName,frame):
        """méthode qui selectionne la bonne action"""
        method_name = 'action_when_go_to_'+frameName
        method = getattr(self, method_name,lambda frame:frame)
        return  method(frame)
    
    def action_when_quit_INSERT_USB(self,msg="Matériel d\'enregistrement,Aucune clef usb n\'a été détectée.\n \n Veuillez en insérer une."):
        path_key=""
        cond =True
        print("action_founded")
        while len(path_key)==0 and cond:
            if len(path_key)==0:
                cond = askretrycancel(title="Matériel d'enregistrement",message=msg)
        path_key= "/media/pi/" + path_key +"/data_chroma.xy"
    
    def action_when_quit_CONFIG_TIME(self):
        #self.action_when_quit_INSERT_USB(msg="Veuillez insérer la clé USB pour Continuer")
        self.chromaAnalyse.setDuration(int(RootView.getInstance().getFrame().getTimeConfigured()))

    def action_when_go_to_CONFIRM_ANALYSE(self,frame:ConfirmAnalyseFrame):
        frame.setDuration(self.chromaAnalyse.getDuration())
        return frame
