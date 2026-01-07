🔹 Pricer Monte-Carlo d’un Autocall Athena (Python)

Ce projet implémente en Python un pricer Monte-Carlo pour un produit structuré de type Autocall Athena, dont le sous-jacent est modélisé par un mouvement brownien géométrique dans le cadre de Black-Scholes. Des trajectoires de prix sont simulées afin de vérifier les conditions de rappel anticipé à chaque date d’observation ; en cas de rappel, le capital et les coupons sont versés, sinon une protection conditionnelle du capital est appliquée à maturité. Les flux obtenus sont ensuite actualisés pour calculer la valeur théorique du produit, permettant d’analyser l’impact des paramètres de marché comme la volatilité ou les taux.

🔹 Pricer d’options par arbre binomial (C++)

Ce projet développe en C++ un pricer d’options vanilles basé sur un arbre binomial recombiné, permettant de valoriser des options européennes et américaines. Le modèle repose sur une dynamique discrète du sous-jacent et sur le principe de valorisation risque-neutre, avec une rétro-propagation des payoffs depuis la maturité jusqu’à l’origine de l’arbre, intégrant l’exercice anticipé pour les options américaines. L’accent est mis sur une architecture orientée objet, la rigueur numérique et les performances du code.
