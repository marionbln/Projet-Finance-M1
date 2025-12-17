import numpy as np

def price_product(payoffs, r, T):
    return np.mean(payoffs) * np.exp(-r * T)
