#ifndef BINOMIAL_TREE_HPP
#define BINOMIAL_TREE_HPP

#include <vector>
#include <cmath>
#include "Option.hpp"

class BinomialTree
{
public:
    BinomialTree(double S0,
                 double r,
                 double sigma,
                 double T,
                 int steps)
        : S0(S0), r(r), sigma(sigma), T(T), n(steps)
    {

        dt = T / n;
        u = std::exp(sigma * std::sqrt(dt));
        d = 1.0 / u;
        p = (std::exp(r * dt) - d) / (u - d);
        discount = std::exp(-r * dt);
    }

    double price(const Option &option) const
    {
        std::vector<double> values(n + 1);

        // Valeurs à maturité
        for (int i = 0; i <= n; ++i)
        {
            double ST = S0 * std::pow(u, i) * std::pow(d, n - i);
            values[i] = option.payoff(ST);
        }

        // Backward induction
        for (int step = n - 1; step >= 0; --step)
        {
            for (int i = 0; i <= step; ++i)
            {
                values[i] = discount * (p * values[i + 1] + (1.0 - p) * values[i]);
            }
        }

        return values[0];
    }

private:
    double S0, r, sigma, T;
    int n;
    double u, d, p, dt, discount;
};

#endif
