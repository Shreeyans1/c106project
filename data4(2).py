import plotly.express as px
import csv

with open("data4.csv")  as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Coffee in ml", y = "sleep in hours")
    fig.show()