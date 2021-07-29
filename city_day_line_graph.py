import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.style.use('seaborn-whitegrid')

city_day = pd.read_csv('kaggle/input/air-quality-data-in-india/city_day.csv').sort_values(by=['Date', 'City'])

city_day.Date = city_day.Date.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
city_day = city_day.sort_values(by='Date')

city_day.corr().AQI.sort_values(ascending=False)

city_day['B_X_O3_NH3'] = city_day['Benzene'] + \
                         city_day['Xylene'] + city_day['O3'] + city_day['NH3']

city_day['ParticulateMatters'] = city_day['PM2.5'] + city_day['PM10']

corr_with_AQI = city_day.corr().AQI.sort_values(ascending=False)

most_polluted = city_day[['City', 'AQI', 'PM10', 'CO']].groupby(['City']).mean().sort_values(by='AQI', ascending=False)

plt.style.use('seaborn-whitegrid')
f, ax_ = plt.subplots(1, 3, figsize=(15, 15))

bar1 = sns.barplot(x=most_polluted.AQI,
                   y=most_polluted.index,
                   palette='Reds_r',
                   ax=ax_[0])

bar1 = sns.barplot(x=most_polluted.PM10,
                   y=most_polluted.index,
                   palette='RdBu',
                   ax=ax_[1])

bar1 = sns.barplot(x=most_polluted.CO,
                   y=most_polluted.index,
                   palette='RdBu',
                   ax=ax_[2])

titles = ['AirQualityIndex', 'ParticulateMatter10', 'CO']
for i in range(3):
    ax_[i].set_ylabel('')
    ax_[i].set_yticklabels(labels=ax_[i].get_yticklabels(), fontsize=14)
    ax_[i].set_title(titles[i])
    f.tight_layout()

f.show()
