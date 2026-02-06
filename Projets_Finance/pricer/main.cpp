#include <iostream>          // Charge les outils système pour l'entrée/sortie (clavier/écran)
#include "BinomialTree.hpp"  // Charge tes propres définitions de classes (Option et BinomialTree)

int main()                   // Définit le bloc principal où l'exécution commence obligatoirement
{
    // On déclare des variables de type 'double' pour stocker des nombres décimaux précis
    double S0 = 100.0;       // Prix de l'action à l'instant t=0 (Spot)
    double K = 100.0;        // Prix cible du contrat (Strike)
    double r = 0.05;         // Taux d'intérêt annuel (5%) utilisé pour l'actualisation
    double sigma = 0.20;     // Volatilité (l'incertitude du marché, ici 20%)
    double T = 1.0;          // Durée du contrat en années (Maturité)

    int steps = 200;         // Un 'int' est un entier ; ici, le nombre de paliers du calcul

    // Instanciation : on crée des objets réels à partir du plan de construction (la classe)
    // 'Option' est le type, 'call' est le nom de l'objet, 'K' et 'Call' sont les paramètres
    Option call(K, Call);    
    Option put(K, Put);      

    // On prépare l'algorithme 'tree' en lui injectant toutes nos données de marché d'un coup
    BinomialTree tree(S0, r, sigma, T, steps);

    // On appelle la fonction '.price()' appartenant à l'objet 'tree'
    // Elle prend l'objet 'call' en entrée pour lui appliquer le modèle mathématique
    double callPrice = tree.price(call); 
    double putPrice = tree.price(put);

    // 'std::cout' représente la console. '<<' injecte les données dans ce flux de sortie
    // 'std::endl' force le passage à la ligne et vide la mémoire tampon de l'affichage
    std::cout << "European Call price: " << callPrice << std::endl;
    std::cout << "European Put price : " << putPrice << std::endl;

    return 0;                // Renvoie le code de succès '0' au système d'exploitation
}
