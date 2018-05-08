# -*-  coding: utf-8 -*-
# @Filename: 切片
# @Date: 2017-05-07 16:22

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0],L[1]])
r=[]
n=3
for i in range(n):
	r.append(L[i])
print(r)
L=list(range(100))
print(L[10:15:2])