#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:02:22 2017

@author: tarzan
"""

print range(1,11)

print [x*x for x in range(1,11)]

print [m+n for m in 'abc' for  n in 'xyz']

import os
print [d for d in os.listdir('.')]


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,'--',v

x=['DFWEV','FWSS','CVBKO']
print [s.lower() for s in x]
             






