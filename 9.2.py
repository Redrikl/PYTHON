import time

class LotkaVolterraSolver:
    """
    Система:
    dr/dt = 2r - alpha*r*f
    df/dt = -f + alpha*r*f
    """
    def __init__(self, alpha, r_init, f_init, dt=0.01, t_max=100):
        self.alpha = alpha
        self.r = r_init
        self.f = f_init
        self.dt = dt
        self.t_max = t_max
        self.history = []

    def run(self, stop_if_extinct=True, both_extinct_check=False):
        t = 0.0
        self.history = [(t, self.r, self.f)]

        while t < self.t_max:
            if stop_if_extinct:
                # Проверка на вымирание одного или обоих видов
                if both_extinct_check:
                    if self.r < 1 and self.f < 1:
                        print("Оба вида вымерли - расчёт остановлен.")
                        break
                else:
                    if self.r < 1 or self.f < 1:
                        print("Один из видов вымер - расчёт остановлен.")
                        break

            dr = (2 * self.r - self.alpha * self.r * self.f) * self.dt
            df = (-self.f + self.alpha * self.r * self.f) * self.dt
            self.r += dr
            self.f += df
            t += self.dt
            self.history.append((t, self.r, self.f))

        return self.history

class PopulationAnalysis:
    """
    Класс для анализа результатов.
    """
    @staticmethod
    def print_overview(data, show_steps=10):
        if not data:
            print("Нет данных для отображения.")
            return
        step = max(len(data) // show_steps, 1)
        header = f"{'Time':>8} {'Rabbits':>12} {'Foxes':>12}"
        separator = "-" * len(header)
        print(header)
        print(separator)
        for i, (t, r, f) in enumerate(data):
            if i % step == 0:
                print(f"{t:8.2f} {r:12.4f} {f:12.4f}")

    @staticmethod
    def final_state(data):
        if not data:
            return (0,0)
        _, r_final, f_final = data[-1]
        return r_final, f_final

    @staticmethod
    def analyze(alpha, r0, f0, dt=0.01, t_end=100, stop_if_extinct=True, both_extinct_check=False):
        solver = LotkaVolterraSolver(alpha, r0, f0, dt, t_end)
        results = solver.run(stop_if_extinct=stop_if_extinct, both_extinct_check=both_extinct_check)
        r_final, f_final = PopulationAnalysis.final_state(results)

        print("\n-------------------------------")
        print(f"Параметры: alpha={alpha}, r0={r0}, f0={f0}")
        PopulationAnalysis.print_overview(results, show_steps=10)
        print(f"\nИтог: r={r_final:.4f}, f={f_final:.4f}")
        if r_final < 1:
            print("Кролики вымерли.")
        if f_final < 1:
            print("Лисы вымерли.")
        if r_final < 1 and f_final < 1:
            print("Оба вида вымерли.")
        print("-------------------------------\n")

if __name__ == "__main__":
    alpha = 0.01

    # Различные начальные условия
    initial_sets = [(2, 3), (15, 22), (1000, 2000)]
    print("Анализ системы для разных начальных условий:")
    for (r_init, f_init) in initial_sets:
        PopulationAnalysis.analyze(alpha, r_init, f_init, dt=0.01, t_end=100)

    # Поиск условий для вымирания лис
    print("Проверка начальных условий на вымирание лис:")
    PopulationAnalysis.analyze(0.01, 10, 2, dt=0.01, t_end=150)

    # Условия для вымирания обоих видов
    print("Проверка начальных условий на вымирание обоих видов:")
    # Здесь включаем проверку both_extinct_check=True
    PopulationAnalysis.analyze(0.01, 2, 2, dt=0.01, t_end=150, both_extinct_check=True)




