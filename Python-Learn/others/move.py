# -*-  coding: utf-8 -*-
# @Filename: move
# @Date: 2017-05-05 17:38

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
	if n == 1:
		print('move', a, '-->', c)
	else:
		move(n - 1, a, c, b)
		move(1, a, b, c)
		move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')