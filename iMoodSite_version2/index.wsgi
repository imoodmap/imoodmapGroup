#-*- coding:utf-8 -*-
#author: WhaleChen

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from bottle import Bottle, run,template,request,debug
import sae
import sae.const
import MySQLdb
import time 




app=Bottle()

from bottle import static_file
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = "./static/css")

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./static/js")

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./static/font-awesome")

@app.route('/font-awesome/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./font-awesome")


@app.route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./img', mimetype='image/jpg')

@app.route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./img', mimetype='image/png')

@app.route('/img/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./img', mimetype='image/png')

@app.route('/img/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./img', mimetype='image/jpg')

@app.route('/img/portfolio/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./img/portfolio', mimetype='image/png')

@app.route('/img/portfolio/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./img/porftolio', mimetype='image/jpg')

@app.route('/img/portfolio/<filename:re:.*\.jpeg>')
def send_image(filename):
    return static_file(filename, root='./img/portfolio', mimetype='image/jpeg')

@app.route('/static/img/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='.static/img', mimetype='image/jpg')


@app.route('/')
@app.route('/login')
def login():
    return template('imm_login', alertContent = "请登录，第一次见面直接登录注册")

@app.route('/login', method ="POST")
def checklogin():
	studentName = request.forms.get('studentname')
	pwd = request.forms.get('password')
	db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="", passwd ="", db="app_imoodmap")
	cursor =db.cursor()
	cursor.execute('USE app_imoodmap')
	#已经创建，若没有测创建一次
	#cursor.execute('CREATE TABLE user_data(studentName VARCHAR(16), password VARCHAR(16),uid INTEGER AUTO_INCREMENT PRIMARY KEY)')

	#check the username
	cursor.execute('SELECT studentName, password FROM user_data')
	usertuple =cursor.fetchall()
	#看看用户是否存在
	for item in usertuple:
	    if studentName == item[0] and pwd != item[1]:
	        cursor.close()
	        db.close()
	        return template('imm_login', alertContent = "亲，密码错误，放轻松，请再次输入！")
	    if studentName == item[0] and pwd == item[1]:
	        cursor.close()
	        db.close()
	        return template('index1', studentname = studentName + " back")
	#用户不存在，则注册
	cursor.execute('INSERT INTO user_data(studentname,password) VALUES("%s","%s")'%(studentName,pwd))
	cursor.close()
	db.commit()
	db.close()
	return template('index1', studentname = studentName)



@app.route('/index')
def mainpage():
    return template('index1',studentname = "imm")

@app.route('/editform',method ='POST')
def editform():
    studentName = request.forms.get('username')
    emotionType =request.forms.get('emotionType')
    flowValue =int(request.forms.get('flowValue'))
    tpFeeling =request.forms.get('tpFeeling')
    tireness =int(request.forms.get('tireness'))
    diaryContent =request.forms.get('diaryContent')
    db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="", passwd ="", db="app_imoodmap")
    cursor =db.cursor()
    cursor.execute('USE app_imoodmap')
    #根据back的后缀查看是否是新用户
    if studentName[-5:] != ' back':
        #为新用户创建表单
        cursor.execute('CREATE TABLE %s(studentName VARCHAR(16), uid INTEGER AUTO_INCREMENT PRIMARY KEY,emotionType CHAR(8),flowValue INTEGER,tpFeeling CHAR(8),tireness Integer(8),diaryContent TEXT,inputTime DATETIME)'%(studentName))
    else:
        studentName = studentName[:-5]
    #构建一个tuple来放所有信息
    inputtuple =(studentName, studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent, time.strftime('%Y-%m-%d %H:%M:%S'))
    cursor.execute('INSERT INTO %s(studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent, inputTime) VALUE("%s","%s",%d,"%s",%d,"%s","%s")'%(inputtuple))
    cursor.close()
    db.commit()
    db.close()


@app.route('/echarts')
def echarts():
    counttypes =[2,4,6,8,10]
    return template('echarts', countTypes = counttypes)

@app.route('/echarts_pie')
def echarts_pie():
    counttypes =[2,4,6,8,10]
    return template('echarts_pie', countTypes = counttypes)    


		
debug(True)	
application =sae.create_wsgi_app(app)
