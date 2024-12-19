import numpy as np
import matplotlib.pyplot as plt
# Задание 4. Вычисление площади фигуры, заданной в полярных координатах

# Заданная функция в полярных координатах
def r(theta):
    return 1 + np.cos(theta)

# Границы по θ
theta_min, theta_max = 0, 2 * np.pi

# Количество случайных точек
N = 1000

# Определение прямоугольника, охватывающего фигуру
r_max = 2  # Максимальное значение r (1 + max(cos(theta)))

# Генерация случайных точек в полярных координатах
theta_random = np.random.uniform(theta_min, theta_max, N)
r_random = np.random.uniform(0, r_max, N)

# Проверка попадания точек внутрь фигуры
inside_figure = r_random <= r(theta_random)

# Количество точек внутри фигуры
M = np.sum(inside_figure)

# Вычисление площади методом Монте-Карло
area_rectangle = (theta_max - theta_min) * r_max
area_figure = (M / N) * area_rectangle

# Построение графика
theta_vals = np.linspace(theta_min, theta_max, 500)
x_vals = r(theta_vals) * np.cos(theta_vals)
y_vals = r(theta_vals) * np.sin(theta_vals)

# Случайные точки в декартовой системе координат
x_random = r_random * np.cos(theta_random)
y_random = r_random * np.sin(theta_random)

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label="Граница фигуры", color="black")
plt.scatter(x_random, y_random, c=inside_figure, cmap="coolwarm", s=5, label="Случайные точки")
plt.title("Метод Монте-Карло: Вычисление площади фигуры в полярных координатах")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.legend()
plt.grid()
plt.show()

area_figure





