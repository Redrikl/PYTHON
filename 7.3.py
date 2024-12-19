import numpy as np

# Определение функции f(x)
def f(x):
    if isinstance(x, (list, np.ndarray)):  # Для массивов
        return np.where(x <= 2, np.exp(x**2), 1 / (4 - np.sin(16 * np.pi * x)))
    else:  # Для одиночных значений
        return np.exp(x**2) if x <= 2 else 1 / (4 - np.sin(16 * np.pi * x))

# Реализация метода Симпсона вручную
def simpson_manual(f_values, x_values):
    n = len(x_values) - 1  # Количество отрезков
    if n % 2 == 1:
        raise ValueError("Метод Симпсона требует чётное количество отрезков.")
    h = (x_values[-1] - x_values[0]) / n  # Шаг
    s = f_values[0] + f_values[-1] + 4 * sum(f_values[1:n:2]) + 2 * sum(f_values[2:n-1:2])
    return h / 3 * s

x_1 = np.linspace(0, 2, 1001)
x_2 = np.linspace(2, 4, 1001)

# Вычисление значений функции
y_1 = f(x_1)
y_2 = f(x_2)

# Вычисление интегралов вручную методом Симпсона
integral_1_manual = simpson_manual(y_1, x_1)
integral_2_manual = simpson_manual(y_2, x_2)

# Сумма интегралов
total_integral_manual = integral_1_manual + integral_2_manual

# Вывод результатов
print(f"[0, 2]: {integral_1_manual}")
print(f"(2, 4]: {integral_2_manual}")
print(f"[0, 4]: {total_integral_manual}")