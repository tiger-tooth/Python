#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:44:03 2017

@author: tarzan
"""
d = {'a': 1, 'b': 2, 'c': 3}
for t in d:
    print t
    

for val in d.itervalues():
    print val

for a in 'ABC':
    print a

from collections import Iterable
print isinstance(11111,Iterable)


for x,y in ([1,2],[3,5]):
    print x,'--',y

