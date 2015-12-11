<b>我的心情</b><p></p>
%for row in rows:
	<b>{{row}}:</b> 
	<p></p>
%end

<p>我现在的心情:</p>
<form action='/imoodmap' method='GET'>
	<input value = '心情' name='newmood' type='text' size = '20' maxlength='40'/>
	<input value = '打分' name='moodlevel' type = 'text' size = '20' maxlength='40'/>
	<input value = '事件' name='story' type='text' size ='40' maxlength='40'/>
	<input value = '创建' name = 'save' type = 'submit'/>
</form>	
