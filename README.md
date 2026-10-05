# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

## PW1 - Lab A: Reproducible Foundations
**What I built:**

Created the CSPC repository structure, configured conda environment, integrated Git/GitHub workflow, written unit tests with pytest, and benchmarked NumPy against Python loops.

**Speed comparison (loop vs NumPy):**

- loop : 3.0120 s
- numpy : 0.0004 s
- speed-up: 8466.98x faster
**Tests:** all passing? yes

**Conclusion:**

NumPy vectorization dramatically increases computational performance compared to pure Python loops. Setting up isolated environments and Git repositories guarantees complete reproducibility of scientific results.


## PW1 Lab B
- **Data observation:** The observed decay data shows an exponential decay over time.
- **Model match:** The observed data points match the theoretical analytical decay law $N_0 e^{-\lambda t}$.
- **Snakemake pipeline:** The Snakemake pipeline automatically regenerates `figure.png` whenever the dataset or plotting script changes.

## PW2 Lab A

- **Mean Acceleration:** -8.58 m/s²
- **Why is acceleration noisy?** Differentiation amplifies measurement noise because comparing small fluctuations between nearby points results in large jumps in calculated rates of change.
- **Integrating Back:** Integrating the noisy acceleration back to position suppresses the noise, matching the original position data within about 0.78 metres (Max Difference: 0.7846 m).

## PW2 Lab B - Optimization in Chemistry

- **Method Comparison (Part 2):** On the convex function f(x), Gradient Descent, Newton's method, and SLSQP all converged to x ≈ 3. On the non-convex landscape g(x), the results depended heavily on the starting point x0: starting at x0=0 led Newton to a local maximum/stationary point (g'' < 0), whereas starting at x0=2 allowed methods to find the local minimum (g'' > 0).
- **Fitted Rate Constant (Part 3):** The reaction rate constant was fitted as k ≈ 0.26 s⁻¹.
- **Equilibrium Composition (Part 4):** Newton and SLSQP agreed on an extent of reaction x ≈ 0.66, giving equilibrium amounts of H₂ ≈ 0.33 mol, I₂ ≈ 0.33 mol, and HI ≈ 1.33 mol.
- **Titration Equivalence Point (Part 5):** The equivalence point was determined at V ≈ 50 mL, where the pH gradient reached its maximum.