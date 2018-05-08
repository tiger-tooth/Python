# -*-  coding: utf-8 -*-
# @Filename: calc
# @Date: 2017-05-05 11:48

def calc(*number):
	sum=0
	for n in number:
		sum=sum+n
	return sum
x=[1,2,3,4]
m=calc(*x)
print(m)