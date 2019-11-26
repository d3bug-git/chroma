#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""

import setuptools

setuptools.setup(

    author='',
    name='Chroma project',
    py_modules=['main.py'],
    packages=['controller','model','view'],
    
    entry_points={}, 
        # Note, any changes to your setup.py, like adding to `packages`, or
        # changing `entry_points` will require the module to be reinstalled;
        # `python3 -m pip install --upgrade --editable ./chroma
)