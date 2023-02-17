# столбчатая диаграмма
import plotly.express as px

# получить данные по странам мира
df = px.data.gapminder().query("country=='Australia'")

fig = px.bar(df,
             x='year',
             y='pop',
             title='График роста численности населения')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
