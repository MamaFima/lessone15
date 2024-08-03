import numpy as np
import matplotlib.pyplot as plt

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Количество')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
