# -*-  coding: utf-8 -*-
# @Filename: 迭代
# @Date: 2017-05-07 16:58
# from collections import Iterable
# d = {'a': 1, 'b': 2, 'c': 3}
# e = 2
# for i, y in d.items():
# 	print(i, y)
#
# a = isinstance(e, Iterable)
# print(a)
#
# a = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
# b = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
# i=0
# j=0
# q=1
# while i<10:
# 	j=0
# 	while j<12:
# 		print(q)
# 		print(a[i]+b[j])
# 		q=q+1
# 		j=j+1
# 	i=i+1
a = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
b = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
i=0
while i <60:
	c = [a[i % len(a)] + b[i % len(b)]]
	print(c)
	i=i+1

