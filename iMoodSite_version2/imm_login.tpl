<!-- the page is studying from zhimaxin_login page url: http://www.iomooc.com/pages/login.html-->

<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>登陆页面 |imoodmap</title>

    <!-- Bootstrap -->
    <script src="http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js"></script>
    <script src="http://cdn.bootcss.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <link href="./static/css/bootstrap.min.css" rel="stylesheet">
    <link href="./static/js/jquery.min.js" rel="stylesheet">

    <style>
        .header {
            text-align: center;
        }

        .header h1 {
            font-size: 200%;
            color: #ECE8E8;
            margin-top: 30px;
        }

        .header p {
            font-size: 14px;
        }



        body {

            background-image: url('./images/login.png');
            background-repeat: no-repeat;
            background-position: 0px -50px;
            color: #D6CFCF;
        }
    </style>

</head>
<body style="zoom: 1;">
      <nav class="navbar navbar-inverse" role="navigation">
        <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>

              <a href=/show/all class="navbar-brand">情绪日记</a>
            </div>

          <div id="bs-example-navbar-collapse-1" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">

               <li><a href=/diarymap>日记回顾</a></li>
              <li><a href=/imoodmap>打气筒</a></li>


               <li ><a href=/submit>社区互动</a></li>
               <li><a href=/about_us>关于我们</a></li>


          </div><!-- navbar-->
        </div> <!-- container -->
    </nav>
<div class="backgroud">
    <div class="header">

            <h1>imoodmap</h1>

            <h3 style="color: grey">擦干雨水和泪水，继续向着梦想</h3> <h3 style="color: white">Keep Moving<br/></h3>


    </div>
</div>

  <form action="/login" method="POST" class="form-horizontal-fluid" >
    <p id="alertContent"> {{alertContent}}</p>
    <div class="form-group">
      <label for="name" class="col-sm-2 control-label">称呼</label>
      <div class="col-sm-10">
         <input type="name" class="form-control" id="name" name="studentname" 
            placeholder="请输入你的称呼">
      </div>
    </div>
    <div class="form-group">
      <label for="password"   class="col-sm-2 control-label">密码</label>
      <div class="col-sm-10">
         <input type="password" class="form-control"  name="password"
            placeholder="请输入密码">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
         <div class="checkbox">
            <label>
               <input type="checkbox"> 请记住我
            </label>
         </div>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
         <button type="submit" class="btn btn-default">登录</button>
      </div>
    </div>
  </form>
</body>