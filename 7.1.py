import numpy as np
from scipy.integrate import quad
from scipy.special import erf

# Функция для численного интегрирования
def func(t):
    return (2 / np.sqrt(np.pi)) * np.exp(-t**2)

# Значения x
x_values = np.arange(0.0, 2.1, 0.1)

# Численное вычисление erf(x)
erf_values = [quad(func, 0, x)[0] for x in x_values]

# Точное значение erf(x)
exact_values = erf(x_values)

# Таблица результатов
print("x\tЧисленное erf(x)\tТочное erf(x)\tАбсолютная ошибка")
for x, num, exact in zip(x_values, erf_values, exact_values):
    print(f"{x:.1f}\t{num:.5f}\t\t{exact:.5f}\t\t{abs(num - exact):.5e}")