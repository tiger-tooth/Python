#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:13:22 2017

@author: tarzan
"""



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%s' %(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'



bart = Student('Bart Simpson', 59)

bart.print_score()
print bart.get_grade()