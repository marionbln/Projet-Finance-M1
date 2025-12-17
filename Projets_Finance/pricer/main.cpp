#include <iostream>
#include "BinomialTree.hpp"

int main()
{
    double S0 = 100.0;
    double K = 100.0;
    double r = 0.05;
    double sigma = 0.20;
    double T = 1.0;

    int steps = 200;

    Option call(K, Call);
    Option put(K, Put);

    BinomialTree tree(S0, r, sigma, T, steps);

    double callPrice = tree.price(call);
    double putPrice = tree.price(put);

    std::cout << "European Call price: " << callPrice << std::endl;
    std::cout << "European Put price : " << putPrice << std::endl;

    return 0;
}
