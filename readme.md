# install
```bash
python setup.py install
```

# usage

## Line
```python
from visxy import Line
p = Line()
```

## Scatter
```python
from visxy import Scatter
p = Scatter()
```

## 设置

### 设置标题
```python
p.set_page_title('page_title')
p.set_figure_title('figure_title')
```

### 设置色彩主题
选项有 ``default``（默认）, ``light`` 和 ``dark``
```python
p.set_theme('dark')
```

### 横轴设置为时间轴
如果横轴数值为时间戳或标准的时间格式字符串，可以设置横轴的属性为时间轴
```python
p.set_x_axis_as_time(True)
```

### 设置坐标轴标签
```python
p.set_x_axis_name('x')
p.set_y_axis_name('y')
```

## 绘图

### 添加数据
```python
# p.add_series(x_column, y_columns, legends)

# x_column 类型为list, 数值为 数据横坐标的list
# y_columns 类型为 list, 数值为 数据纵坐标的list, 或 多组数据组成的 list of list
# labels 类型为 str 或 多个数据组成的 list of str, 与 y_columns 的结构保持一致

p.add_series([10, 20], [[30, 40], [50, 10]], ["A", "B"])
```

### 设置数据可视化属性

#### line
* symbol: Optional[str] = "emptyCircle"
* symbol_size: int = 4
* line_color: Optional[str] = None
* line_width: int = 2
* line_type: str = "solid"
* line_opacity: float = 1


#### scatter
* symbol: str = "circle"
* symbol_size: int = 10

举例
```python
p.set_series_visual(symbol_size=10)
```
### 设置标记线

#### 添加纵线
```python
# p.add_markline_vertical(x_list, tag)

# x_list 类型为 float 或 多个数据组成的 list of float, 表示一条或多条竖线的横轴截距
# tag 标记线的文本标注

p.add_markline_vertical([13, 15, 17], '竖线组 1')
```

#### 添加横线
```python
# p.add_markline_horizontal(y_list, tag)

# y_list 类型为 float 或 多个数据组成的 list of float, 表示一条或多条横线的纵轴截距
# tag 标记线的文本标注

p.add_markline_horizontal([19, 20, 21], '横线组 2')
```

#### 设置标记线的可视化属性
```python
# p.set_markline_visual()

# 仅能设置刚添加的标记线的可视化属性

# tag: 记线的文本标注
# line_color: 标记线颜色
# line_type: 标记线的形状, 'dashed'(默认), 'solid' 或'dotted'
# start_symbol, end_symbol: 标记线起终点的标志
#      ["circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"]

p.set_markline_visual(line_type='solid')
```

## 渲染
```python
p.render()
```
