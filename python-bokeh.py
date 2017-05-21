
# coding: utf-8

# In[1]:

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.io import output_file, show , curdoc
from bokeh.layouts import row ,gridplot , column
from bokeh.charts import Histogram,Scatter, output_file, show
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool
from bokeh.models.widgets import Tabs, Panel


# In[2]:


import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show , curdoc

from bokeh.layouts import row ,gridplot , column

from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool
from bokeh.models.widgets import Tabs, Panel
df = pd.read_csv('652.csv', 
                 encoding = 'big5',
                 sep = ',',
                 header = 0)
df.columns = ['farm','year','1month','2month','3month','4month','5month','6month','7month','8month','9month','10month','11month','12month','empity']


df = df[df.farm=='蘿蔔(元/公斤)']
df.head(9)

p1 = figure(x_axis_label='年分',y_axis_label='1month',title = '蘿蔔一月價格圖')
p1.circle(df['year'],df['1month'], size=10)

p2 = figure(x_axis_label='年分',y_axis_label='2month',title = '蘿蔔二月價格圖')
p2.circle(df['year'],df['2month'], size=10)

p3 = figure(x_axis_label='年分',y_axis_label='3month',title = '蘿蔔三月價格圖')
p3.circle(df['year'],df['3month'], size=10)

p4 = figure(x_axis_label='年分',y_axis_label='4month',title = '蘿蔔四月價格圖')
p4.circle(df['year'],df['4month'], size=10)

p5 = figure(x_axis_label='年分',y_axis_label='5month',title = '蘿蔔五月價格圖')
p5.circle(df['year'],df['5month'], size=10)

p6 = figure(x_axis_label='年分',y_axis_label='6month',title = '蘿蔔六月價格圖')
p6.circle(df['year'],df['6month'], size=10)

p7 = figure(x_axis_label='年分',y_axis_label='7month',title = '蘿蔔七月價格圖')
p7.circle(df['year'],df['7month'], size=10)

p8 = figure(x_axis_label='年分',y_axis_label='8month',title = '蘿蔔八月價格圖')
p8.circle(df['year'],df['8month'], size=10)

p9 = figure(x_axis_label='年分',y_axis_label='9month',title = '蘿蔔九月價格圖')
p9.circle(df['year'],df['9month'], size=10)

p10 = figure(x_axis_label='年分',y_axis_label='10month',title = '蘿蔔十月價格圖')
p10.circle(df['year'],df['10month'], size=10)

p11 = figure(x_axis_label='年分',y_axis_label='11month',title = '蘿蔔十ㄧ月價格圖')
p11.circle(df['year'],df['11month'], size=10)

p12 = figure(x_axis_label='年分',y_axis_label='12month',title = '蘿蔔十二月價格圖')
p12.circle(df['year'],df['12month'], size=10)
#output_file('stock-df.html')




winter = Panel(child=row(p12, p1,p2), title='冬')
spring = Panel(child=row(p3, p4,p5), title='春')
summer = Panel(child=row(p6, p7,p8), title='夏')
fall = Panel(child=row(p9, p10,p11), title='秋')

tabs = Tabs(tabs=[spring, summer, fall, winter])
output_file('farmfalldata.html', mode='inline')
show(tabs)
#p2 = figure(x_axis_label='一月價格',y_axis_label='七月價格',title = '農產月份比較')

#p2.circle(df['1month'],df['7month'], size=10)
#show(p2)


# In[6]:

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import row ,gridplot , column

from bokeh.models.widgets import Tabs, Panel
df = pd.read_csv('Computers.csv', 
                 sep = ',',
                 header = 0)
pspeed = figure(x_axis_label='speed', y_axis_label='price', title = 'speed跟價格關係')
pspeed.circle(df['speed'], df['price'], size=10)
phd = figure(x_axis_label='hd', y_axis_label='price',title = 'hd跟價格關係')
phd.circle(df['hd'], df['price'], size=10)
pram = figure(x_axis_label='ram', y_axis_label='price', title = 'ram跟價格關係')
pram.circle(df['ram'], df['price'], size=10)
pscreen = figure(x_axis_label='screen', y_axis_label='price',title = 'screen跟價格關係')
pscreen.circle(df['screen'], df['price'], size=10)

#pcd = figure(x_axis_label='cd', y_axis_label='price',title = 'cd跟價格關係')
#pcd.circle(df['cd'],df['price'], size=10)
pads = figure(x_axis_label='ads',  y_axis_label='price',  title = 'ads跟價格關係')
pads.circle(df['ads'], df['price'], size=10)
#layout = gridplot([pspeed,phd],[pram,pscreen],[None,pads])

know = Panel(child=row(phd, pram,pscreen), title='know')
unknow = Panel(child=row(pspeed,pads), title='unknow')

tabs = Tabs(tabs=[know, unknow])
output_file('ComputerPricetabs.html', mode='inline')
show(tabs)


