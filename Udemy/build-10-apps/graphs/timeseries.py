#!/usr/bin/env python3

"""
This script takes a CSV file or URL as an argument and 
it will produce a time series graph, if the provided 
csv has dates in the first column.

Several example links are provided below.
"""

import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from pick import pick
import sys

# Example links with CSV timeseries
# https://raw.githubusercontent.com/selva86/datasets/master/a10.csv
# https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv
# https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv
# https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-total-female-births.csv

output_file("timeseries.html")
try:
    csvfile = sys.argv[1]
    df1 = pd.read_csv(csvfile, parse_dates=[0])

    if df1.columns[0].lower() != "date" or df1.columns[0].lower() != "dates":
        print("Date column should be first.")
        exit(1)
    else:
        df2 = df1.rename(columns = {df1.columns[0] : "date" })
        


    title = "Please choose your Y axis: "
    options = df2.columns[1:]
    option, index = pick(options,title)

    f = figure(width=500, height=250, x_axis_type="datetime", sizing_mode="scale_both")
    f.line(df2['date'], df2[option], color = "red", alpha=0.5)
    show(f)

except:
    print(
    """Please provide a valid CSV that has Date as the first column. It can be either local or a URL."""
    )

