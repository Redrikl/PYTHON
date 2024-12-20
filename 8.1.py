import math
from scipy.special import erf


def newton_erf(target, initial_guess=0.5, tol=1e-10, max_iter=100):
    x = initial_guess
    for _ in range(max_iter):
        fx = erf(x) - target
        dfx = 2 / math.sqrt(math.pi) * math.exp(-x**2)
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("не сошёлся")

# erf(x) = 0.5
result_x = newton_erf(0.5)
print(result_x)
print(erf(result_x))
