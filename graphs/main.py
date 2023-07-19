from bokeh.io import output_file,show
from bokeh.plotting import figure
from bokeh.layouts import column

a = [3, 7.5, 9]
b = [3, 6, 10]

output_file("graph.html")

graph1 = figure(title = "Triangles")
graph1.triangle(a, b)

graph2 = figure(title = "Circles")
graph2.circle(a, b)

show(column(graph1,graph2))