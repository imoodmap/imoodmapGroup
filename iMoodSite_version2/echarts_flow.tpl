<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>情绪统计图 |imoodmap</title>

    <!-- Bootstrap -->

    <link href="./static/css/bootstrap.min.css" rel="stylesheet">
    <link href="./static/js/jquery.js" rel="stylesheet" type="text/css"> 
</head>
<body>

    <p id="test"> 情绪日记 </p>
    <p id="counttypes">{{countTypes}}</p>
    <div id="main" style="height:600px "></div>
    <!-- ECharts单文件引入 -->
    <script src="http://echarts.baidu.com/build/dist/echarts.js"></script>
    <script src="http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js"></script>  
    <script type="text/javascript">
        //传输外部数据jquery
        var outdata = $("#test").text();

        var countdata =$("#counttypes").text().replace(/[\[\]]/g,"").split(","); //正则表达式获取array
        $("#counttypes").hide();

        // 路径配置
        require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });
        require(
            [
                'echarts',
                'echarts/chart/line' // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
             // 基于准备好的dom，初始化echarts图表
            var myChart = ec.init(document.getElementById('main')); 
            var idx = 1;


        option = {
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:['心流值']
            },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : ['0','1','2','3','4','5','6','7','8','9']
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [

                {
                    name:'心流值',
                    type:'line',
                    stack: '总量',
                    itemStyle: {normal: {areaStyle: {type: 'default'}}},
                    data: countdata
                }
            ]
            };


  myChart.setOption(option); 
            }
        );


</script>
<br>
<div class="col-lg-12 text-center">

<a href="/index2" class="page-scroll btn btn-xl" id="backHome">返回</a>
</div>

</body>