from bokeh.io import output_file,show
from bokeh.plotting import figure
import pandas


url = "https://github.com/pythonizing/data/raw/master/verlegenhuken.xlsx"
df1 = pandas.read_excel(url)
output_file("temps_pressures.html")

f = figure()

f.circle(df1["Temperature"]/10, df1["Pressure"]/10, size = 1)
f.title = "Temperature and Air Pressure"
f.xaxis.axis_label = "Temperature (°C)"
f.yaxis.axis_label = "Pressure (hPa)"

show(f)