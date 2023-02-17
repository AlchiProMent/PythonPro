# столбчатая диаграмма "аккуратного" формата
import plotly.express as px

# получить набор данных о медалях
df = px.data.medals_long()

fig = px.bar(df, x='nation', y='count', color='medal', title='Медали по странам')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
