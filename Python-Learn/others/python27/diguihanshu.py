#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:55:59 2017

@author: tarzan
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print fact(5000)