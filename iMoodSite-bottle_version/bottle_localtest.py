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

from bottle import static_file
@app.route('/static/<test>')
def server_static(test):
    test +=".jpg" 
    return static_file(test, root='/Users/Zoe/GitHub/bootstrap-practice/iMoodSite/static/')

# Static Routes
@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico|jpeg)>')
def images(filename):
    return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@app.route('/index')
def index():
    return template('index')

debug(True)
run(app, host='localhost', port =1234,reloader=True)
