from calendar import month
from threading import main_thread
import justpy as jp
import pandas
from pytz import utc
from chart_def_areaspline import chart_def

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')  
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews.", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.", classes="text-center q-pa-md")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.chart.type = 'spline'
    hc.options.xAxis.categories = list(month_average_crs.index)
    
    
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]] } for v1 in month_average_crs.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)