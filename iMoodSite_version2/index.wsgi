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

mysql_host = "w.rdc.sae.sina.com.cn"
mysql_port = 3307
mysql_user = 'the_access_key'
mysql_passwd = "the_secret_key"
mysql_db = 'app_imoodmap'


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
    studentName = request.forms.get('studentname')
    pwd = request.forms.get('password')

    #connect db
    db = MySQLdb.connect(
        host =mysql_host, 
        port =mysql_port, 
        user =mysql_user, 
        passwd = mysql_passwd, 
        db= mysql_db
        )

    cursor =db.cursor()
    cursor.execute('USE app_imoodmap')
    #已经创建，若没有测创建一次
    #用 users 表单取代 user_data
    #cursor.execute('CREATE TABLE user_data(studentName VARCHAR(16), password VARCHAR(16),uid INTEGER AUTO_INCREMENT PRIMARY KEY)')
    #cursor.execute('CREATE TABLE users(studentName VARCHAR(16), password BLOB,uid INTEGER AUTO_INCREMENT PRIMARY KEY)')
    


    #check the username
    #cursor.execute('SELECT studentName, password FROM user_data')
    cursor.execute('SELECT studentName, AES_DECRYPT(password, "key"+"%s") as password FROM users '%(studentName))

    checkname =cursor.fetchall()
    #看看用户是否存在
    for item in checkname:
        if studentName == item[0] and pwd != item[1]:
            cursor.close()
            db.close()
            return template('imm_login', alertContent = "亲，密码错误，放轻松，请再次输入！")
        if studentName == item[0] and pwd == item[1]:
            cursor.close()
            db.close()
            return template('index1', studentname = studentName, mark ="back")


    #用户不存在，则注册
    #cursor.execute('INSERT INTO user_data(studentname,password) VALUES("%s","%s")'%(studentName,pwd))
    cursor.execute('INSERT INTO users(studentName,password) VALUES("%s",AES_ENCRYPT(%s, ("key"+"%s")))'%(studentName,pwd, studentName))
    cursor.close()
    db.commit()
    db.close()
    return template('index1', studentname = studentName, mark= "freshman")



@app.route('/index')
def mainpage():
    return template('index1',studentname = "imm")

@app.route('/editform',method ='POST')
def editform():
    #判断新人是否mark 标记
    marktag =  request.forms.get('mark')

    studentName = request.forms.get('username')
    emotionType =request.forms.get('emotionType')
    flowValue =int(request.forms.get('flowValue'))
    tpFeeling =request.forms.get('tpFeeling')
    tireness =int(request.forms.get('tireness'))
    diaryContent =request.forms.get('diaryContent')

    db = MySQLdb.connect(
        host =mysql_host, 
        port =mysql_port, 
        user =mysql_user, 
        passwd = mysql_passwd, 
        db= mysql_db
        )
    cursor =db.cursor()
    cursor.execute('USE app_imoodmap')

    #根据back的后缀查看是否是新用户
    if "freshman" in marktag:
        #为新用户创建表单
        cursor.execute('CREATE TABLE %s(studentName VARCHAR(16), uid INTEGER AUTO_INCREMENT PRIMARY KEY,emotionType CHAR(8),flowValue INTEGER,tpFeeling CHAR(8),tireness Integer(8),diaryContent TEXT,inputTime DATETIME)'%(studentName))

    #构建一个tuple来放所有信息
    inputtuple =(studentName, studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent, time.strftime('%Y-%m-%d %H:%M:%S'))
    cursor.execute('INSERT INTO %s(studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent, inputTime) VALUE("%s","%s",%d,"%s",%d,"%s","%s")'%(inputtuple))
    cursor.close()
    db.commit()
    db.close()

    #将emotionType和一个数字对应，避免处理中文
    emotions = ['恐惧','悲伤','愤怒','讨厌','快乐']
    crp = zip(emotions, range(1,6))  # 注意 1 到5 对应顺序
    #建立字典
    dict_crp = dict(crp)
    #建立统计情绪出现次数的

    #获取所有的emotionType 的值 和 flowValue 的值
    db = MySQLdb.connect(
        host =mysql_host, 
        port =mysql_port, 
        user =mysql_user, 
        passwd = mysql_passwd, 
        db= mysql_db
        )
    cursor =db.cursor()
    cursor.execute('USE app_imoodmap')
    cursor.execute('SELECT emotionType, flowValue, inputTime FROM %s'%(studentName))
    get_data_charts = cursor.fetchall()
    emotionTypelist_charts =[]
    flowlist_charts =[]
    for item in get_data_charts:
        #emotionType 转为数字的list
        emotionTypelist_charts.append(dict_crp[item[0]])
        #flowValue直接是数字的list
        flowlist_charts.append(item[1])
    #统计object出现次数,按对应顺序 tuple 
    countEmotionType = [emotionTypelist_charts.count(1), emotionTypelist_charts.count(2), emotionTypelist_charts.count(3), emotionTypelist_charts.count(4), emotionTypelist_charts.count(5)]

    countFlowValue = [flowlist_charts.count(0), flowlist_charts.count(1), flowlist_charts.count(2), flowlist_charts.count(3), flowlist_charts.count(4), flowlist_charts.count(5), flowlist_charts.count(6), flowlist_charts.count(7),flowlist_charts.count(8), flowlist_charts.count(9)]  
    cursor.close()
    db.commit()
    db.close()

    return template('echarts_pie', countTypes = countEmotionType)


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
