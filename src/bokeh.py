#!/usr/bin/env python
# coding: utf-8

# In[1]:


%load_ext autoreload

# In[2]:


%reset -f

# In[3]:


from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

output_notebook()

# In[4]:


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title="simple line example", 
    x_axis_label='x', 
    y_axis_label='y',
    width=500,
    height=500
)
p.line(x, y);

show(p)

# In[5]:


x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

p = figure(
    tools='pan, box_zoom, reset, save',
    y_axis_type="log",
    y_range=[0.001, 10**11],
    title='log axis example',
    x_axis_label='sections',
    y_axis_label='particles'
)
p.line(x, x, legend_label="y=x")
p.circle(x, x, legend_label="y=x", fill_color="white", size=8)

p.line(x, y0, legend_label="y=x^2", line_width=3)

p.line(x, y1, legend_label="y=10^x", line_color="red")
p.circle(x, y1, legend_label="y=10^x", fill_color="red", line_color="red", size=6)

p.line(x, y2, legend_label="y=10^x^2", line_color="orange", line_dash="4 4")

show(p)

# # Linked panning
# 
# Where changing the range of one plot causes others to update by sharing range objects between the plots.

# In[6]:


import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

N = 100
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

s1 = figure(
    width=250,
    plot_height=250,
    title=None
)
s1.circle(x, y0, size=10, color='navy', alpha=.5);

s2 = figure(
    width=250,
    height=250,
    x_range=s1.x_range,
    y_range=s1.y_range,
    title=None
)
s2.triangle(x, y1, size=10, color='firebrick', alpha=.5);

s3 = figure(
    width=250,
    height=250,
    x_range=s1.x_range,
    title=None
)
s3.square(x, y2, color='olive', alpha=.5)

p = gridplot([[s1, s2, s3]], toolbar_location=None)
show(p)

# # Linked brushing
# 
# A selection on one plot causes a selection to update on other plots. This example shares the `ColumnDataSource` between two plots. 

# In[7]:


import numpy as np
from bokeh.plotting import *
from bokeh.models import ColumnDataSource

N = 300
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = 'pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select'

G_W = 500
G_H = 350

left = figure(
    tools=TOOLS,
    width=G_W,
    height=350,
    title=None
)
left.circle('x', 'y0', source=source)

right = figure(
    tools=TOOLS,
    width=G_W,
    height=350,
    title=None
)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])
show(p)

# # Datetime axes

# In[18]:


import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size) / float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

p = figure(
    plot_width=800, 
    plot_height=400, 
    x_axis_type="datetime",
)
p.circle(aapl_dates, aapl, size=4, color='darkgrey', alpha=.2, legend_label='close')
p.line(aapl_dates, aapl_avg, color='navy', legend_label='avg')

p.title.text = 'AAPL One-Month Average'
p.legend.location = 'top_left'
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.ygrid.band_fill_color = 'red'
p.ygrid.band_fill_alpha = .1

show(p)

# # Bars and rectangles

# In[9]:


import pandas as pd

df = pd.DataFrame({
    'group':['a', 'b'],
    'size':[25, 30]
})
df.sort_values(by=['size'], ascending=False, inplace=True)

source = ColumnDataSource(df)
p = figure(
    plot_width=500, 
    plot_height=500, 
    x_range=['a', 'b']  # Use categorical data (can filter here)
)
p.vbar(x='group', top='size', width=.5, color='firebrick', source=source)
show(p)

# # Filtering

# In[10]:


from bokeh.layouts import gridplot
from bokeh.models import BooleanFilter, CDSView, ColumnDataSource
from bokeh.plotting import figure, show

np.random.seed(42)

df = pd.DataFrame({
    'x':np.random.randint(0, 10, 15),
    'y':np.random.randint(0, 10, 15)
})


source = ColumnDataSource(df)
booleans = [True if y_val > 7 else False for y_val in source.data['y']]
view = CDSView(source=source, filters=[BooleanFilter(booleans)])
TOOLS = ['box_select', 'hover', 'reset']
p = figure(
    plot_height=300,
    plot_width=300,
    tools=TOOLS
)
p.circle(x='x', y='y', size=10, hover_color='red', source=source)

p_filtered = figure(
    plot_height=300,
    plot_width=300,
    tools=TOOLS,
    x_range = p.x_range,
    y_range = p.y_range
)
p_filtered.circle(x='x', y='y', size=10, hover_color='red', source=source, view=view)

p.title.text = 'Non Filtered Data'
p_filtered.title.text = 'Filtered Data'
show(gridplot([[p, p_filtered]]))

# # Stacked bar charts

# In[11]:


fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

p = figure(
    x_range=fruits,
    plot_height=250,
    title='Fruit counts by year',
    toolbar_location=None,
    tools=""
)
p.vbar_stack(years, x='fruits', width=.9, color=colors, source=data, legend_label=years)

p.y_range.start = 0
p.x_range.range_padding = .1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = 'top_left'
p.legend.orientation = 'horizontal'

show(p)

# In[12]:


from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]

exports = {'fruits' : fruits,
           '2015'   : [2, 1, 4, 3, 2, 4],
           '2016'   : [5, 3, 4, 2, 4, 6],
           '2017'   : [3, 2, 4, 4, 5, 3]}
imports = {'fruits' : fruits,
           '2015'   : [-1, 0, -1, -3, -2, -1],
           '2016'   : [-2, -1, -3, -1, -2, -2],
           '2017'   : [-1, -2, -1, 0, -2, -2]}

p = figure(
    y_range=fruits, 
    plot_height=250,
    x_range=(-16, 16), 
    title='Fruit import / export by year',
    tools="hover", 
    tooltips="@$name"
)

p.hbar_stack(
    years, 
    y='fruits', height=.9, color=GnBu3, 
    source=ColumnDataSource(exports),
    legend_label=["%s exports" % x for x in years]
)
p.hbar_stack(
    years, 
    y='fruits', height=.9, color=OrRd3, 
    source=ColumnDataSource(imports),
    legend_label=["%s imports" % x for x in years]
)

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

show(p)

# # Hover Tools
# 
# Bokeh automatically sets the `name` property for each layer in the bar stack to be the value of the stack column for that layer. This name value is accessible to hover tools via the `$name` special variable.
# 
# The hover variable `@$name` can be used to look up the values from the stack column for each layer.
# 
# - `$name`: Name of the current individual chunk of bar stack (the value of the stacking variable)
# - `@fruits`: Name of the current bar variable (the same for all chunks of the same bar)
# - `@$name`: Get the current value of the count for each individual stack

# In[19]:


from bokeh.io import output_file, show
from bokeh.plotting import figure

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

p = figure(
    x_range=fruits, 
    plot_height=250, 
    title="Fruit Counts by Year",
    toolbar_location=None, 
    tools="hover", 
    tooltips="$name @fruits: @$name"
)
p.vbar_stack(years, x='fruits', width=0.9, color=colors, source=data,
             legend_label=years)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
