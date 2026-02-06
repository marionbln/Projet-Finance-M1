import numpy as np  # Utilisation de la bibliothèque NumPy pour les calculs matriciels

def simulate_paths(S0, r, sigma, T, n_steps, n_simulations):
    # Calcul de l'intervalle de temps entre deux observations (ex: 1 an)
    dt = T / n_steps 
    
    # Création d'une matrice de zéros (Lignes : scénarios, Colonnes : dates)
    paths = np.zeros((n_simulations, n_steps + 1)) 
    
    # Injection du prix initial S0 dans la première colonne pour chaque scénario
    paths[:, 0] = S0 

    # Boucle itérative sur chaque étape de temps
    for t in range(1, n_steps + 1):
        # Génération d'un vecteur de chocs aléatoires (loi normale centrée réduite)
        Z = np.random.normal(0, 1, n_simulations) 
        
        # Calcul vectorisé du prix à l'instant 't' basé sur l'instant 't-1'
        # Application de la formule du Mouvement Brownien Géométrique
        paths[:, t] = paths[:, t-1] * np.exp(
            (r - 0.5 * sigma**2) * dt +  # Composante de dérive (drift)
            sigma * np.sqrt(dt) * Z      # Composante de diffusion (volatilité)
        )

    return paths # Renvoi de la matrice complète des trajectoires simulées
