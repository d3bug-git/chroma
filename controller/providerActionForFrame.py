#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils import require
require("pypubsub")
from pubsub import pub
from model import ChromaAnalyse
from view import RootView,ConfirmAnalyseFrame,ConfigTimeFrame,Popup,InsertUSBFrame,GraphFrame,HomeFrame
from hardware import Broche
import time

__all__ = ['ProviderActionForFrame',]

class ProviderActionForFrame(object):
    def __init__(self,controller=None,*args,**kw):
        super(ProviderActionForFrame).__init__(*args,**kw)
        self.controller = controller
        self.animationForGraphFrameFunction =None

    def setController(self,controller):
        self.controller = controller
    
    def getActionWhenQuit(self,frameName):
        method_name = 'action_when_quit_'+frameName
        method = getattr(self, method_name,lambda:print("action_when_quit_not_found_for: "+frameName))
        return  method()

    def getActionWhenGoTo(self,frameName,frame):
        method_name = 'action_when_go_to_'+frameName
        method = getattr(self, method_name,lambda frame:frame)
        return  method(frame)

    def getPathOfUSBKey(self):
        import subprocess
        keyPath=""

        #cmd to execute
        cmd = "ls /media/pi"

        #execute cmd
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        
        #get name of key usb
        keyName = proc.stdout.readline()
        keyPath=keyName.rstrip()
        keyPath=str(keyPath,'utf-8')

        return keyPath
#********************************Action when quit********************************
    def action_when_quit_INSERT_USB(self,title="Matériel d'enregistrement",msg="Matériel d\'enregistrement,Aucune clef usb n\'a été détectée.\n \n Veuillez en insérer une."):
        import platform
        if platform.system() != 'Windows':
            print("enter action when quit insert usb")
            popup = Popup()
            keyPath = self.getPathOfUSBKey()
            RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",popup.quit)
            while len(keyPath)==0:
                popup.popupAskRetry(title=title,message=msg)
                keyPath = self.getPathOfUSBKey()
            popup.destroy()
            RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>")
            RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",self.controller.goToNextPage)
            keyPath= "/media/pi/"+ keyPath+"/"
            ChromaAnalyse.getInstance().setKeyPath(keyPath)
            print("quit action when quit insert usb")          
    
    def action_when_quit_CONFIG_TIME(self):
        self.action_when_quit_INSERT_USB(title="Matériel d'enregistrement",msg="Veuillez insérer la clé USB pour Continuer")

        ChromaAnalyse.getInstance().setDuration(int(RootView.getInstance().getFrame().getTimeConfigured()))
        pub.sendMessage("DURATION_OF_ANALYSE",duration=ChromaAnalyse.getInstance().getDuration())
        RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_PLUS)+">>")
        RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_MOINS)+">>")

    def action_when_quit_CONFIRM_ANALYSE(self):
        import platform
        if platform.system() != 'Windows':
            from hardware import Hardware
            Hardware.getInstance().deactiveSwitchMachine()
        self.action_when_quit_INSERT_USB(title="Matériel d'enregistrement",msg="Veuillez insérer la clé USB pour Lancer l'analyse")
   
    def action_when_quit_REAL_TIME_GRAPH(self):
        import platform
        if platform.system() != 'Windows':
            from hardware import Hardware
            Hardware.getInstance().stopThreadForReadAdc()
            #TODO: verify if usb key is inserted
            ChromaAnalyse.getInstance().saveDataToUsbKey()
            RootView.getInstance().getFrame().saveImageOfGraphWithName(ChromaAnalyse.getInstance().getKeyPath()+ChromaAnalyse.getInstance().getNameOfFile())
        self.animationForGraphFrameFunction=None
        popup = Popup()
        #bind to quit popup
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",popup.quit)
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_STOP)+">>",popup.quit)
        #display popup
        title = "Matériel d'enregistrement"
        message = "Les données ont bien été enregistrées sur la clé USB\n:)"
        popup.popupInformation(title=title,message=message)
        popup.destroy()
        #unbind stop an ok to quit
        RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>")
        RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_STOP)+">>")
        #bind ok,stop to next an previous page
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>",self.controller.goToNextPage)
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_STOP)+">>",self.controller.goToPreviousPage)
        ChromaAnalyse.getInstance().reset()
         
#********************************Action when go********************************
    def action_when_go_to_HOME(self,frame:HomeFrame):
        return frame
    def action_when_go_to_INSERT_USB(self,frame:InsertUSBFrame):
        import platform
        if platform.system() != 'Windows':
            from hardware import Hardware
            #Hardware.getInstance().activateSelectorMachine()
            #Hardware.getInstance().activateSelectorVmax()
            Hardware.getInstance().startThreadGetStateOfPin()
        return frame

    def action_when_go_to_CONFIG_TIME(self,frame:ConfigTimeFrame):
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_PLUS)+">>",frame.incrementTimeConfigured)
        RootView.getInstance().bind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_MOINS)+">>",frame.decrementTimeConfigured)
        return frame

    def action_when_go_to_CONFIRM_ANALYSE(self,frame:ConfirmAnalyseFrame):
        import platform
        if platform.system() != 'Windows':
            from hardware import Hardware
            Hardware.getInstance().activeSwitchMachine()
        frame.setDuration(ChromaAnalyse.getInstance().getDuration())
        return frame
    
    def action_when_go_to_REAL_TIME_GRAPH(self,frame:GraphFrame):
        import platform
        if platform.system() != 'Windows':
            from hardware import Hardware
            #Hardware.getInstance().deactivateSelectorMachine()
            #Hardware.getInstance().deactivateSelectorVmax()
            Hardware.getInstance().stopThreadGetStateOfPin()
            Hardware.getInstance().startThreadForReadAdc()
            frame.setVMax(Hardware.getInstance().getVMax())
        self.animationForGraphFrameFunction = frame.startAnimation()
        frame.setDuration(ChromaAnalyse.getInstance().getDuration())
        
        RootView.getInstance().unbind("<<"+self.controller.convertBrocheToBrocheName(Broche.BUTTON_OK)+">>")
        return frame

