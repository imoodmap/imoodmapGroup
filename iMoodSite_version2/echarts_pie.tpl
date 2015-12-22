<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>ECharts_pie</title>
</head>
<body>
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
        $("#test").hide();
        var countdata = $("counttypes").text();
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
            '2015-01-01', '2015-02-01', '2015-03-01', '2015-04-01', '2015-05-01',
            { name:'2015-06-01', symbol:'emptyStar6', symbolSize:8 },
            '2015-07-01', '2015-08-01', '2015-09-01', '2015-10-01', '2015-11-01',
            { name:'2015-12-01', symbol:'star6', symbolSize:8 }
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
                        {value: 545,  name:'恐惧'},
                        {value: 545,  name:'悲伤'},
                        {value: 545,  name:'愤怒'},
                        {value: 545,  name:'讨厌'},
                        {value: 545, name:'快乐'}
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

</body>
                           