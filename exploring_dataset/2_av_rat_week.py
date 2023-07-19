from threading import main_thread
import justpy as jp
import pandas
from pytz import utc
from chart_def import chart_def

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews.", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.", classes="text-center q-pa-md")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.title.text = "Week"
    hc.options.title.text = "Average rating by week"
    hc.options.series[0].name = "Avg Rating on week"
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])

    return wp


jp.justpy(app)