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
