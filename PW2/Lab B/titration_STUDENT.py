import numpy as np
import matplotlib.pyplot as plt

# Load titration data
data = np.genfromtxt('titration.csv', delimiter=',', skip_header=1)
V = data[:, 0]
pH = data[:, 1]

# Calculate slope (derivative)
slope = np.gradient(pH, V)
eq_idx = np.argmax(slope)
eq_V = V[eq_idx]

print(f"Equivalence Point Volume: {eq_V:.2f} mL")

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# pH curve
ax1.plot(V, pH, 'b.-', label='pH Curve')
ax1.axvline(eq_V, color='r', linestyle='--', label=f'Eq Point ({eq_V:.1f} mL)')
ax1.set_xlabel('Volume of Base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('pH Curve')
ax1.legend()
ax1.grid(True)

# Slope curve
ax2.plot(V, slope, 'g.-', label='dpH / dV')
ax2.axvline(eq_V, color='r', linestyle='--', label=f'Peak ({eq_V:.1f} mL)')
ax2.set_xlabel('Volume of Base (mL)')
ax2.set_ylabel('dpH / dV')
ax2.set_title('Slope (Derivative)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')
print("Figure saved as titration.png")