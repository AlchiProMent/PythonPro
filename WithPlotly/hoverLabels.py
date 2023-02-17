# поведение всплывающих меток hover
import plotly.express as px

# получить данные по странам мира
df = px.data.gapminder().query("continent=='Oceania'")

# график изменения продолжительности жизни
fig = px.line(df,
              x='year',
              y='lifeExp',
              title='График изменения продолжительности жизни',
              color='country')
# добавить маркеры
fig.update_traces(mode='markers+lines', hovertemplate=None)
fig.update_layout(hovermode='x unified')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
#fig.write_image('01.png', width=1280, height=720)
