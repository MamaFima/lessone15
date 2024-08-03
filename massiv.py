import numpy as np
import matplotlib.pyplot as plt

#a = np.array([1, 2, 3, 4]) #Создаем массив
#a = np.ones((2, 5))#массив заполненный единицами
#a = np.zeros((3, 3))#массив заполненный нулями
#a = np.random.random((4, 5))#массив заполненный рандомными числами до 1
#a = np.arange(0, 10, 2)#массив заполненный последовательностью чисел (в круглых скобках начало, конец и шаг)
#a = np.linspace(0, 12, 10)
#print(a)

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("ось х")
plt.ylabel("ось у")
plt.title("График функции у = х**2")
plt.grid(True)
plt.show()



