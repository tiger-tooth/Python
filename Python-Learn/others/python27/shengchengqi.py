#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:11:43 2017

@author: tarzan
"""

g=(x*x for x in range(1,11))


for n in g:
    print n


def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for n in fib(6):
    print n




