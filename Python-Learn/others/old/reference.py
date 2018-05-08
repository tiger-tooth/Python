# -*-  Project Name:'Code'
# -*-  Name:'reference'
# -*-  Author:'Tarzan'
# -*-  Date:'2017/1/3'  '19:47'
# -*-  coding: utf-8 -*-
print ('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

del shoplist[0]

print ('shoplist is',shoplist)
print ('my list is',mylist)

print('Copy by making a full slice')
del mylist[0]

print ('shoplist is',shoplist)
print ('mylist is',mylist)
