import math

import numpy as np
import matplotlib.pyplot as plt
# Задание 2. Вычисление интеграла методом Монте-Карло

# Границы интегрирования
a, b = 0, 5

# Функция для интегрирования
def f(x):
    return np.sqrt(29-15*(np.cos(x)**2))

# Количество случайных точек
N = 1000

# Генерация случайных точек в пределах [a, b]
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Вычисление точек под графиком функции
y_func = f(x_random)
under_curve = y_random <= y_func

# Количество точек под кривой
M = np.sum(under_curve)

# Вычисление интеграла методом Монте-Карло
area_rectangle = (b - a) * f(b)
integral_value = (M / N) * area_rectangle

# Построение графика
x_vals = np.linspace(a, b, 500)
plt.figure(figsize=(8, 6))
plt.plot(x_vals, f(x_vals), label="Функция $f(x) = x^2$", color='blue')
plt.scatter(x_random, y_random, c=under_curve, cmap='coolwarm', s=5, label="Случайные точки")
plt.legend()
plt.title("Метод Монте-Карло: Вычисление интеграла")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

print(integral_value)
