from run import city_day, corr_with_AQI
import matplotlib.pyplot as plt
city_day['Year_Month'] = city_day.Date.apply(lambda x : x.strftime('%Y-%m'))
df = city_day.groupby(['Year_Month']).sum().reset_index()

# let's only see those that are important to the AQI
# otherwise we will have a messy plot

metrices = corr_with_AQI[corr_with_AQI>0.5].index
plt.style.use('seaborn-whitegrid')
fig, ax_ = plt.subplots(figsize=(20, 10))

df = city_day.groupby(['Year_Month']).sum().reset_index()

for col in metrices:
    x = df['Year_Month']
    y = df[col]

    ax_.plot_date(x, y, label=col, linestyle="-")

ax_.set_xticklabels(df['Year_Month'], rotation=85)
ax_.legend()

fig.show()