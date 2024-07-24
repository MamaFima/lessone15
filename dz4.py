import pandas as pd
import numpy as np

data = {
    'Ученики': ['Иван Петров', 'Эдуард Иванов', 'Илья Резцов', 'Анна Разумова', 'Инна Ильина', 'Ольга Гердт',
                'Екатерина Дымова', 'Дарья Ланько', 'Денис Рощин', 'Петр Максимов'],
    'Алгебра': [5, 5, 4, 4, 4, 5, 3, 3, 3, 2],
    'Геометрия': [5, 5, 4, 4, 4, 4, 3, 3, 3, 3],
    'Физика': [4, 4, 4, 5, 5, 5, 3, 2, 3, 3],
    'Химия': [5, 5, 5, 5, 4, 4, 4, 4, 3, 3],
    'Русский язык': [5, 5, 4, 4, 4, 4, 4, 3, 3, 3]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Алгебра'].quantile(0.25)
Q3_math = df['Алгебра'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 для оценок по алгебре: {Q1_math}")
print(f"Q3 для оценок по алгебре: {Q3_math}")
print(f"IQR для оценок по алгебре: {IQR_math}")

std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
