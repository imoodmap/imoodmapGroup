# -*- coding: utf-8 -*-
#!/usr/bin/env python
#这是一个参考：
#本文档2015-12-23日pull下的index.wsgi，对其中涉及到数据库的内容略有更改。主要为：
#1 用户密码加密
#2 数据库结构调整（命名略有差异）
#3 checklogin时仅从库中抽提完全吻合的用户名密码
#其中1的实现，需要将mysql中users数据库的password格式改为BLOB
#数据库调整为三个表，分别为users，moodtype，和records，不同用户的情绪纪录均放在同一个records中，以foreign key（moodtype_id和users_id进行相互索引）。moodtype表预先已完成输入。
#相关mysql数据库（app_storychain)已经共享给imoodmap。

import sae
import sae.kvdb
import MySQLdb


from bottle import Bottle
from bottle import run, redirect, template, request, response, static_file
from bottle import debug

from pprint import pprint

from os import path

import sys
reload(sys)
sys.setdefaultencoding('utf8')

debug(True)
app = Bottle()


#imm测试
#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root = "./imm/static/css")

#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/static/js")

#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/static/font-awesome")

#@app.route('/imm/font-awesome/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/font-awesome")


#@app.route('/imm/images/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/jpg')

#@app.route('/imm/images/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/png')

#@app.route('/imm/img/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/png')

#@app.route('/imm/img/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/jpg')

#@app.route('/imm/img/portfolio/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/portfolio', mimetype='image/png')

#@app.route('/imm/img/portfolio/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/porftolio', mimetype='image/jpg')

#@app.route('/imm/img/portfolio/<filename:re:.*\.jpeg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/portfolio', mimetype='image/jpeg')

#@app.route('/imm/static/img/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/static/img', mimetype='image/jpg')

mysql_host = "w.rdc.sae.sina.com.cn"
mysql_port = 3307
mysql_user = 'the_access_key'
mysql_passwd = "the_secret_key"
mysql_db = 'app_storychain'

	
@app.route('/imm')
@app.route('/imm/login')
def immlogin():
    return template('imm/imm_login', alertContent = "请登录，第一次见面直接登录注册")

@app.route('/imm/login', method ="POST")
def checkimmlogin():
	username = request.forms.get("studentname")
	print username
	pwd = request.forms.get('password')
	db = MySQLdb.connect(
		host =mysql_host, 
		port =mysql_port, 
		user =mysql_user, 
		passwd = mysql_passwd, 
		db= mysql_db
		)
	cursor =db.cursor()

	#check the username
	cursor.execute('SELECT name, AES_DECRYPT(password, "littleporkbun") FROM users WHERE name = %s', (username))
	checkname =cursor.fetchone()
	if checkname:
		if pwd == checkname[1]:
			return template('imm/index1', studentname = username)
		else:
			return template('imm/imm_login', alertContent = "亲，密码错误，放轻松，请再次输入！")
	else:
		cursor.execute('''
			INSERT INTO users(name,password) 
			VALUES(%s, AES_ENCRYPT(%s, "littleporkbun"))''',
			(username, pwd)
			)
	cursor.close()
	db.commit()
	return template('imm/index1', studentname = username)



@app.route('/imm/index')
def mainpage():
    return template('imm/index1',studentname = "imm")

@app.route('/imm/index',method ='POST')
def editform():
	studentName = request.forms.get('username')
	emotionType =request.forms.get('emotionType')
	flowValue =int(request.forms.get('flowValue'))
	tpFeeling =int(request.forms.get('tpFeeling'))
	tireness =int(request.forms.get('tireness'))
	diaryContent =request.forms.get('diaryContent')
	print studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent
	db = MySQLdb.connect(
		host =mysql_host, 
		port =mysql_port, 
		user =mysql_user, 
		passwd = mysql_passwd, 
		db= mysql_db
		)
	cursor =db.cursor()

	cursor.execute('SELECT id FROM users WHERE name =%s', (studentName))
	users_id = cursor.fetchone()[0]
	print users_id
	cursor.execute('SELECT id FROM moodtype WHERE type =%s', (emotionType))
	moodtype_id = cursor.fetchone()[0]
	print moodtype_id
	print moodtype_id+users_id
	print flowValue+tpFeeling+tireness
	cursor.execute('''INSERT INTO records 
		(content,flow, tiredness, physicalcomfort,users_id,moodtype_id)
		VALUES(%s,%r, %r, %r,%r,%r)
		''', 
		(diaryContent,flowValue, tireness, tpFeeling, users_id, moodtype_id))
	cursor.close()
	db.commit()



@app.route('/imm/echarts')
def echarts():
    counttypes =[2,4,6,8,10]
    return template('imm/echarts', countTypes = counttypes)

@app.route('/imm/echarts_pie')
def echarts_pie():
    counttypes =[2,4,6,8,10]
    return template('imm/echarts_pie', countTypes = counttypes) 



	
application = sae.create_wsgi_app(app)



