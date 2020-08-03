from string import Template


def get_template():
    return Template(
        """<!DOCTYPE html>
<html style="height:100%;">

<head>
    <meta charset="utf-8">
    <title>${page_title}</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
</head>

<body style="height:98%;">
    <div id="main" style="height:100%;"></div>
    <script type="text/javascript">
        var option = {
            title: {text: '${figure_title}'},
            tooltip: {
                axisPointer: {type: "cross"},
                formatter: function (p) {
                    return p.data[0] + ", " + p.value[p.encode.y[0]]
                }
            },
            toolbox: {
                feature: {
                    dataZoom: {},
                    saveAsImage: {
                        excludeComponents: ['toolbox', 'dataZoom']
                    }
                }
            },
            legend: {},
            xAxis: [{'scale': true${xaxis_is_time}${x_axis_name}}],
            yAxis: [{${y_axis_name}}],
            animation: false,
            dataZoom: [{type: 'inside'}, {type: 'slider'}],
            dataset: ${dataset},
            series: ${series}
        };

        var myChart = echarts.init(document.getElementById('main')${theme});
        myChart.setOption(option);
    </script>
</body>

</html>
"""
    )
