import numpy as np
import math
from scipy.special import erf
def erf(x, n=1000):
    def integrand(t):
        return (2 / np.sqrt(np.pi)) * np.exp(-t**2)
    
    a, b = 0, x 
    h = (b - a) / n
    integral = 0.5 * (integrand(a) + integrand(b))
    for i in range(1, n):
        integral += integrand(a + i * h)
    return h * integral

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
