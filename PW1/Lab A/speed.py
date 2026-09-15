import time
import numpy as np
import decay

N0 = 200000
rate = 0.4

start = time.perf_counter()
decay.simulate(N0, rate)
time_pure = time.perf_counter() - start

start = time.perf_counter()
np.random.binomial(N0, np.exp(-rate)) 
time_numpy = time.perf_counter() - start

speedup = time_pure / time_numpy

print(f"Pure Python Loop: {time_pure:.6f} s")
print(f"NumPy Vectorized: {time_numpy:.6f} s")
print(f"Speed-up factor: {speedup:.2f}x faster")