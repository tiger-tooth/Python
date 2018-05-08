#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:38:46 2017

@author: tarzan
"""

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

print power(5)



def enroll(name,gender):
    print 'name:', name
    print 'gender:', gender

enroll('Sarah', 'F')
