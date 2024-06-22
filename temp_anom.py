from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dvd1587/dash_temp_anomalies/main/annual-temperature-anomalies.csv')

app = Dash()

app.layout = [
    html.H1(children='Annual Temperature Anomalies Time-Series (1991-2020 mean in '+chr(176)+'C)', style={'textAlign':'center'}),
    dcc.Dropdown(df.Entity.unique(), 'India', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.Entity==value]
    return px.line(dff, x='Year', y='Temperature anomaly')

