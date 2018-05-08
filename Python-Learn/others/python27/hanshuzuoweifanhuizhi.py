#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:00:41 2017

@author: tarzan
"""


#==============================================================================
# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum
# 
# f1=lazy_sum(1,3,5,7,9)
# 
# f2=lazy_sum(1,3,5,7,1)
# print f1()==f2()
# 
# 
#==============================================================================


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
    
        
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()



