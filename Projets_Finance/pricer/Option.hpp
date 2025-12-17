#ifndef OPTION_HPP
#define OPTION_HPP

#include <algorithm>

enum OptionType
{
    Call,
    Put
};

class Option
{
public:
    Option(double strike, OptionType type)
        : K(strike), optionType(type) {}

    double payoff(double S) const
    {
        if (optionType == Call)
            return std::max(S - K, 0.0);
        else
            return std::max(K - S, 0.0);
    }

private:
    double K;
    OptionType optionType;
};

#endif
