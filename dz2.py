import pandas as pd

df = pd.read_csv('dz.csv')

df.fillna(0, inplace=True) #заменяем значения Nan  на 0
print(df)

group = df.groupby('City')['Salary'].mean()
print(group)
