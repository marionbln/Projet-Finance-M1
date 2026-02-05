#ifndef BINOMIAL_TREE_HPP
#define BINOMIAL_TREE_HPP

#include <vector>
#include <cmath>
#include "Option.hpp"

class BinomialTree
{
public:
    // CONSTRUCTEUR : Prépare les paramètres de l'univers financier
    BinomialTree(double S0, double r, double sigma, double T, int steps)
        : S0(S0), r(r), sigma(sigma), T(T), n(steps)
    {
        // 1. On découpe le temps en intervalles (ex: 1 an / 200 pas)
        dt = T / n;

        // 2. Facteur de hausse (u) et baisse (d) basés sur la volatilité (sigma)
        // Formule de Cox-Ross-Rubinstein
        u = std::exp(sigma * std::sqrt(dt));
        d = 1.0 / u;

        // 3. Probabilité "risque-neutre" (p)
        // C'est la probabilité théorique pour que le modèle soit sans arbitrage
        p = (std::exp(r * dt) - d) / (u - d);

        // 4. Facteur d'actualisation (discount)
        // Sert à ramener une valeur future à sa valeur d'aujourd'hui
        discount = std::exp(-r * dt);
    }

    // MÉTHODE PRICE : Calcule le prix de l'option passée en paramètre
    double price(const Option &option) const
    {
        // On crée un vecteur pour stocker les prix de l'option à chaque nœud
        // On n'a besoin que de (n+1) cases pour optimiser la mémoire
        std::vector<double> values(n + 1);

        // ÉTAPE 1 : CALCUL DES VALEURS À L'ÉCHÉANCE (MATURITÉ) 
        // On va tout au bout de l'arbre (à la date T)
        for (int i = 0; i <= n; ++i)
        {
            // i représente le nombre de hausses (u) subies par l'action
            // (n-i) représente le nombre de baisses (d)
            double ST = S0 * std::pow(u, i) * std::pow(d, n - i);

            // On demande à l'objet Option : "Quel est le gain direct pour ce prix ST ?"
            values[i] = option.payoff(ST);
        }

        // ÉTAPE 2 : INDUCTION ARRIÈRE (BACKWARD INDUCTION) 
        // On "rembobine" l'arbre de la fin vers le début
        for (int step = n - 1; step >= 0; --step)
        {
            for (int i = 0; i <= step; ++i)
            {
                // La valeur d'un nœud est la moyenne pondérée de ses deux futurs possibles
                // On multiplie par 'discount' pour retirer l'effet des intérêts
                values[i] = discount * (p * values[i + 1] + (1.0 - p) * values[i]);
            }
        }

        // La case 0 contient maintenant le prix de l'option à t=0 (aujourd'hui)
        return values[0];
    }

private:
    // Variables de marché
    double S0;    // Prix initial de l'action
    double r;     // Taux d'intérêt
    double sigma; // Volatilité
    double T;     // Temps total (maturité)
    int n;        // Nombre de pas (précision)

    // Variables calculées pour l'arbre
    double u, d, p, dt, discount;
};

#endif
