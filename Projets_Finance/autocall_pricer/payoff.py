def autocall_payoff(paths, params):
    S0 = params["S0"]
    coupon = params["coupon"]
    nominal = params["nominal"]
    barriere_rappel = params["barriere_rappel"]
    barriere_pdi = params["barriere_pdi"]

    n_simulations, n_steps = paths.shape[0], paths.shape[1] - 1
    payoffs = np.zeros(n_simulations)

    for i in range(n_simulations):
        for t in range(1, n_steps + 1):
            if paths[i, t] >= barriere_rappel * S0:
                payoffs[i] = nominal * (1 + coupon * t)
                break
        else:
            # Cas maturité
            ST = paths[i, -1]
            if ST >= barriere_pdi * S0:
                payoffs[i] = nominal
            else:
                payoffs[i] = nominal * (ST / S0)

    return payoffs
