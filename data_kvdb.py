# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sae.kvdb
from datetime import datetime

def store_mood(flow, moodname, story):
	user = request.get_cookie('account', secret='somekey')
	time = datetime.now()
	str_time = time.strftime('%Y%m%d%H%M%S')
	kv = sae.kvdb.Client()
	key = 'immmood___'+user.encode('utf-8')+'___mmi'+str_time
	value = (user, moodname, flow, story, time)
	kv.add(key, value)
	
def revise_mood(key, flow, moodname, story):
	kv = sae.kvdb.Client()
	time = kv.get(key)[4]
	user = kv.get(key)[0]
	value = (user, moodname, flow, story, time)
	kv.replace(key, value)
	
def store_chat(user, content):
	kv=sae.kvdb.Client()
	time = datetime.now()
	str_time = time.strftime('%Y%m%d%H%M%S')
	key='immchat___'+str_time+'___mmi'
	value = (user, content, time)
	kv.add(key, value)

def store_dairy(user, content):
	kv=sae.kvdb.Client()
	time = datetime.now()
	str_time = time.strftime('%Y%m%d%H%M%S')
	key='immdairy___'+str_time+'___mmi'
	value = (user, content, time)
	kv.add(key, value)	
	
def revise_chat_dairy(key, content):
	kv=sae.kvdb.Client()
	user=kv.get(key)[0]
	time=kv.get(key)[2]
	value = (user, content, time)
	kv.replace(key, value)
	
def delete_one(key):
	kv = sae.kvdb.Client()
	kv.delete(key)

def show_list(prefix):
	kv=sae.kvdb.Client()
	last_key=None
	list = []
	while True:
		list += [i for i in get_by_prefix(prefix, marker=last_key)]
		if len(list)<100:
			break
		else:	
			last_key = list[100][0]
	return sorted(list)
	
def store_userinfo(userid, password)
	kv = sae.kvdb.Client()
	information = ''
	if not userid:
		information = 'Ahoo，你的用户名弄丢了？'
	else:	
		key_user = 'immuser___'+userid.encode('utf-8')+'___mmi'
		if ord(char) <33 or ord(char) ==127 for char in U_u: 	
			information='Oops, 你的用户名里混进了奇怪的东西！'
			break
		elif kv.get(key_user):
			information = 'Oops, 英雄所见略同，有人和你重名了!'	
		else:
			kv.add(key_user, password)
			information = '你的用户名已被保存，现在就登录，开始一段心路历程吧！'
	return information	

def backup():
	if request.GET.get('send'):
		password = request.GET.get('password')
		if password=='seriously!important!':
			kv=sae.kvdb.Client()
	key_prefix=('immuser___', 'immmood___', 'immchat___', 'immdairy___')
	for prefix in key_prefix:
		body = [i for i in kv.get_by_prefix(prefix)]
		data = open(prefix[3:-4]+'.cvs','w+')
		pprint(body, data)
	kv.disconnect_all()
	return '备份成功'	
	