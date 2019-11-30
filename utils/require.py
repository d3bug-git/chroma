#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

import pip, sys,platform

__all__ = ['install','require',]

#En fonction de la version de pip je choisi le bon main
if int(pip.__version__.split('.')[0])>9:
    if platform.system() =='Windows':
        from pip._internal.main import main
    else:
        from pip._internal import main       
else: 
    from pip import main

#fonction utile juste pour installer un package
def install(package):
    main(['install', package])
 
# On essaye d'importer les dépendances, et si elles sont pas dispos on les installe 
# pour l'utilisateur courant.
def require(*packages):
    for package in packages:
        try:
            if not isinstance(package, str):
                import_name, install_name = package
            else:
                import_name = install_name = package
            __import__(import_name)
        except ImportError:
            cmd = ['install', install_name]
            if not hasattr(sys, 'real_prefix'):
                cmd.append('--user')
            main(cmd)

