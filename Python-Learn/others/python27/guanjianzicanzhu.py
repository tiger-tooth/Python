#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:37:02 2017

@author: tarzan
"""

def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

person('Michael',30)

kw={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=kw['city'],job=kw['job'])
person('Jack',24,**kw)

    