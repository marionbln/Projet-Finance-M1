import numpy as np

def autocall_payoff(paths, params):
    # Extraction des variables depuis le dictionnaire de paramètres
    S0 = params["S0"]
    coupon = params["coupon"]
    nominal = params["nominal"]
    barriere_rappel = params["barriere_rappel"]
    barriere_pdi = params["barriere_pdi"]

    # Identification des dimensions de la matrice : scénarios et étapes
    n_simulations, n_steps = paths.shape[0], paths.shape[1] - 1
    payoffs = np.zeros(n_simulations) # Stockage du gain final pour chaque scénario

    for i in range(n_simulations): # Analyse de chaque scénario individuellement
        for t in range(1, n_steps + 1): # Parcours chronologique de l'année 1 à 6
            # Condition de rappel anticipé : l'indice dépasse 100% de S0
            if paths[i, t] >= barriere_rappel * S0:
                # Paiement du capital + coupons accumulés (6% par année écoulée)
                payoffs[i] = nominal * (1 + coupon * t)
                break # Arrêt immédiat du produit pour ce scénario
        else:
            # Cas où aucun rappel n'a eu lieu durant la vie du produit
            ST = paths[i, -1] # Niveau final de l'indice à maturité
            
            # Vérification de la barrière de protection (PDI) à 60%
            if ST >= barriere_pdi * S0:
                payoffs[i] = nominal # Remboursement intégral du capital
            else:
                # Perte en capital proportionnelle à la baisse de l'indice
                payoffs[i] = nominal * (ST / S0)

    return payoffs # Liste des 50 000 gains générés
