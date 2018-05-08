#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:48:46 2017

@author: tarzan
"""
import functools

int2=functools.partial(int,base=2)

print int2('1000000')

print int2('100000',base=10)



