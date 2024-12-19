import numpy as np

# Функция для интегрирования
def f(x):
    return 4 / (1 + x**2)

# Метод прямоугольников
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b - h, n)
    return h * np.sum(f(x))

# Метод трапеций
def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return h * (np.sum(f(x)) - (f(a) + f(b)) / 2)

# Параметры
a, b = 0, 1
n_values = [8, 32, 128]

# Вычисление
print("n\tПрямоугольники\tТрапеции\tОшибка прямоугольников\tОшибка трапеций")
for n in n_values:
    rect_pi = rectangle_method(f, a, b, n)
    trap_pi = trapezoid_method(f, a, b, n)
    exact_pi = np.pi
    print(f"{n}\t{rect_pi:.5f}\t\t{trap_pi:.5f}\t\t{abs(rect_pi - exact_pi):.5e}\t\t{abs(trap_pi - exact_pi):.5e}")

## Сплайн-квадратуры обеспечивают более точное приближение интеграла