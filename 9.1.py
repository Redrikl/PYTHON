import math
import time

def erf_euler_alt(x_values, step=0.001):
    # Для каждого x считаем число шагов и суммируем значения функции под интегралом
    return [
        sum(
            (2 / math.sqrt(math.pi)) * math.exp(-(i * step)**2) * step
            for i in range(int(x / step))
        )
        for x in x_values
    ]

def erf_numeric_alt(x, n=1000):
    #  формула левых прямоугольников
    a, b = 0, x
    h = (b - a) / n
    return sum(
        (2 / math.sqrt(math.pi)) * math.exp(-(a + i * h)**2) * h
        for i in range(n)
    )

if __name__ == "__main__":
    # Задаём набор x
    x_values = [round(0.1 * i, 1) for i in range(21)]

    # Вычисления методом Эйлера
    start_euler = time.time()
    euler_results = erf_euler_alt(x_values)
    euler_time = time.time() - start_euler

    # Численное интегрирование
    start_numeric = time.time()
    numeric_results = [erf_numeric_alt(x) for x in x_values]
    numeric_time = time.time() - start_numeric

    # Вывод результатов
    print("x          Эйлер (erf)     Численный (erf)              Разница         Табличное (math.erf)")
    for x, e_val, n_val in zip(x_values, euler_results, numeric_results):
        diff = abs(e_val - n_val)
        print(f"{x:<5} | {e_val:<15}      {n_val:<15}    {diff:<12}    {math.erf(x):<15}")

    # Вывод времени
    print("\nВремя выполнения:")
    print(f"Метод Эйлера: {euler_time:.6f} секунд")
    print(f"Численное интегрирование: {numeric_time:.6f} секунд")