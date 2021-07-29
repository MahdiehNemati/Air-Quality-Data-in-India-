import datetime

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-whitegrid')

city_day = pd.read_csv('kaggle/input/air-quality-data-in-india/city_day.csv').sort_values(by=['Date', 'City'])
city_day.Date = city_day.Date.apply(lambda x : datetime.datetime.strptime(x, '%Y-%m-%d'))
city_day = city_day.sort_values(by = 'Date')
city_day.corr().AQI.sort_values(ascending = False)


corr_with_AQI = city_day.corr().AQI.sort_values(ascending = False)
