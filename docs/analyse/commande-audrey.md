# Analyse de la commande - Audrey

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1. **Pour décider à quel seuil déclencher le dispositif renforcé**, la direction a besoin de savoir, pour chaque niveau de la Météo des forêts, quelle part des jours a connu au moins un départ de feu en Côte-d'Or.
   - *Test :* si cette part augmente nettement entre « modéré » et « élevé », la direction déclenche à « élevé » ; si elle est déjà forte au niveau « modéré », elle abaisse le seuil.
2. **Pour décider à quel seuil déclencher le dispositif renforcé dans la limite du budget**, la direction a besoin de savoir, pour chaque seuil possible, combien de jours de dispositif renforcé il aurait représentés par saison et quelle part des départs de feu ces jours auraient couverts.
   - *Test :* si un seuil couvre la plupart des départs de feu en peu de jours, la direction le retient ; si couvrir les départs de feu coûte trop de jours, elle limite le renforcement à certaines zones ou à certaines périodes.
3. **Pour décider où concentrer les moyens**, la direction a besoin de savoir dans quelles zones de Côte-d'Or (communes, massifs forestiers) se concentrent les départs de feu et les surfaces brûlées.
   - *Test :* si les départs de feu se concentrent sur quelques zones, la direction y affecte les moyens en priorité ; s'ils sont dispersés, elle garde une couverture départementale déclenchée moins souvent.
4. **Pour décider si le seuil doit être propre à la Côte-d'Or**, la direction a besoin de savoir si le lien entre le niveau de la Météo des forêts et les départs de feu est le même en Côte-d'Or que dans les autres départements de Bourgogne-Franche-Comté et dans le reste de la France.
   - *Test :* si le lien est le même, la direction reprend le seuil de référence ; s'il est différent, elle fixe un seuil propre au département.

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| Météo des forêts | Le dispositif de Météo-France qui publie chaque jour un niveau de danger d'incendie de forêt | Son producteur, ses niveaux, sa zone de prévision (département entier ou sous-zones), depuis quand il existe |
| Danger élevé | Un des niveaux de la Météo des forêts | Le niveau exact auquel pensent les chefs de centre ; la liste officielle des niveaux |
| Départ de feu | Un feu qui démarre, quelle que soit sa taille finale | S'il compte les feux éteints très vite, ou seulement ceux qui dépassent une surface minimale |
| Feu de forêt | Un feu qui touche une surface boisée | La différence avec un départ de feu, un feu de végétation ou une intervention pour incendie ; la surface minimale retenue par les sources |
| Département | La Côte-d'Or, code 21 | Si on parle du territoire administratif (code INSEE) ou de la zone couverte par le SDIS 21 |
| Dispositif renforcé | Les moyens ajoutés quand le danger monte : patrouilles, guet | Ce qu'il contient exactement et ce que coûte une journée de dispositif renforcé |
| Seuil actuel | Le niveau de la Météo des forêts à partir duquel le SDIS 21 déclenche aujourd'hui le dispositif renforcé | Sa valeur réelle ; s'il est le même partout dans le département |
| Moyens humains et financiers | Les effectifs, les engins et le budget alloués à la lutte contre les feux | Ce que la direction peut réellement déplacer d'une zone à une autre |
| Saison feux | La période de l'année où le risque est surveillé | Ses dates de début et de fin ; si elle inclut le printemps |
| Massif forestier | Un ensemble de forêts d'un seul tenant | S'il existe un découpage officiel des massifs en Côte-d'Or |

## 3. Les besoins

La décision à éclairer, en une phrase :

Choisir le niveau de la Météo des forêts qui déclenche le dispositif renforcé et les zones de Côte-d'Or où concentrer les moyens, sans dépasser le budget de l'été 2027.

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
- La valeur du seuil actuel et la façon dont il est appliqué.
- Le coût d'une journée de dispositif renforcé et le budget disponible pour 2027.
- La définition d'un départ de feu retenue par le SDIS 21 (surface minimale, prise en compte des feux éteints rapidement).
- L'accès aux données d'intervention du SDIS 21, qui ne sont peut-être pas publiques.
- La zone que couvre un niveau de la Météo des forêts : le département entier ou des sous-zones.
- Ce que recouvrent les « moyens » : effectifs, engins, postes de guet.
- Les dates de la saison feux, et si le printemps en fait partie.

## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Niveau quotidien de la Météo des forêts et nombre de départs de feu du même jour | Un jour × une zone de prévision | Au moins 10 saisons feux | Jusqu'à la saison 2026 incluse | Côte-d'Or |
| 2 | La même table que pour la question 1, plus le coût d'une journée de dispositif renforcé | Un jour × une zone de prévision | Au moins 10 saisons feux | Saison 2026 ; coûts et budget 2027 | Côte-d'Or |
| 3 | Liste des départs de feu avec date, commune ou coordonnées, surface brûlée et cause si elle est connue ; surface forestière par commune | Un départ de feu | Au moins 10 ans | Jusqu'à la saison 2026 incluse | Communes de Côte-d'Or |
| 4 | Niveau quotidien de la Météo des forêts et nombre de départs de feu, pour chaque département | Un jour × un département | La même période pour tous les départements | Jusqu'à la saison 2026 incluse | Les 8 départements de Bourgogne-Franche-Comté et la France métropolitaine |
