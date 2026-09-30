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