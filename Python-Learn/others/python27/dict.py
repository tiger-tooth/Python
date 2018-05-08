#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:39:50 2017

@author: tarzan
"""

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d
print d['Michael']
d['Adam']=67
print d

print 'Thomas' in d

print d.get('Thoms')

d.pop('Bob')
print d.get('Bob')


 