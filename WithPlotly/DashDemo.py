# демонстрация интерактивной работы с графиком через Dash
import plotly.express as px
from dash import Dash, html, dcc, Output, Input

# создать приложение
app = Dash(__name__)

# создать DOM
app.layout = html.Div([
    html.H1('Анализ ресторанных чеков'),
    dcc.Graph(id='graph'),
    html.P('В разрезе:'),
    dcc.Dropdown(id='names', options=['smoker', 'day', 'time', 'sex'], value='smoker'),
    html.P('По значению:'),
    dcc.Dropdown(id='values', options=['total_bill', 'tip', 'size'], value='total_bill')
])

@app.callback(
    # выходноц интерфейс
    Output('graph', 'figure'),
    # входные интерфейсы
    Input('names', 'value'),
    Input('values', 'value'))
def generate_cart(names, values):
    df = px.data.tips()
    fig = px.pie(df, names=names, values=values)
    return fig

# запустить сервер
app.run_server(debug=True)
