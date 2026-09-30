import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv (columns: time, count; skip the header row)
#         and split it into two arrays: t and observed
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)

# TODO 2: set N0 to the FIRST observed value, then build the analytical curve
#         analytical = N0 * exp(-LAMBDA * t)
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make a 1x2 subplot with SHARED x and y axes.
#         left panel : scatter of the observed data, titled "Observed data"
#         right panel: line plot of the analytical curve, titled "Analytical"
#         label the axes.
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

# Left panel: scatter of observed data
ax1.scatter(t, observed, color='blue', label='Observed')
ax1.set_title("Observed data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")

# Right panel: line plot of analytical curve
ax2.plot(t, analytical, color='red', label='Analytical')
ax2.set_title("Analytical")
ax2.set_xlabel("Time")

# TODO 4: save the figure as figure.png
plt.tight_layout()
plt.savefig("figure.png")