#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:19:56 2017

@author: tarzan
"""



class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
        
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
      
    def set_score(self,score):
        self.__score=score
    
    
bart = Student('Bart Simpson', 59)
bart.set_score(99)
print bart.get_name()
print bart.get_score()

#bart.print_score()
#print bart.get_grade()


