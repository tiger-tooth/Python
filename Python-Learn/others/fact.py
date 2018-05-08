# -*-  coding: utf-8 -*-
# @Filename: fact
# @Date: 2017-05-05 16:41

def fact(x):
	if x == 1:
		return 1
	return x * fact(x - 1)


print(fact(1000))
