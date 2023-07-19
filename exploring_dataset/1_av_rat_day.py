from ast import parse
from threading import main_thread
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
from chart_def import chart_def

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews.", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.", classes="text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average rating by day"
    hc.options.series[0].name = "Avg Rating on Day"
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    return wp


jp.justpy(app)