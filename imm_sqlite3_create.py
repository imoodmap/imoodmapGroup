#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xiaoyuer
# @Date:   2015-12-14 23:36:33
# @Last Modified time: 2015-12-14 23:40:56
def create():
    import sqlite3
    cxn=sqlite3.connect('sqlite3/imood')
    cur=cxn.cursor()
    cur.execute('CREATE TABLE emotionDiary(studentName VARCHAR(16),id INTEGER,emotionType CHAR(8),flowValue INTEGER,tpFeeling CHAR(8),tireness CHAR(8),dairyContent LONGTEXT,inputTime DATETIME)')
