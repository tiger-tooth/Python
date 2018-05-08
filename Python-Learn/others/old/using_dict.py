# -*-  Project Name:'Code'
# -*-  Name:'using_dict'
# -*-  Author:'Tarzan'
# -*-  Date:'2016/12/29'  '10:32'
# -*-  coding: utf-8 -*-
ab = {'Swaroop': 'swaroopch@byteofpython.info',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.com',
      'Spammer': 'spammer@hotmail.com'}

print ("Swaroop's address is %s " % ab['Swaroop'])

ab['Guido'] = 'guido@python.org'


del ab['Spammer']

print ('\nThere are %d contacts in the address-book\n' % len(ab))

for name, address in ab.items():
    print ('Contact %s at %s' % (name, address))

print ("\nGuido's address is %s" % ab['Guido'])
