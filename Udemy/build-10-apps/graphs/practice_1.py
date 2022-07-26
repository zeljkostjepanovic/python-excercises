# importing pandas and bokeh libs
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

# load up some data
df = pd.read_csv("data.csv")
x = df["x"]
y = df["y"]

# create output file
output_file =("graph_1.html")

# create a figure object

f = figure()

# create plot
f.line(x,y)

# write plot in the figure object
show(f)