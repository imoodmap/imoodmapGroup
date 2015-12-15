@app.post('/wechat')
def get_data():
        import xml.etree.ElementTree as ET
	str_xml =request.body.read()
	xml = ET.fromstring(str_xml)
	content =xml.find("Content").text
	msgType =xml.find("MsgType").text
	fromUser =xml.find("FromUserName").text
	toUser=xml.find("ToUserName").text
	createtime = int(time.time())
	len_cotent =len(content)	
	
	db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="", passwd ="", db="app_whalechen")
        cursor =db.cursor()
        cursor.execute('USE app_whalechen')
	if msgType == "event":
	    mscontent =xml.find("Event").text
	    if mscontent =='subscribe':
	        #cursor.execute('INSERT INTO emotion_diary (fromUser, ct, flowStatement,content) VALUES("%s","%s",%d,"%s")'%(fromUser,time.strftime('%Y-%m-%d %H:%M:%S'), 5,"begin"))
		contentEcho = '''欢迎关注本微信，期待和你一起寻找最棒的你！心流状态初始值为5。'''
        else:
	    if len_cotent > 100:
	        contentEcho = "对不起，内容太多，消化不良，试试短一些的句子"
            else:
                if content[0] in 'wW':
	            cursor.execute('SELECT content, dt FROM dairy_db') #find out diary is misspelled, the unique tag
	            idtuple =cursor.fetchall()
	            idlist =list(idtuple)
		    the1print = time.strftime('%Y-%m-%d %H:%M:%S')
	            the2print = "欢迎！你输入了： " + content[1:]
	            the3print = idlist[len(idlist)-1][1].strftime('%Y-%m-%d %H:%M:%S')
	            the4print = idlist[len(idlist)-1][0]
		    newid = len(idlist)+1
		    contentEcho = (the1print +the2print +"  上一条信息为"+the3print+the4print)
		    cursor.execute('INSERT INTO dairy_db (content,id,dt) VALUES("%s",%d,"%s")'%(content[1:].encode('utf-8'),newid,time.strftime('%Y-%m-%d %H:%M:%S')))
	        elif content[0] in 'hH':
	            contentEcho ='''
			心流日记记录说明：心流状态采用主观评估，我们相信你的感觉。
			希望你当下评估你的心流状态，从0-9 给自己打个分数。
			按 x后直接加数字后直接加内容 来建立第一个心流档案。 
			在心流状态转变的时候，请再次评估，按 x后直接加数字后直接加内容 内容为你对情绪梗点说明。
			我们获得在数字之后的文字内容作为你个人对于心流状态的记录。
			如果希望查看你的心流日记内容，请按c
			'''
			
	        elif content[0] in 'xX':
		    #cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary WHERE fromUser =%s'%(fromUser))  #WHERE 不能用
		    cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary')
		    idtuple =cursor.fetchall()
		    idlist =list(idtuple)
		    listlen =len(idlist)
		    #timegap
		    i = listlen
		    time1 = '' #作为判断是第一次赋值的条件
		    while i > 0:
		        if idlist[i-1][0] == fromUser:
		            time1 =idlist[i-1][1].strftime('%Y-%m-%d %H:%M:%S')
			    flowState1 = idlist[i-1][2] # flowState is an int
		            break
			else:
		            i = i-1
		    time0 =time.strftime('%Y-%m-%d %H:%M:%S')
		    flowState0 = content[1]	
			
		    cursor.execute('INSERT INTO emotion_diary (fromUser, ct, flowStatement,content) VALUES("%s","%s",%d,"%s")'%(fromUser,time.strftime('%Y-%m-%d %H:%M:%S'), int(content[1]),content[2:].encode('utf-8')))
		    if time1 =='':
			contentEcho = ("真棒！恭喜你踏上记录心流日记的历程！你记录心流状态的时间是" +'%s'+"，你的心流状态是"+'%s'+"  你现在的感觉是："+"%s"+"，期待更棒的你！")%(time0,flowState0,content[2:])
		    else:
			contentEcho = ("你上一次记录心流状态的时间是" +'%s'+"，这段时间你的心流状态从"+"%d"+"转变到了"+'%s'+"\n"+"你现在的感觉是："+"%s")%(time1,flowState1,flowState0,content[2:]) 
			
		elif content[0] in'cC':
	            #from modulefuyong import prepare_emotionDiary
		    #idlist = prepare_emotionDiary(cursor)
		    cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary')
		    idtuple =cursor.fetchall()
		    idlist =list(idtuple)
		    listlen = len(idlist)
		    timelist =[]
	            flowlist =[]
		    contentlist =[]
		    i =listlen
		    while i > 0:
		        if idlist[i-1][0] == fromUser:
			    timelist.append(idlist[i-1][1].strftime('%Y-%m-%d %H:%M:%S'))
			    flowlist.append(idlist[i-1][2])
			    contentlist.append(idlist[i-1][3])
		            i = i-1
			    if len(timelist) >5:
			        break
			if timelist == []:
			    contentEcho =("请先开始记录心情日记喔！")
			else:
			    number = len(timelist)
			    contentEcho = "你之前的五条心流日记为 "
			    for j in range(number):
			        contentEcho +=("\n"+"%s"+" 心流值为"+ "%d"+" 梗点为"+"%s")%(timelist[j], flowlist[j],contentlist[j])
						
			
				
				
		
                else:
                    contentEcho = '''
			心流记录，请按 x后直接加数字后直接加内容 从0-9,一位 ；
			心流记录具体帮助 按h 获得具体指导和说明；
			如果希望查看你的心流日记内容，请按c
			吐槽日记，请按w后直接加输入内容；
			请输入少于50个的汉字。
			例子，w唱歌 表示吐槽 唱歌 
			x7听了轻音乐后心情舒畅 表示 记录心流值 为 7，
			此时听了轻音乐后心情舒畅。
			'''
	db.commit()
	db.close()
	return '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
	'''%(fromUser, toUser, createtime, contentEcho)