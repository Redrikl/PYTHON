import numpy as np
import matplotlib.pyplot as plt

# Задание 1. Вычисление площади треугольника методом Монте-Карло

# Границы треугольника
x1, y1 = 0, 0
x2, y2 = 25, 0
x3, y3 = 15, 10

# Количество случайных точек
N = 1000

# Генерация случайных точек в прямоугольнике, содержащем треугольник
x_min, x_max = 0, 25
y_min, y_max = 0, 10
x_random = np.random.uniform(x_min, x_max, N)
y_random = np.random.uniform(y_min, y_max, N)

# Проверка попадания точек внутрь треугольника
def is_inside_triangle(x, y):
    # Используем метод барицентрических координат
    denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    c = 1 - a - b
    return (a >= 0) & (b >= 0) & (c >= 0)

inside = is_inside_triangle(x_random, y_random)

# Количество точек внутри треугольника
M = np.sum(inside)

# Вычисление площади методом Монте-Карло
area_rectangle = (x_max - x_min) * (y_max - y_min)
area_triangle = (M / N) * area_rectangle

# Построение графика
plt.figure(figsize=(8, 8))
plt.scatter(x_random, y_random, c=inside, cmap='coolwarm', s=5)
plt.plot([x1, x2], [y1, y2], 'k-')
plt.plot([x2, x3], [y2, y3], 'k-')
plt.plot([x3, x1], [y3, y1], 'k-')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

print(area_triangle)