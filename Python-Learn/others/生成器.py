# -*-  coding: utf-8 -*-
# @Filename: 生成器
# @Date: 2017-05-09 13:47

# L=(x*x for x in range(10))
# for n in L:
# 	print(n)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a,b = b, a+b
		n=n+1
	print('done')

fib(10)