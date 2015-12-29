<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>情绪日记记录 |imoodmap</title>

    <!-- Bootstrap -->

    <link href="./static/css/bootstrap.min.css" rel="stylesheet">
    <link href="./static/js/jquery.js" rel="stylesheet" type="text/css"> 
</head>
<body>
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

              <a  class="navbar-brand">情绪日记</a>
            </div>

          <div id="bs-example-navbar-collapse-1" class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">


               <li><a href="/index2">Back</a></li>
            </ul>


          </div><!-- navbar-->
        </div> <!-- container -->
    </nav>

<table class="table table-hover">
   <caption>情绪日记数据</caption>
   <thead>
      <tr>
      %for row in ["emotionType", "flowValue", "tpFeeling", "tireness", "diaryContent"]:
         <th> {{row}} </th>
      %end
      </tr>
   </thead>
   <tbody>

      %for line in data:
          <tr>

             <td>{{line[0]}}</td>
             <td>{{line[1]}}</td>
             <td>{{line[2]}}</td>
             <td>{{line[3]}}</td>
             <td>{{line[4]}}</td>
          </tr>
      %end
</tbody>.
</table>
</body>



    

