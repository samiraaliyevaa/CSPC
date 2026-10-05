import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, newton

# Equilibrium constant for H2 + I2 <=> 2HI
K = 50.0

def k_imbalance(x):
    return ((2*x)**2) / ((1 - x)**2) - K

# Derivative of k_imbalance for Newton's method
def dk_imbalance(x):
    return 8 * x / ((1 - x)**3)

# 1) Newton's method with derivative
x_newton = newton(k_imbalance, x0=0.6, fprime=dk_imbalance)

# 2) SLSQP method
res_slsqp = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method="SLSQP", bounds=[(0.01, 0.99)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium x (Newton): {x_newton:.4f}")
print(f"Equilibrium x (SLSQP):  {x_slsqp:.4f}")

nH2 = 1 - x_newton
nI2 = 1 - x_newton
nHI = 2 * x_newton

print(f"Equilibrium amounts: H2 = {nH2:.2f} mol, I2 = {nI2:.2f} mol, HI = {nHI:.2f} mol")

# Plotting
x_vals = np.linspace(0, 0.95, 100)
plt.figure(figsize=(7, 5))
plt.plot(x_vals, 1 - x_vals, label='H2 & I2 (Reactants)')
plt.plot(x_vals, 2 * x_vals, label='HI (Product)')
plt.axvline(x_newton, color='gray', linestyle='--', label=f'Equilibrium x ≈ {x_newton:.2f}')
plt.xlabel('Extent of Reaction (x)')
plt.ylabel('Amount (moles)')
plt.title('Chemical Equilibrium')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
print("Figure saved as equilibrium.png")