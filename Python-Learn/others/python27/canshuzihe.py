#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:45:33 2017

@author: tarzan
"""

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():\n----what the hell is it ?' % func.__name__
        return func(*args, **kw)
    return wrapper

@log

def f(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

f(1,2)
#==============================================================================
# func(1,2,3,(1,2,3))
# func(1,2,3,'ass')
# func(1,2,3,'happy','kiss')
# func(1,2,3,'jijijiji',5)
# 
# kw={'ag':'ag','bg':'bg'}
# func(1,2,3,'jijijiji',**kw)
# func(1,2,3,'bili',x=1,y=3,z=344)
# 
# 
#==============================================================================

