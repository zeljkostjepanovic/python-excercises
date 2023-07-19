from main import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_str"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_str"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


fig1 = figure(x_axis_type='datetime', height=400, width=800)
fig1.yaxis.visible = False
fig1.title.text = "Motion Detection Times"
fig1.title.text_color = "black"

cds = ColumnDataSource(df)


hover = HoverTool(tooltips=[("Start", "@Start_str"), ("End", "@End_str")])
fig1.add_tools(hover)

q = fig1.quad(left="Start",right="End", bottom=0, top=1, color="green", source=cds)

output_file("motion_detect_graph.html")

show(fig1)