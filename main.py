#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from view import RootView,ProviderFrame
from model import PageModel
from controller import PageController
from hardware import Hardware
import time

if __name__ == "__main__":
    m = PageModel()
    v = RootView()
    p = ProviderFrame(v)
    h = Hardware()

    c = PageController(m,v,p)
    
    c.getView().mainloop()
   

