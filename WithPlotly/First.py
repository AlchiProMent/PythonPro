# знакомство с Plotly
import plotly.express as px
from pandas import DataFrame

# данные для визуализации
df = DataFrame({'data_x': [1, 2, 3, 4, 5, 6, 7]}, index=['Point1','Point2','Point3','Point4','Point5','Point6','Point7'])
# возвести в куб
df['data_y'] = df['data_x'] ** 3
# добавить подписи точек
df['signatures'] = ['1 в кубе',
                    '2 в кубе',
                    '3 в кубе',
                    '4 в кубе',
                    '5 в кубе',
                    '6 в кубе',
                    '7 в кубе']
# сформировать график
fig = px.line(df,
              x='data_x',
              y='data_y',
              title='График квадратов значений',
              hover_name=df.index,
              width=1280,
              height=720,
              text='signatures')
fig.update_traces(textposition='bottom right')
# показать график
#fig.show()
# в HTML
fig.write_html('graph.html', auto_open=True)