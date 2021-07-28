
# Sum of pollution
import plotly.express as px
import pandas

from run import city_day

df = city_day.drop(columns = ['Date', 'AQI_Bucket', 'AQI']).groupby('City').sum().reset_index()
fig = px.treemap(pandas.melt(df, id_vars = 'City'), path=['City','variable'],
                 values=pandas.melt(df, id_vars = 'City')['value'],
                 title = 'Cities and the proportion of pollution in each')
fig.show()