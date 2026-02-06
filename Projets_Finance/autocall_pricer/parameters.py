import numpy as np

# Paramètres marché
S0 = 100          # Niveau initial de l'indice
r = 0.02          # Taux sans risque
sigma = 0.20      # Volatilité
T = 6             # Maturité (années)

# Paramètres produit
coupon = 0.06     # 6% par an
barriere_rappel = 1.0     # 100%  elle declenche remboursement anticipé du produit à date d'anniv, si l'indice S au dessus de Pdi alors investisseur recoit capital + nb d'années écoulées
barriere_pdi = 0.6        # 60% declenche protection capital à 100% à l'echeance (put down andin)
nominal = 100

# Monte-Carlo
n_simulations = 50_000
n_steps = T      # 1 observation par an
dt = T / n_steps

