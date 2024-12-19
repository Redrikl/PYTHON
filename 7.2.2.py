from scipy.interpolate import CubicSpline
import numpy as np

# Функция для интегрирования
def f(x):
    return 4 / (1 + x**2)

# Метод сплайн-квадратур
def spline_quadrature(f, a, b, n):
    # Узлы интерполяции
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Построение сплайна
    spline = CubicSpline(x, y)

    # Вычисление интеграла через сплайн
    integral = 0
    for i in range(n):
        integral += spline.integrate(x[i], x[i+1])
    return integral

# Параметры
a, b = 0, 1
n_values = [8, 32, 128]
exact_pi = np.pi

print("n\tСплайн-квадратуры\tОшибка")
for n in n_values:
    spline_pi = spline_quadrature(f, a, b, n)
    error = abs(spline_pi - exact_pi)
    print(f"{n}\t{spline_pi:.5f}\t\t{error:.5e}")