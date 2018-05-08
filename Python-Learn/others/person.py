# -*-  coding: utf-8 -*-
# @Filename: person
# @Date: 2017-05-05 13:55

# def person(name, age, **kw):
# 	print('name:', name, 'age', age, 'other:', kw)
#
# person('michale',17)
# person('jack',29,c='beijing',d='guangzhou')
#
# extra={'city':'beijing',
#        'gender':'male'}
# person('Kiki',20,**extra)
#
# def person(name, age, **kw):
# 	if 'city' in kw:
# 		pass
# 	if 'job' in kw:
# 		pass
# 	print('name:', name, 'age:', age, 'other:', kw)

def person(name,age,*,city,job):
	print(name,age,city,job)


person('jack', 24, city='beijing', jobw='chaoyang')
