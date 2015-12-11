# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sae
import sae.kvdb

from bottle import Bottle
from bottle import run, redirect, template, request, response, static_file
from bottle import debug

from pprint import pprint

from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

debug(True)
app = Bottle()

#情绪显示/新输入
@app.route('/imoodmap', method='get')
def moodmap():
	kv = sae.kvdb.Client()
	if request.GET.get('save'):
		newmood = unicode(request.GET.get('newmood'))
		level = int(request.GET.get('moodlevel'))
		story = unicode(request.GET.get('story'))
		currentT = datetime.now()
		Time = currentT.strftime('%Y%m%d%H%M%S')
		key_newmood = 'immmood___'+newmood.encode('utf-8')+'___mmi'+Time
		value_newbody = [newmood, level, story, currentT]
		kv.add(key_newmood, value_newbody)
	keylist = kv.getkeys_by_prefix('immmood___')
	#key为'immmood___'+情绪名+'___mmi'+系统时间
	moodname = {i[10:-20] for i in keylist}
	valuelist = kv.get_by_prefix('immmood___')
	#value是每组为（情绪名，情绪评分，故事，系统时间）的复合列表
	body = [i for i in valuelist]
	output = template('imm_main', rows = body)
	return output

#储存备份
@app.route('/backup')
def backup():
	kv=sae.kvdb.Client()
	key_prefix='immmood___'
	body = [i for i in kv.get_by_prefix(key_prefix)]
	data = open('imm_data.txt','w+')
	pprint(body, data)
	kv.disconnect_all()
	return '备份成功'

#CSS, images
@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root = '/path')
	
application = sae.create_wsgi_app(app)