#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:03:25 2017

@author: tarzan
"""
#==============================================================================
# 
# def f(x):
#     return x*x
# 
# print map(f,[1,2,3,4,5,6,7,8,9])
# 
# 
# print map(str,[1,2,3,4,5,6,7,8,9])
# 
# 
# def add(x,y):
#     return x+y
# print reduce(add,[1,2,3,4,5])
# 
# def fn(x,y):
#     return x*10+y
# print reduce(fn,[1,3,5,7,9])
#==============================================================================


def f(x,y):
    return x*10+y

def char2int(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(f,map(char2int,'13579'))








