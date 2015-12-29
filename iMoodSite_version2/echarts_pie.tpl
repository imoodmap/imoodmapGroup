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


          </div><!-- navbar-->
        </div> <!-- container -->
    </nav>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
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
                'echarts/chart/pie',
                'echarts/chart/funnel' // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
             // 基于准备好的dom，初始化echarts图表
            var myChart = ec.init(document.getElementById('main')); 
            var idx = 1;
 option = {
    timeline : {
        data : [
            'Now', '1-1', '1-2', '', '1-3',
            { name:'1-4', symbol:'emptyStar6', symbolSize:8 },
            '1-5', '1-6', '1-7', '1-8', '1-9',
            { name: '1-10', symbol:'star6', symbolSize:8 }
        ],
        label : {
            formatter : function(s) {
                return s.slice(0, 7);
            }
        }
    },
    options : [
        {
            title : {
                text: '情绪类型占比变化',
                subtext: ''
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                data:['恐惧','悲伤','愤怒','讨厌','快乐']
            },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {
                        show: true, 
                        type: ['pie', 'funnel'],
                        option: {
                            funnel: {
                                x: '25%',
                                width: '50%',
                                funnelAlign: 'left',
                                max: 1700
                            }
                        }
                    },
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie', 
                    center: ['50%', '45%'],
                    radius: '50%',
                    data:[
                        {value: 100+countdata[0]*100,  name:'恐惧'},
                        {value: 100+countdata[1]*100,  name:'悲伤'},
                        {value: 100+countdata[2]*100,  name:'愤怒'},
                        {value: 100+countdata[3]*100,  name:'讨厌'},
                        {value: 100+countdata[4]*100, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'情绪类型占比变化',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'浏览器（数据纯属虚构）',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'浏览器（数据纯属虚构）',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'浏览器（数据纯属虚构）',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'浏览器（数据纯属虚构）',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'浏览器（数据纯属虚构）',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'恐惧'},
                        {value: idx * 64  + 160,  name:'悲伤'},
                        {value: idx * 32  + 320,  name:'愤怒'},
                        {value: idx * 16  + 640,  name:'讨厌'},
                        {value: idx++ * 8  + 1280, name:'快乐'}
                    ]
                }
            ]
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
                           