import numpy as np
from scipy.integrate import quad

# Определение функции
def f(x):
    if x <= 2:
        return np.exp(-x**2)
    else:
        return 4 - np.sin(16 * x)

# Составное интегрирование
def integrate_piecewise(f, intervals):
    result = 0
    for a, b in intervals:
        result += quad(f, a, b)[0]
    return result

# Интервалы интегрирования
intervals = [(0, 2), (2, 4)]

# Вычисление интеграла
integral_value = integrate_piecewise(f, intervals)

print(f"Значение интеграла: {integral_value:.5f}")