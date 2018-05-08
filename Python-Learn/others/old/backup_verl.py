# -*-  Project Name:'Code'
# -*-  Name:'backup_verl'
# -*-  Author:'Tarzan'
# -*-  Date:'2017/1/10'  '14:23'
# -*-  coding: utf-8 -*-

import os
import time

source=[r'E:\_Python\trash\docs',r'E:\_Python\trash\texts']

target_dir=r'E:\_Python\trash\backup'

target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip %s%s"%(target,''.join(source))

if os.system(zip_command)==0:
	print 'Successful backuo to',target
else:
	print 'Backup FAILED'
