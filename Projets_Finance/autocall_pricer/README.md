
--------------------------------------

Présentation globale de mon projet

Mon projet en une minute ?
J’ai développé en Python un pricer Monte-Carlo pour un produit structuré de type Autocall Athena. Le sous-jacent est modélisé par un mouvement brownien géométrique dans le cadre de Black-Scholes. Je simule un grand nombre de trajectoires de l’indice, puis j’applique la logique contractuelle du produit : vérification des barrières de rappel à chaque date d’observation, arrêt anticipé du produit lorsque la condition est remplie, ou application d’une protection conditionnelle du capital à maturité. Les flux obtenus dans chaque scénario sont ensuite actualisés afin de calculer la valeur théorique du produit à l’émission, et j’analyse l’impact des paramètres de marché comme la volatilité ou les taux.

Qu'est-ce qu'un Athena ?
Un Athena est un type d’Autocall, c’est-à-dire un produit structuré dont le remboursement peut être anticipé.
Il se caractérise par le fait que le coupon n’est versé que si le produit est rappelé à une date d’observation, lorsque le sous-jacent dépasse une barrière prédéfinie. Si cette barrière n’est pas atteinte, aucun coupon n’est payé et le produit continue jusqu’à la date suivante. En l’absence de rappel jusqu’à maturité, le remboursement du capital dépend du niveau final du sous-jacent, avec généralement une protection conditionnelle du capital.


Pourquoi avoir choisi un Autocall ?
L’Autocall est un produit très répandu sur les marchés, notamment en Europe. Il présente un payoff non linéaire et dépendant du chemin du sous-jacent, ce qui le rend intéressant d’un point de vue quantitatif. De plus, il n’existe pas de formule fermée simple pour le pricer, ce qui rend l’approche Monte-Carlo particulièrement adaptée et pertinente.

Modélisation financière

Quel modèle j'utilise pour le sous-jacent ?
J’utilise un mouvement brownien géométrique, comme dans le modèle de Black-Scholes, avec un taux sans risque et une volatilité supposés constants sur toute la durée du produit.

Quelles sont les hypothèses du modèle Black-Scholes ?
Le modèle repose sur l’absence d’opportunité d’arbitrage, des marchés frictionless, un taux sans risque constant, une volatilité constante et des rendements log-normaux du sous-jacent. En pratique, certaines de ces hypothèses sont simplificatrices, en particulier celle de la volatilité constante, qui ne reflète pas toujours la réalité du marché.

Pourquoi utiliser Monte-Carlo plutôt qu’une formule fermée ?
Le payoff d’un Autocall dépend non seulement du niveau final du sous-jacent, mais aussi de son évolution à des dates intermédiaires, notamment à cause du mécanisme de rappel anticipé. Cette dépendance au chemin empêche l’existence d’une formule analytique simple, ce qui justifie l’utilisation de Monte-Carlo.

Payoff et logique du produit structuré

Comment je gère le rappel anticipé dans mon code ?
À chaque date de constatation, je compare le niveau du sous-jacent à la barrière de rappel. Si la condition est remplie, le produit est rappelé, le remboursement du capital et des coupons est déclenché, et les flux futurs sont annulés.

Que se passe-t-il si le produit n’est jamais rappelé ?
Si aucun rappel n’a lieu avant la maturité, j’applique la protection conditionnelle du capital. Le nominal est remboursé si la barrière de protection est respectée ; sinon, l’investisseur subit une perte proportionnelle à la baisse du sous-jacent.

Quelle est la différence entre Athena et Phoenix ?
Dans un Autocall Athena, le coupon n’est versé qu’en cas de rappel. Dans un Autocall Phoenix, un coupon peut être versé même sans rappel, et les coupons non versés peuvent être récupérés grâce à un effet mémoire.


Programmation (Python)

Pourquoi Python ?
Python est très utilisé en finance, facile à lire, rapide pour prototyper et dispose de bibliothèques adaptées au calcul scientifique et à la simulation numérique.

Comment j'assure la convergence Monte-Carlo ?
J’augmente le nombre de simulations jusqu’à ce que le prix se stabilise.


Esprit critique

Quelles sont les limites de ton modèle ?
Le modèle repose sur une volatilité constante et ne prend pas en compte le smile de volatilité ni la dynamique réelle du marché. En pratique, on utiliserait plutôt un modèle à volatilité stochastique, comme Heston, calibré sur des données de marché.

Qu'est-ce que jeferais avec plus de temps ?
J’ajouterais des fonctionnalités comme l’effet mémoire, l’analyse des grecques du produit ou un modèle à volatilité stochastique.

Question finale

Qu'est-ce j'ai appris avec ce projet ?

Ce projet m’a permis de comprendre concrètement comment un produit structuré est conçu, valorisé et analysé, et comment transformer une logique financière complexe en un modèle quantitatif implémenté en code.
