# -*- coding: utf-8 -*-
#!/usr/bin/env python

import MySQLdb
db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="", passwd ="", db="app_whalechen") #should be your key
cur =db.cursor()
cur.execute('USE app_whalechen')
'''
观察到：目前的sae-mysql app_whalechen数据库emotion_diary表格各栏为
fromUser（str） ct（time related str） flowStatement（int） content（str）
尚缺少一栏emotionType
以下这句是为在表格中插入这一栏
'''
cur.execute('ALTER TABLE emotion_diary ADD emotionType CHAR')

def store_mood(studentName, inputTime, flowValue, emotionType, diaryContent):
	'''
	储存输入的各关键数据（默认已为约定格式）
	'''
	cur.execute('USE app_whalechen')
	cur.execute(
		'''INSERT INTO emotion_diary 
		(fromUser, ct, flowStatement, content, emotionType)
		VALUES("%s", "%S", %d, "s%", "s%")''', 
		%(studentName, inputTime, flowValue, diaryContent, emotionType)
		)
	
def revise_mood(studentName, inputTime, flowValue, emotionType, diaryContent):
	'''
	按照时间和用户名更改各关键数据（默认已为约定格式）
	'''	
	cur.execute('USE app_whalechen')
	cur.execute(
		'''UPDATE emotion_diary 
		SET emotionType=emotionType 
		flowStatement=flowValue 
		content=diaryContent 
		WHERE ct = InputTime AND fromUser = studentName'''
		)
	
def show_one_record(inputTime, studentName):
	'''
	按照时间和用户名显示一条数据（默认已为约定格式）
	'''	
	cur.execute('USE app_whalechen')
	cur.execute('SELECT * FROM emotion_diary WHERE ct = imputTime AND fromUser=studentName')
	record = cur.fetchone()
	return record
	
def show_latest_records(studentName, emotionType):
	'''
	若未指定情绪类型(即'all')，则输出最近的5条记录。
	若指定情绪类型，则输出该类型最近5条记录。
	'''
	cur.execute('USE app_whalechen')	
	if emotionType = 'all':
		cur.execute(
			'''SELECT * FROM emotion_diary 
			WHERE fromUser = studentName
			ORDER BY ct DESC
			LIMIT 5'''
			)
	else:		
		cur.execute(
			'''SELECT * FROM emotion_diary 
			WHERE fromUser = studentName AND emotionType = emotionType
			ORDER BY ct DESC
			LIMIT 5'''
			)
	records = cur.fetchall()
	return records
	
def delete_one_in_mysql(studentName, inputTime):
	cur.execute('DELETE FROM emotion_diary WHERE ct = inputTime AND fromUser = studentName')	
	
