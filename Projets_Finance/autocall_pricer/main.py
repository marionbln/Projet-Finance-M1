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

paths = simulate_paths(
    p.S0, p.r, p.sigma, p.T, p.n_steps, p.n_simulations
)

payoffs = autocall_payoff(paths, params)
price = price_product(payoffs, p.r, p.T)

print(f"Prix du produit : {price:.2f}")
plot_paths(paths)
