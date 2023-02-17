# бары цвета из градиентного набора
import plotly.express as px

# получить данные по странам мира
df = px.data.gapminder().query("country=='Australia'")

# столбчатая диаграмма, отмечающая среднююю продолжительность жизни цветом
fig = px.bar(df, x='year', y='pop', color='lifeExp',
             labels={'pop': 'Численность населения', 'lifeExp': 'Средняя продолжительность жизни'})

# показать в браузере
fig.write_html('graph.html', auto_open=True)
