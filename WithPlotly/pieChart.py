# круговая диаграмма
import plotly.express as px

# получить набор счетов из ресторана
df = px.data.tips()

# столбчатая диаграмма, отмечающая среднююю продолжительность жизни цветом
fig = px.pie(df, names='day', values='tip')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
