%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<b>我的心情</b><p></p>
%for row in rows:
	<p>{{row[1][0]}}</p>
	<p>{{row[1][1]}}</p>
	<p>{{row[1][2]}}</p>
	<p>{{row[1][3]}}</p>	
%end

<p>我现在的心情:</p>
<form action='/imoodmap' method='GET'>
	<input name='newmood' type='text' size = '20' maxlength='40'/>
	<input name='moodlevel' type = 'text' size = '20' maxlength='40'/>
	<input name='story' type='text' size ='40' maxlength='40'/>
	<input value = '创建' name = 'save' type = 'submit'/>
</form>	
