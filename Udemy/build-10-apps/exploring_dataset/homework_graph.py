import justpy as jp
import pandas
from chart_def import chart_def

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = pandas.Categorical(data['Timestamp'].dt.strftime('%A'), categories=weekdays, ordered=True)

weekday_average = data.groupby(['Weekday']).mean()

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews.", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.", classes="text-center q-pa-md")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(weekday_average.index)
    hc.options.xAxis.title.text = "Weekday"
    
    
    hc_data = [{"name": v1, "data": [v2 for v2 in weekday_average[v1]] } for v1 in weekday_average.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)