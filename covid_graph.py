import pandas as pd
import plotly.express as px
import datetime
import plotly.io as pio

start_date = datetime.datetime(year=2020, month=3, day=8)
data = pd.read_csv("us-counties.csv")
graph = px.line(data, x="date", y="cases", color="county", title="Cases by county")
graph.update_layout(xaxis_range=['2020-03-08','2020-03-26'])
graph.show()
pio.write_html(graph, file="index.html", auto_open=False)

