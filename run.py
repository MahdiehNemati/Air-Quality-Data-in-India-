import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-whitegrid')

city_day = pd.read_csv('kaggle/input/air-quality-data-in-india/city_day.csv').sort_values(by=['Date', 'City'])
