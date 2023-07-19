import pandas
from bokeh.io import output_file,show
from bokeh.plotting import figure


output_file = ("graph_1.html")
csv_url = "https://pythonizing.github.io/data/bachelors.csv"



df1 = pandas.read_csv(csv_url)
f = figure()
f.title.text="Women Engineering degrees by year"
f.yaxis.minor_tick_line_color=None
f.xaxis.minor_tick_line_color=None
f.xaxis.axis_label="Year"
f.yaxis.axis_label="Engineering degrees"

f.line(df1["Year"],df1["Engineering"])

show(f)