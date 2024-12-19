import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Заданная функция
def func(x):
    return np.sin(np.pi * x)

# Узлы интерполяции
def chebyshev_nodes(a, b, n):
    return np.array([np.cos((2 * i + 1) / (2 * n) * np.pi) for i in range(n)]) * (b - a) / 2 + (a + b) / 2

# Интерполяция Лагранжа
def lagrange_interpolation(x, y, x_vals):
    poly = lagrange(x, y)
    return poly(x_vals)

# Интерполяция кубическими сплайнами
def cubic_spline_interpolation(x, y, x_vals):
    spline = CubicSpline(x, y)
    return spline(x_vals)

# Интерполяция Лагранжа
x_vals = np.linspace(-1, 1, 500)
n_values = [5, 10]

plt.figure(figsize=(12, 8))
for n in n_values:
    # Равноотстоящие узлы
    x_eq = np.linspace(-1, 1, n)
    y_eq = func(x_eq)
    y_lagrange_eq = lagrange_interpolation(x_eq, y_eq, x_vals)

    # Чебышевские узлы
    x_cheb = chebyshev_nodes(-1, 1, n)
    y_cheb = func(x_cheb)
    y_lagrange_cheb = lagrange_interpolation(x_cheb, y_cheb, x_vals)

    plt.plot(x_vals, func(x_vals), label='Исходная функция', color='black')
    plt.plot(x_vals, y_lagrange_eq, label=f'Лагранж, равноотстоящие n={n}', linestyle='--')
    plt.plot(x_vals, y_lagrange_cheb, label=f'Лагранж, Чебышевские n={n}', linestyle=':')

plt.legend()
plt.title("Интерполяция Лагранжа")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# Кубический сплайн
plt.figure(figsize=(12, 8))
for n in n_values:
    # Равноотстоящие узлы
    x_eq = np.linspace(-1, 1, n)
    y_eq = func(x_eq)
    y_spline_eq = cubic_spline_interpolation(x_eq, y_eq, x_vals)

    plt.plot(x_vals, func(x_vals), label='Исходная функция', color='black')
    plt.plot(x_vals, y_spline_eq, label=f'Кубический сплайн, равноотстоящие n={n}', linestyle='--')

plt.legend()
plt.title("Интерполяция кубическим сплайном")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()