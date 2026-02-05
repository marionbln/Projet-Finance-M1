import numpy as np
import matplotlib.pyplot as plt
import parameters as p
from simulation import simulate_paths
from payoff import autocall_payoff
from pricing import price_product

# On prépare les paramètres pour la fonction payoff
params = {
    "S0": p.S0,
    "coupon": p.coupon,
    "nominal": p.nominal,
    "barriere_rappel": p.barriere_rappel,
    "barriere_pdi": p.barriere_pdi
}

def analyze_sensitivities():
    # 1. Analyse du VEGA (Variation de la Volatilité)
    volats = np.linspace(0.05, 0.50, 10) # De 5% à 50%
    prices_vega = []
    
    for v in volats:
        # np.random.seed(42)  # Optionnel : pour lisser la courbe
        paths = simulate_paths(p.S0, p.r, v, p.T, p.n_steps, p.n_simulations)
        payoffs = autocall_payoff(paths, params)
        prices_vega.append(price_product(payoffs, p.r, p.T))

    # 2. Analyse du RHO (Variation des Taux)
    rates = np.linspace(0.0, 0.10, 10) # De 0% à 10%
    prices_rho = []
    
    for r_test in rates:
        # np.random.seed(42)
        paths = simulate_paths(p.S0, r_test, p.sigma, p.T, p.n_steps, p.n_simulations)
        payoffs = autocall_payoff(paths, params)
        prices_rho.append(price_product(payoffs, r_test, p.T))

    #  AFFICHAGE
    plt.figure(figsize=(12, 5))

    # Graphique Vega
    plt.subplot(1, 2, 1)
    plt.plot(volats * 100, prices_vega, 'r-o', label="Prix vs Volatilité")
    plt.title("Analyse du VEGA")
    plt.xlabel("Volatilité (%)")
    plt.ylabel("Prix (€)")
    plt.grid(True)

    # Graphique Rho
    plt.subplot(1, 2, 2)
    plt.plot(rates * 100, prices_rho, 'b-s', label="Prix vs Taux")
    plt.title("Analyse du RHO")
    plt.xlabel("Taux sans risque (%)")
    plt.ylabel("Prix (€)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_sensitivities()