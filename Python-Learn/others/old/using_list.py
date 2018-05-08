# -*-  Project Name:'Code'
# -*-  Name:'print_tuple'
# -*-  Author:'Tarzan'
# -*-  Date:'2016/12/28'  '21:13'
# -*-  coding: utf-8 -*-
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist), 'items to pleasure.'
print 'These items are:'
for item in shoplist:
    print item,


print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is',shoplist

print 'The first item I will buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist

