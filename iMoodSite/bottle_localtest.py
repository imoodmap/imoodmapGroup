# -*- coding: utf-8 -*-
# @Author: imoodmap Group

from bottle import Bottle,run,template,request,debug
import sqlite3


app =Bottle()
@app.route('/')
@app.route('/input/<name>')
def mainpage(name ='imm'):
	return 'hello'

@app.route('/output',method = 'POST')
def output():
    diaryContent =request.forms.get('diaryContent')
    flowValue =request.forms.get('flowValue')
    return template('Your flowValue is {{number}}, and your notes are {{notes}}', number = str(flowValue), notes = diaryContent)


debug(True)
run(app, host='localhost', port =8080,reloader=True)
