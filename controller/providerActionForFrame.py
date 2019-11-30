#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils import require
require('tkinter')
from tkinter.messagebox import askretrycancel

__all__ = ['ProviderActionForFrame',]

class ProviderActionForFrame(object):
    def __init__(self,*args,**kw):
        super(ProviderActionForFrame).__init__(*args,**kw)
    
    def getActionWhenQuit(self,frameName):
        """méthode qui selectionne la bonne action"""
        method_name = 'action_when_quit_'+frameName
        method = getattr(self, method_name,lambda:print("action_not_found_for: "+frameName))
        return  method()
    
    def action_when_quit_INSERT_USB(self):
        path_key=""
        cond =True
        print("action_founded")
        while len(path_key)==0 and cond:
            if len(path_key)==0:
                cond = askretrycancel('Matériel d\'enregistrement','Aucune clef usb n\'a été détectée.\n \n Veuillez en insérer une.')
        path_key= "/media/pi/" + path_key +"/data_chroma.xy"