# -*-  coding: utf-8 -*-
# @Filename: my_abs
# @Date: 2017-05-04 17:30

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>0:
		return x
	else:
		return -x

a=my_abs(1212121212)
print(a)