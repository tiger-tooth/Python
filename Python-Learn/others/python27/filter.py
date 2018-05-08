#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:21:11 2017

@author: tarzan
"""
def is_odd(n):
    return n%2==1
print filter(is_odd,range(1,101))

def not_empty(s):
    return s and s.strip()

print filter(not_empty,['a',None,'b','b'])



