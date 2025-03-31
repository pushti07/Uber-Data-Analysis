import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('UberDataset.csv')
df

df.info()

# Data Preprocessing
df['PURPOSE'].fillna('NOT', inplace = True)
df

df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors = 'coerce')

df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors = 'coerce')

df.info()

from datetime import datetime

df['date'] = pd.DatetimeIndex(df['START_DATE']).date
df['time'] = pd.DatetimeIndex(df['START_DATE']).hour

df.head()

df['day'] = pd.cut(x = df['time'], bins = [0, 10, 15, 19, 24], labels = ['Morning', 'Afternoon', 'Evening', 'Night'])
df

df.dropna(inplace = True)
df.shape

# Data Visualization
plt.figure(figsize = (20, 5))
plt.subplot(1, 2, 1)

sns.countplot(x = 'CATEGORY', data = df)
plt.xticks()

plt.subplot(1, 2, 2)
sns.countplot(x = 'PURPOSE', data = df)
plt.show()

sns.countplot(df['day'])

df.head()

df['Month'] = pd.DatetimeIndex(df['START_DATE']).month

month_label = {1.0 : 'Jan', 2.0 : 'Feb', 3.0 : 'Mar', 4.0 : 'Apr', 5.0 : 'May', 6.0 : 'June', 7.0 : 'July', 8.0 : 'Aug', 9.0 : 'Sept', 10.0 : 'Oct', 11.0 : 'Nov', 12.0 : 'Dec'}

df['Month'] = df.Month.map(month_label)

mon = df.Month.value_counts(sort = False)

df.head()

df = pd.DataFrame({
    'MONTHS' : mon.values,
    'VALUE COUNT' : df.groupby('Month', sort = False)['MILES'].max()
})

p = sns.lineplot(data = df)
p.set(xlabel = 'MONTHS', ylabel = 'VALUE COUNT')

df['DAY'] = df.START_DATE.dt.weekday

day_label = {
    0 : 'Mon', 1 : 'Tues', 2 : 'Wed', 3 : 'Thurs' , 4 : 'Fri', 5 : 'Sat', 6 : 'Sun'
}

df['DAY'] = df['DAY'].map(day_label)

day_label = df.DAY.value_counts()
sns.barplot(x = day_label.index, y = day_label)
plt.xlabel('Day')
plt.ylabel('Count')

sns.boxplot(df['MILES'])
sns.boxplot(df[df['MILES'] < 100]['MILES'])

sns.boxplot(df[df['MILES'] < 40]['MILES'])
sns.distplot(df[df['MILES'] < 40]['MILES'])
