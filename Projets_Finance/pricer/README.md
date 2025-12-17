Présentation globale du projet

J’ai développé en C++ un pricer d’options européennes basé sur le modèle binomial de Cox, Ross et Rubinstein. L’objectif était d'appliquer mon cours.


--------En détail :

Présentation générale du projet

Dans le cadre de ma préparation aux métiers de la finance de marché, j’ai développé en C++ un pricer d’options européennes basé sur le modèle binomial de Cox, Ross et Rubinstein. L’objectif de ce projet était double. D’une part, comprendre en profondeur les mécanismes de valorisation des options vus en cours, et d’autre part, les implémenter de manière rigoureuse dans un langage utilisé en environnement professionnel. Le choix du C++ s’explique par ses performances, sa gestion fine de la mémoire et son usage courant dans les équipes de pricing et de risk management.

Principe du modèle binomial

Le modèle binomial repose sur l’idée qu’à chaque pas de temps, le prix du sous-jacent peut évoluer selon deux scénarios possibles : une hausse ou une baisse. Cette évolution est représentée sous la forme d’un arbre recombining, ce qui permet de limiter la complexité du modèle. À maturité, on calcule le payoff de l’option en fonction du prix atteint par le sous-jacent. La valeur de l’option à la date initiale est ensuite obtenue par une méthode de remontée à rebours, appelée backward induction.

L’un des points fondamentaux du modèle est l’utilisation de la probabilité risque-neutre. Sous l’hypothèse d’absence d’opportunité d’arbitrage, l’espérance du prix du sous-jacent, pondérée par cette probabilité, croît au taux sans risque. Cela permet de valoriser l’option sans faire d’hypothèse sur les probabilités réelles du marché.

Paramétrisation du modèle CRR

Dans le modèle de Cox, Ross et Rubinstein, les facteurs de hausse et de baisse sont choisis de manière à faire correspondre la variance du modèle discret à celle d’un mouvement brownien géométrique. On pose ainsi un facteur de hausse égal à l’exponentielle de la volatilité multipliée par la racine du pas de temps, et le facteur de baisse comme son inverse. Cette construction garantit la recombinaison de l’arbre et assure la convergence du modèle binomial vers le modèle continu de Black-Scholes lorsque le nombre de pas tend vers l’infini.

La probabilité risque-neutre est ensuite calculée de façon à ce que l’espérance du prix du sous-jacent actualisée soit égale à son prix actuel. Cette probabilité joue un rôle central dans la phase de backward induction.

Implémentation en C++

L’implémentation a été réalisée selon une architecture orientée objet simple et claire. J’ai séparé la définition du produit financier de celle du modèle de valorisation. La classe Option contient les paramètres spécifiques au produit, tels que le strike et le type de l’option, et définit la fonction de payoff. La classe BinomialTree encapsule quant à elle le modèle de pricing, les paramètres de marché et la logique de calcul.

Pour des raisons de performance et de lisibilité, j’ai utilisé un vecteur unidimensionnel pour stocker les valeurs de l’option à chaque étape de l’arbre. Cette approche permet de réduire la complexité mémoire à un ordre linéaire, puisqu’un seul niveau de l’arbre est nécessaire à la fois lors de la remontée à rebours.

Valorisation des options européennes

La valorisation commence par le calcul des valeurs de l’option à maturité, en appliquant directement la fonction de payoff aux différents prix possibles du sous-jacent. Ensuite, on remonte pas à pas vers la date initiale en calculant, à chaque nœud, l’espérance actualisée des valeurs futures sous la probabilité risque-neutre. Le prix de l’option à la date initiale correspond à la valeur obtenue à la racine de l’arbre.

Ce cadre permet de valoriser aussi bien des options d’achat que des options de vente, en modifiant simplement la fonction de payoff.

Extension aux options américaines

Une extension naturelle du projet consiste à valoriser des options américaines. Contrairement aux options européennes, ces dernières peuvent être exercées à tout moment avant maturité. Dans le modèle binomial, cela se traduit par une comparaison, à chaque nœud de l’arbre, entre la valeur de continuation et la valeur d’exercice immédiat. La valeur retenue est le maximum des deux.

Cette approche permet notamment de mettre en évidence le fait qu’un call américain sur une action sans dividende n’est jamais exercé avant maturité, tandis qu’un put américain peut l’être dans certaines situations.

Analyse numérique et convergence

J’ai également étudié la convergence du prix de l’option lorsque le nombre de pas de temps augmente. On observe que plus le nombre de périodes est élevé, plus le prix calculé par le modèle binomial se rapproche du prix donné par la formule fermée de Black-Scholes. Cette convergence illustre le lien théorique entre les modèles discrets et continus et permet de valider la robustesse de l’implémentation.

Limites du modèle

Malgré sa simplicité et sa flexibilité, le modèle binomial présente certaines limites. Il repose sur l’hypothèse de volatilité et de taux constants, ce qui n’est pas réaliste sur les marchés financiers réels. De plus, il ne permet pas de capturer les phénomènes de smile ou de skew de volatilité observés sur les marchés d’options. Ces limites justifient l’utilisation de modèles plus avancés dans un cadre professionnel.

Améliorations possibles

Pour aller plus loin, plusieurs améliorations peuvent être envisagées. Il serait possible d’introduire des dividendes, soit sous forme discrète, soit sous forme de rendement continu. On pourrait également enrichir l’architecture logicielle pour intégrer plusieurs modèles de pricing, ou encore ajouter une procédure de calibration de la volatilité implicite à partir de prix de marché. Enfin, l’extension à des méthodes de Monte Carlo permettrait de traiter des options exotiques plus complexes.

Conclusion

Ce projet m’a permis de faire le lien entre la théorie de la valorisation des options et son implémentation concrète en C++. Il m’a également permis de mieux comprendre les hypothèses sous-jacentes aux modèles et leurs limites. Cette approche me semble essentielle pour travailler en finance de marché, où la capacité à combiner rigueur théorique et implémentation robuste est primordiale.