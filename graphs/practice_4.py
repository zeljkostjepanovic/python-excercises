#!/usr/bin/env python3

import pandas as pd
from bokeh.io import output_file,show
from bokeh.plotting import figure

p = figure(plot_width=500, plot_height=400)

p.title = "Earthquakes"
p.title.text_color = "Red"
p.title.text_font = "Sans"
p.title.text_font_style = "italic"

p.yaxis.minor_tick_line_color = "Yellow"

p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"

p.line([1,2,3,4,5],[6,7,8,9,10], line_width=2, color="red", alpha=0.5)
p.circle([i*2 for i in [1,2,3,4,5]],[5,6,4,3,6], size=8, color="olive", alpha=0.5)


output_file("scatter_plot.html")
show(p)