import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)
y = np.random.rand(20)

plt.scatter(x, y, c='blue', alpha=0.5, edgecolors='black')
plt.title('Диаграмма рассеяния случайно сгенерированных данных')
plt.xlabel('Массив Х')
plt.ylabel('МассивY')
plt.grid(True)
plt.show()