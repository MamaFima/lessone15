import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

df.fillna(0, inplace=True) #заменяем значения Nan  на 0
print(df)

#df.dropna(inplace=True) #удаляем полностью строки с Nan

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

#df.to_csv('outpu.csv', index=False) #сохранение измененного датафрейма


