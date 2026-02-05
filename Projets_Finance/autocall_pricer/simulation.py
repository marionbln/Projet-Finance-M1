import numpy as np

def simulate_paths(S0, r, sigma, T, n_steps, n_simulations):
    dt = T / n_steps
    paths = np.zeros((n_simulations, n_steps + 1))
    paths[:, 0] = S0

    for t in range(1, n_steps + 1):
        Z = np.random.normal(0, 1, n_simulations)
        paths[:, t] = paths[:, t-1] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
        )

    return paths
