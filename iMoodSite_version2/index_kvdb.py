
from bottle import Bottle, run,template,request
import os
import sae
import sae.kvdb

app =Bottle()
#initial operation
kv =sae.kvdb.Client()
kv.set('key0','Welcome all!')

def insert_int_db(diaryInput):
	keySets = get_keys_by_prefix('key')
	latestN = len(keySets)
	keyNumber ='key' +str(latestN)
	kv.set(keyNumber,diaryInput)
	return latestN

def get_all_data():
        results =[]
	#this copyed from wp, very nice design,return list
	for i in kv.get_by_prefix('key'):
	    results.append(i[1])
	return results
	
@app.route('/')
def mainpage():
        return template('write',diaryWritten='Hello')
@app.route('/write',method='POST')
def write():
        diaryInput =request.forms.get('diaryInput')
	total = insert_int_db(diaryInput)
	diaryAlreadyWritten =get_all_data()
        return template('write',diaryWritten=diaryAlreadyWritten)

application =sae.create_wsgi_app(app)
