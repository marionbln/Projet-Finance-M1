import numpy as np

def price_product(payoffs, r, T):
    return np.mean(payoffs) * np.exp(-r * T) # On actualise la moyenne des payoffs à la valeur présente en utilisant le taux d'actualisation r et la maturité T