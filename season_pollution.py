import matplotlib.pyplot as plt

from run import city_day, corr_with_AQI

city_day['Year_Month'] = city_day.Date.apply(lambda x: x.strftime('%Y-%m'))

metrices = corr_with_AQI[corr_with_AQI > 0.5].index

df = city_day.groupby(['Year_Month']).sum().reset_index()

plt.style.use('seaborn-whitegrid')
fig, ax_ = plt.subplots(len(metrices), 1, figsize=(20, 50))

fig.tight_layout(pad=4)
for i, col in enumerate(metrices):
    x = df['Year_Month']
    y = df[col]
    ax_[i].plot_date(x, y, label=col, linestyle="-")
    ax_[i].set_xticklabels(df['Year_Month'], rotation=85)
    ax_[i].legend()

fig.show()