# -*-  Project Name:'Code'
# -*-  Name:'using_tuple'
# -*-  Author:'Tarzan'
# -*-  Date:'2016/12/28'  '20:13'
# -*-  coding: utf-8 -*-
zoo=('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)

new_zoo=('monkey','dolphin',zoo)
print 'Number of animals is',len(new_zoo)
print 'All animals in new zoo are',new_zoo
print 'Animals also brought from old zoo are',new_zoo[2]
print 'Last animal brought from old zoo is',new_zoo[2][2]

