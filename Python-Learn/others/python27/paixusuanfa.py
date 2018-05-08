#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:49:18 2017

@author: tarzan
"""

print sorted([36,5,12,9,21])

def re(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([36,5,12,9,21],re)


