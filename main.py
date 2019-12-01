#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
import platform

from view import RootView,ProviderFrame
from model import PageModel
from controller import PageController

if platform.system() != 'Windows':
    from hardware import Hardware
    

if __name__ == "__main__":
    m = PageModel()
    v = RootView()
    p = ProviderFrame(v)
    if platform.system() != 'Windows':
        h = Hardware()

    c = PageController(m,v,p)
    
    c.getView().mainloop()
   

