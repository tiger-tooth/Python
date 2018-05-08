#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:34:47 2017

@author: tarzan
"""
import  math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny


x,y=move(100,100,60,math.pi/6)
print x,y
