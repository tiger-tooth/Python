#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 18:10:32 2017

@author: tarzan
"""


def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
a=[1,2,3]
print calc(*a)

