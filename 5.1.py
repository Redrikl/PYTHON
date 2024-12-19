import numpy as np
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Исходные данные
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.0, 0.68, 0.44, 0.24, 0.12, 0.14])

# 1. Линейная функция y = a*x + b
def linear_func(x, a, b):
    return a * x + b

params_linear, _ = curve_fit(linear_func, x, y)
a_linear, b_linear = params_linear
print(f"Линейная функция: y = {a_linear:.4f} * x + {b_linear:.4f}")

# 2. Степенная функция y = a * x^b (преобразуем через логарифм)
def power_func(x, a, b):
    return a * x**b

params_power, _ = curve_fit(lambda x, a, b: a * x**b, x, y)
a_power, b_power = params_power
print(f"Степенная функция: y = {a_power:.4f} * x^{b_power:.4f}")

# 3. Показательная функция y = a * e^(b*x)
def exp_func(x, a, b):
    return a * np.exp(b * x)

params_exp, _ = curve_fit(exp_func, x, y)
a_exp, b_exp = params_exp
print(f"Показательная функция: y = {a_exp:.4f} * e^({b_exp:.4f} * x)")

# 4. Квадратичная функция y = a*x^2 + b*x + c
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

params_quad, _ = curve_fit(quadratic_func, x, y)
a_quad, b_quad, c_quad = params_quad
print(f"Квадратичная функция: y = {a_quad:.4f} * x^2 + {b_quad:.4f} * x + {c_quad:.4f}")

# Построение графиков
plt.scatter(x, y, color='red', label='Исходные данные')

# Графики функций
x_fit = np.linspace(min(x), max(x), 100)
plt.plot(x_fit, linear_func(x_fit, *params_linear), label='Линейная', linestyle='--')
plt.plot(x_fit, power_func(x_fit, *params_power), label='Степенная', linestyle='-.')
plt.plot(x_fit, exp_func(x_fit, *params_exp), label='Показательная', linestyle=':')
plt.plot(x_fit, quadratic_func(x_fit, *params_quad), label='Квадратичная', linestyle='-')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация методом наименьших квадратов')
plt.grid()
plt.show()
