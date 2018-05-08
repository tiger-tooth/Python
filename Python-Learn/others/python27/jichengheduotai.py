#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:54:43 2017

@author: tarzan
"""

class Animal(object):
    def run(self):
        print 'Animal is running...'
        
class Dog(object):
    def run(self):
        print 'Dog is running...'
class Cat(object):
    def run(self):
        print 'Cat is running...'
dog=Dog()
dog.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)