import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- Part 3: Read data and fit reaction rate ---
# Load kinetics data (time, concentration)
data = np.genfromtxt('kinetics.csv', delimiter=',', skip_header=1)
t = data[:, 0]
C_meas = data[:, 1]

# Set initial concentration C0 to the first measured value
C0 = C_meas[0]

# Define total squared error function
def total_error(k):
    C_pred = C0 * np.exp(-k * t)
    return np.sum((C_meas - C_pred)**2)

# Minimize error to find optimal rate constant k
res = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]

print(f"Fitted rate constant k: {fitted_k:.4f}")

# --- Plotting ---
plt.figure(figsize=(7, 5))
plt.scatter(t, C_meas, color='red', label='Measured Data')

t_fine = np.linspace(t.min(), t.max(), 100)
plt.plot(t_fine, C0 * np.exp(-fitted_k * t_fine), label=f'Fitted Curve (k ≈ {fitted_k:.2f})')

plt.xlabel('Time (s)')
plt.ylabel('Concentration')
plt.title('Reaction Kinetics Fitting')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
print("Figure saved as kinetics.png")