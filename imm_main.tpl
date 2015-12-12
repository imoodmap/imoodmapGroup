
<!-- 任何问题，直接联系我whale-->
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>情绪心流输入</title>

    <!-- Bootstrap -->
    <script src="http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js"></script>
    <script src="http://cdn.bootcss.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <!-- 注意要修改href的地址！！whale -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="js/jquery.min.js" rel="stylesheet">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
    h3 {
     color: green;
	 font-family: courier;
	 font-size:200%;
	 text-align:center;
	 }
    body {
    font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
    font-size: 14px;
    line-height: 1.42857;
    color: #333;
    background-color: #E0AFAF;
    }
    </style>
  </head>
<body>



%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<b>我的心情</b><p></p>
%for row in rows:
	<p>{{row[1][0]}}</p>
	<p>{{row[1][1]}}</p>
	<p>{{row[1][2]}}</p>
	<p>{{row[1][3]}}</p>	
%end

<!-- 加入bootstrap，测试一下 whale-->
<p>我现在的心情:</p>	

  <form class="bs-example-fluid bs-example-form" role="form" action='/imoodmap' method='GET'>
  <div class="input-group ">
  <!-- 希望把情绪变成一个5-7 个选项的list,而不是漫天说自己的情绪，如insideout一样，后期处理方便-->
    <span class="input-group-addon">七彩情绪</span>
	<input name='newmood' type='text' class="form-control" />
	<span class="input-group-addon">心流状态</span>
	<input name='moodlevel' type = 'text' class="form-control"/>
	<span class="input-group-addon">你的故事</span>
	<input name='story' type='text' class="form-control"/> 
	<span class="input-group-addon">创建</span>
	<input value = 'click' name = 'save' type = 'submit' class="form-control"/>
  </div>
  </form>	
</body>
</html>