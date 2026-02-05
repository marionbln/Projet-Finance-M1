import numpy as np

def autocall_payoff(paths, params):
    # 1. RÉCUPÉRATION DES PARAMÈTRES DU PRODUIT 
    S0 = params["S0"]                # Prix initial de l'indice
    coupon = params["coupon"]        # Rendement annuel promis (ex: 0.06 pour 6%)
    nominal = params["nominal"]      # Capital investi (ex: 1000€)
    barriere_rappel = params["barriere_rappel"] # Seuil de déclenchement (ex: 1.0 pour 100%)
    barriere_pdi = params["barriere_pdi"]       # Barrière de protection (ex: 0.6 pour 60%)

    n_simulations, n_steps = paths.shape[0], paths.shape[1] - 1
    payoffs = np.zeros(n_simulations)

    for i in range(n_simulations):
        # 2. SURVEILLANCE DES DATES DE RAPPEL 
        for t in range(1, n_steps + 1):
            # Si à l'année 't', l'indice est au-dessus du seuil de rappel
            if paths[i, t] >= barriere_rappel * S0:
                # Remboursement du capital + tous les coupons accumulés
                payoffs[i] = nominal * (1 + coupon * t)
                break  # Le produit s'arrête immédiatement (Path-dependent)
        
        # 3. SCÉNARIO À MATURITÉ (SI PAS DE RAPPEL) 
        else:
            # On arrive au bout des 6 ans sans avoir jamais déclenché le rappel
            ST = paths[i, -1] # Prix final au dernier jour
            
            # Cas A : L'indice est au-dessus de la barrière de protection (PDI)
            if ST >= barriere_pdi * S0:
                payoffs[i] = nominal  # L'investisseur récupère 100% de son capital
            
            # Cas B : Crash boursier, barrière PDI franchie à l'échéance
            else:
                # L'investisseur subit la perte réelle de l'indice (Performance négative)
                payoffs[i] = nominal * (ST / S0)

    return payoffs
