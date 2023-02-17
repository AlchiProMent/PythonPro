# агрегированные данные в виде столбчатой диаграммы
import plotly.express as px

# получить набор счетов из ресторана
df = px.data.tips()

# столбчатая диаграмма, отмечающая среднююю продолжительность жизни цветом
fig = px.histogram(df, x='sex', y='total_bill', color='smoker', barmode='overlay')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
