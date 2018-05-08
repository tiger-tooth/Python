#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:07:37 2017

@author: tarzan
"""

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad oprand type')
    
    
    if x>=0:
        return x
    else:
        return -x



print my_abs(909)
print my_abs(-100)

print my_abs('s')

