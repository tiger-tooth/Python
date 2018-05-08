#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:18:53 2017

@author: tarzan
"""

__author__='Michael Liao'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print 'Hello,world!'
    elif len(args)==2:
        print 'Hello,%s!' % args[1]
    else:
        print 'Too many arguments!'


if __name__=='__main__':
    test()
    
