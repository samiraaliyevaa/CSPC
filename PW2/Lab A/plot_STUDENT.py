import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# --- Part 2: Read data and calculate derivatives ---
data = np.genfromtxt('freefall.csv', delimiter=',', skip_header=1)
t = data[:, 0]  # Time (s)
y = data[:, 1]  # Measured height / position (m)

# Compute velocity from position, then acceleration from velocity
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean Acceleration: {np.mean(a):.2f} m/s^2")

# --- Part 3: Noise evaluation ---
print(f"Acceleration Standard Deviation: {a.std():.2f}")

# --- Part 4: Integrating back ---
# Recover velocity from acceleration and position from velocity
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

# Calculate the maximum difference between recovered and original position
max_diff = np.max(np.abs(y - y_rec))
print(f"Max Position Difference: {max_diff:.4f} m")

# --- Part 5: Plotting ---
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
axs[0].plot(t, y, label='Original Position (y)')
axs[0].set_ylabel('Position (m)')
axs[0].legend()
axs[0].grid(True)

# Panel 2: Velocity
axs[1].plot(t, v, color='orange', label='Velocity (v)')
axs[1].set_ylabel('Velocity (m/s)')
axs[1].legend()
axs[1].grid(True)

# Panel 3: Acceleration
axs[2].plot(t, a, color='red', label='Acceleration (a)')
axs[2].axhline(-9.81, color='black', linestyle='--', label='Theoretical g (-9.81 m/s²)')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Acceleration (m/s²)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png')
print("Figure saved as motion.png")