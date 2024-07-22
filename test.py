import pandas as pd

df = pd.read_csv('hh_tomsk.csv')

#df['Test'] = [new for new in range(20)] #добавляем столбец

#print(df)
#df.drop('Test', axis=1, inplace=True) #удаляем столбец

#print(df)

df.drop(2, axis=0, inplace=True) #удаляем строку

print(df)

