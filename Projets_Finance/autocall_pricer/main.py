from simulation import simulate_paths
from payoff import autocall_payoff
from pricing import price_product
from plots import plot_paths
import parameters as p

params = {
    "S0": p.S0,
    "coupon": p.coupon,
    "nominal": p.nominal,
    "barriere_rappel": p.barriere_rappel,
    "barriere_pdi": p.barriere_pdi
}

# simuler les trajectoires de l'indice sous-jacent ( mettre grand nombre de simulations mm si on affiche qu'une partie des trajectoires)
paths = simulate_paths(
    p.S0, p.r, p.sigma, p.T, p.n_steps, p.n_simulations
)

payoffs = autocall_payoff(paths, params) # On calcule les payoffs à partir des trajectoires simulées et des paramètres du produit
price = price_product(payoffs, p.r, p.T) # c'est le prix du produit, c'est à dire la valeur actuelle des payoffs moyens obtenus à partir de la simulation

print(f"Prix du produit : {price:.2f}")
plot_paths(paths)
