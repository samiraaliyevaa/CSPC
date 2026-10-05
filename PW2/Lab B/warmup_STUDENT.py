import numpy as np
from scipy.optimize import minimize, newton

# --- Part 2A: Simple Convex Function f(x) = (x-3)^2 + 1 ---
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

# 1) Gradient Descent (by hand)
x_gd = 0.0
alpha = 0.1
for _ in range(100):
    x_gd -= alpha * df(x_gd)

# 2) Newton's Method
x_newton = newton(df, x0=0)

# 3) SLSQP Minimizer
res_slsqp = minimize(f, x0=0, method="SLSQP")

print("=== Part 2A: f(x) = (x-3)^2 + 1 ===")
print(f"Gradient Descent: x = {x_gd:.4f}")
print(f"Newton Method:    x = {x_newton:.4f}")
print(f"SLSQP Minimize:   x = {res_slsqp.x[0]:.4f}")


# --- Part 2B: Harder Landscape g(x) = x^4 - 3x^2 + x + 5 ---
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

print("\n=== Part 2B: g(x) = x^4 - 3x^2 + x + 5 ===")
for x0 in [0, 2]:
    print(f"\nStarting point x0 = {x0}:")
    
    # Gradient Descent
    x_g_gd = float(x0)
    for _ in range(200):
        x_g_gd -= 0.01 * dg(x_g_gd)
    print(f"  Gradient Descent: x = {x_g_gd:.4f}")

    # Newton's Method
    try:
        x_g_newton = newton(dg, x0=x0)
        curv = d2g(x_g_newton)
        status = "Minimum" if curv > 0 else "Maximum"
        print(f"  Newton Method:    x = {x_g_newton:.4f} (g'' = {curv:.2f} -> {status})")
    except Exception as e:
        print("  Newton Method:    An error occurred")

    # SLSQP
    res_g_slsqp = minimize(g, x0=x0, method="SLSQP")
    print(f"  SLSQP Minimize:   x = {res_g_slsqp.x[0]:.4f}")