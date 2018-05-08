#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:28:03 2017

@author: tarzan
"""

names = ['Michael','Bob','Tracy']
for name in names:
    print name
    
sum = 0
for x in range(101):
    sum = sum + x
print sum

#birth = int(raw_input('birth: '))
birth = input()
if birth<2000:
    print 'before 00'
else:
    print 'after 00'

