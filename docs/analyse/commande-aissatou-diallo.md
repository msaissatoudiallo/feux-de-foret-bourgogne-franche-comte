# Analyse de la commande - Aissatou Diallo

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1. **Dans quelles zones de la Côte-d'Or les départs de feu sont-ils les plus nombreux, et où brûlent-ils le plus de surface ?**
   - Si les feux sont concentrés sur quelques communes ou massifs : la direction y place en priorité ses moyens (guet, patrouilles, matériel).
   - S'ils sont répartis sur tout le département : elle garde des moyens mobiles, capables d'intervenir partout.

2. **À quelles périodes de l'année (mois, semaines) les départs de feu se produisent-ils en Côte-d'Or ?**
   - S'ils se concentrent en juillet-août : la direction renforce le dispositif seulement sur ces semaines.
   - S'il y en a aussi au printemps : elle doit prévoir le renfort plus tôt et étaler son budget sur une période plus longue.

3. **Pour chaque niveau de la Météo des forêts, à quelle fréquence observe-t-on au moins un départ de feu en Côte-d'Or ?**
   - Si les feux augmentent nettement à partir d'un certain niveau : la direction fixe son seuil de déclenchement à ce niveau.
   - Si les feux ne suivent pas l'indice : elle ne peut pas se fier à l'indice seul, et doit le combiner avec d'autres critères (période, zone…).

4. **L'indice se trompe-t-il autant en Côte-d'Or (danger annoncé sans feu, feux par indice bas) que dans les autres départements de la région et en France ?**
   - Si l'indice se trompe partout autant : c'est une limite de l'indice lui-même, la direction adapte son seuil en connaissance de cause.
   - Si l'indice se trompe surtout en Côte-d'Or : il y a des causes propres au département (causes des feux, type de forêt…), la direction doit les étudier et adapter son dispositif localement.

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| SDIS | Service départemental d'incendie et de secours : les pompiers d'un département (ici la Côte-d'Or, n° 21). | Le territoire couvert par le SDIS 21 correspond-il exactement au département de la Côte-d'Or ? |
| Départ de feu | Le moment et l'endroit où un feu commence, qu'il soit grand ou petit. | Est-ce que chaque départ de feu devient un « feu de forêt » dans les données ? Compte-t-on aussi les feux éteints tout de suite ? |
| Feu de forêt | Un feu qui brûle une zone de forêt. | À partir de quelle surface ou de quel type de végétation (forêt, broussailles, champs) on parle de feu de forêt ? La définition est-elle la même dans toutes les sources ? |
| Météo des forêts | Un indice de Météo-France qui annonce chaque jour le niveau de danger de feu de forêt. | Qui le calcule, sur quelle zone (département ou plus petit), depuis quand il existe, et sur quelle période de l'année il est publié. |
| Niveau / seuil de l'indice | Les différents niveaux de danger (par exemple faible, modéré, élevé, très élevé). | Combien de niveaux existent exactement, et quel est le seuil actuellement utilisé par le SDIS 21 ? |
| Danger élevé | Un des niveaux de l'indice, qui signifie un risque important de feu. | De quel niveau précis parlent les chefs de centre quand ils disent « danger élevé » ? |
| Dispositif renforcé | Les mesures supplémentaires prises quand le risque est fort : patrouilles, guet (surveillance), etc. | Que contient exactement ce dispositif, combien il coûte par jour, et sur quelle zone il est déclenché ? |
| Moyens humains et financiers | Les pompiers, le matériel et le budget que le SDIS peut répartir. | Quel est le budget disponible pour l'été 2027, et combien de personnes peuvent être mobilisées ? |
| Chef de centre | Le responsable d'une caserne de pompiers. | Combien de centres il y a en Côte-d'Or et quelle zone couvre chaque centre ? |
| Été / saison feux | La période où il y a le plus de feux de forêt. | Quels mois exactement : juin à septembre ? La commande parle aussi du printemps. |

## 3. Les besoins

La décision à éclairer, en une phrase :

Pour l'été 2027, avec un budget limité, la direction du SDIS 21 doit décider où et quand renforcer son dispositif contre les feux de forêt, et à partir de quel niveau de la Météo des forêts le déclencher.

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
- **Le budget disponible** pour l'été 2027 et le **coût d'une journée** de dispositif renforcé : sans ces chiffres, on ne sait pas combien de jours ou de zones on peut renforcer.
- **Le seuil actuel** de déclenchement : quel niveau de la Météo des forêts est utilisé aujourd'hui, et depuis quand.
- **Le contenu du dispositif renforcé** : patrouilles, guet… mais combien de personnes, sur quelle zone, et peut-il être déclenché sur une partie du département seulement ?
- **Les données internes du SDIS** : la direction a-t-elle ses propres données d'interventions, et peut-on y accéder ? Sinon, il faudra se baser uniquement sur des données ouvertes.
- **Les chiffres de l'été 2026** : la direction dit s'attendre à « autant de feux que l'été 2026 », mais ne précise pas combien il y en a eu.
- **Les remarques des chefs de centre** : il faudrait des exemples précis (dates, lieux) des fausses alertes et des feux partis par indice bas, pour vérifier ces impressions avec les données.
- **Hypothèse à confirmer** : on suppose que ce qui s'est passé les années précédentes (où et quand partent les feux) se reproduira en 2027.

## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Liste des départs de feu avec leur localisation (commune, et si possible coordonnées GPS) et la surface brûlée | Un départ de feu | Les 10 dernières années au moins, pour voir si les zones touchées sont toujours les mêmes | Une mise à jour par an suffit (on étudie le passé) | Côte-d'Or, au niveau de la commune |
| 2 | Liste des départs de feu avec leur date (et si possible l'heure) | Un départ de feu | Les 10 dernières années au moins, toute l'année (pas seulement l'été) | Une mise à jour par an suffit | Côte-d'Or |
| 3 | Le niveau de la Météo des forêts de chaque jour, et le nombre de départs de feu observés ce même jour | Un jour dans une zone (niveau de l'indice + nombre de feux) | Toutes les années où l'indice est disponible, sur toute la saison | Historique pour l'analyse ; quotidienne si on veut ensuite suivre le seuil pendant l'été 2027 | Côte-d'Or, à la zone la plus fine où l'indice est publié |
| 4 | Même donnée que la question 3, mais pour tous les départements | Un jour dans un département (niveau de l'indice + nombre de feux) | La même période pour tous les départements, pour pouvoir comparer | Une mise à jour par an suffit | Les 8 départements de Bourgogne-Franche-Comté et toute la France |

Remarque : les questions 3 et 4 demandent de **croiser deux données** (l'indice et les feux). Il faudra pouvoir les relier par la **date** et par la **zone** (département ou commune) : ce seront nos clés de jointure.