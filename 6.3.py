import numpy as np
import matplotlib.pyplot as plt
# Задание 3. Вычисление числа π методом Монте-Карло

# Параметры задачи
radius = 1  # Радиус круга
N = 1000  # Количество случайных точек

# Генерация случайных точек в квадрате [-1, 1] x [-1, 1]
x_random = np.random.uniform(-radius, radius, N)
y_random = np.random.uniform(-radius, radius, N)

# Проверка попадания точек в круг
inside_circle = x_random**2 + y_random**2 <= radius**2

# Количество точек внутри круга
M = np.sum(inside_circle)

#  Монте-Карло
area_square = (2 * radius) ** 2
pi_approx = (M / N) * area_square

# график
theta = np.linspace(0, 2 * np.pi, 500)
circle_x = radius * np.cos(theta)
circle_y = radius * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.scatter(x_random, y_random, c=inside_circle, cmap='coolwarm', s=5, label="Случайные точки")
plt.plot(circle_x, circle_y, color='black', label="Окружность радиуса 1")
plt.title("Метод Монте-Карло: Вычисление числа π")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.legend()
plt.grid()
plt.show()

pi_approx