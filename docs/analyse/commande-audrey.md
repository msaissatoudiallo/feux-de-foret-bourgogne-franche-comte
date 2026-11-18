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

## 5. Confrontation aux sources

### Matrice

Sources de l'inventaire du groupe (`docs/sources/inventaire.md`) : BDIFF, Météo des forêts (MdF), EFFIS, SIM2, BD Forêt V2, Interventions SDIS, Statistiques nationales des SDIS, Données climatologiques quotidiennes (Climato).

| Question | BDIFF | Météo des forêts | EFFIS | SIM2 | BD Forêt V2 | Interventions SDIS | Statistiques SDIS | Climato quotidiennes |
|---|---|---|---|---|---|---|---|---|
| 1 | **partiel** : la colonne « date de première alerte » donne les jours de feu, mais pas le niveau de danger. Sur la période de la MdF (juin-sept. 2024 et 2025), seulement 2 feux en Côte-d'Or (fiche BDIFF, « Ce que j'ai découvert »). | **partiel** : `niveau_j1` par `num_dep` et `date`, mais seulement depuis le 3 juin 2024 et de fin mai à début octobre (rubrique « Période »). Le sens de `niveau_j1` reste à vérifier. | **inconnu** : le FWI existe pour des jours passés, mais ni sa période ni sa conversion au département n'ont été vérifiées (rubriques « Période » et « Clés »). | **partiel** : température, pluie, vent et humidité par point de grille et par `DATE`, depuis 1958. Ce n'est pas le niveau de danger, c'est une donnée indirecte (rubrique « Questions »). | **absent** : état de la forêt en 2017, sans date de feu ni niveau de danger (rubrique « Période »). | **absent** : un total par département et par an, sans le jour (rubrique « Grain »). | **absent** : des totaux annuels en PDF, sans le jour (rubrique « Grain »). | **partiel** : `TX`, `RR`, `UN` et `FFM` par station et par `AAAAMMJJ`, toute l'année depuis 1950, et les 120 jours de feu sont couverts. Mais ce ne sont pas les niveaux de la MdF, c'est une donnée indirecte (rubrique « Questions »). |
| 2 | **partiel** : la date de première alerte donne la part des feux couverts par un seuil, avec le même manque de recouvrement qu'en question 1. | **partiel** : `niveau_j1` permet de compter les jours au-dessus de chaque seuil, mais seulement sur 2 saisons complètes (2024 et 2025). Exemple en 2026 : 16 jours au niveau 3. | **inconnu** : mêmes raisons qu'en question 1. | **partiel** : donnée indirecte, comme en question 1. | **absent** : pas de jour ni de coût. | **absent** : pas de jour ni de coût d'un dispositif. | **absent** : les dépenses de fonctionnement du SDIS sont des totaux annuels (34 M€ en 2022), pas le coût d'une journée de dispositif renforcé (rubrique « Ce que j'ai découvert »). | **partiel** : donnée indirecte, comme en question 1. Rien sur le coût. |
| 3 | **partiel** : le code INSEE et le nom de la commune, plus les surfaces parcourues, sont donnés pour chaque feu. Mais la localisation s'arrête à la commune, sans coordonnées. Il n'y a que 120 feux, presque aucun avant 2015, et la colonne « Nature » (cause) est vide pour 100 feux sur 120. | **absent** : un niveau par département, sans zone plus fine (rubrique « Grain »). | **inconnu** : les zones brûlées 2018-2025 existent en Shapefile, mais n'ont pas été ouvertes. Les petits feux de chez nous ne sont peut-être pas vus par le satellite (rubrique « Ce que j'ai remarqué »). | **absent** : météo seulement, pas de feux. | **partiel** : les colonnes `TFV` et `ESSENCE` donnent la forêt et son type, mais il n'y a ni code commune ni massif. La jointure se fait par la position, sur un état de 2017 (rubrique « Clés »). | **absent** : un total par département, pas par zone. | **absent** : un total par département, pas par zone. | **absent** : météo seulement, pas de feux. |
| 4 | **partiel** : le code département et la date de première alerte sont donnés pour toute la France. Mais il n'y a pas le niveau de danger, et le recouvrement avec la MdF est court (43 feux en BFC et 2 632 en France sur les étés 2024-2025). | **partiel** : `num_dep` couvre les 96 départements métropolitains, mais seulement depuis 2024 et l'été seulement (rubriques « Emprise » et « Période »). | **inconnu** : mêmes raisons qu'en question 1. L'Excel est par pays, pas par département. | **partiel** : la table `SHP_SIM_FRANCE` donne `num_dep` pour tous les départements, mais c'est une donnée indirecte. | **absent** : rien sur le lien entre l'indice et les feux. | **partiel** : la colonne « Feux de végétations » est donnée par département et par an, mais ce ne sont pas seulement des feux de forêt, il n'y a pas le jour, et la structure change selon les années. | **partiel** : une comparaison des départements entre eux, mais en PDF, par an et sans lien avec l'indice. | **partiel** : il existe un fichier par département (découpage des fichiers, rubrique « Mode d'accès »), mais c'est une donnée indirecte. |

### Écarts avec la section 4

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1 | Météo des forêts croisée avec la BDIFF | un jour × une zone de prévision → un jour × un département | au moins 10 saisons feux → 2 saisons croisables (juin 2024 à octobre 2025), été seulement | jusqu'à la saison 2026 → 2025 pour la BDIFF (2026 n'est pas publiée) | = (Côte-d'Or), mais seulement 2 feux sur la période |
| 2 | Météo des forêts croisée avec la BDIFF | = (un jour × un département, comme en question 1) | au moins 10 saisons feux → 2 saisons | saison 2026 et coûts 2027 → feux jusqu'à 2025, aucun coût | = (Côte-d'Or) |
| 3 | BDIFF, avec la BD Forêt V2 | un départ de feu → un feu classé « forêt » seulement, localisé à la commune et sans coordonnées | au moins 10 ans → 2006-2025, mais le premier feu date de 2012 et les données sont faibles avant 2015 | jusqu'à la saison 2026 → 2025 ; la forêt dans son état de 2017 | = (communes de Côte-d'Or) ; pas de découpage en massifs |
| 4 | Météo des forêts croisée avec la BDIFF | = (un jour × un département) | même période pour tous → = (les mêmes dates pour tous), mais seulement 2 saisons | jusqu'à la saison 2026 → 2025 pour la BDIFF | = (8 départements de BFC et France métropolitaine) |

### Décisions

Aucune question n'a de source « complet ». La cellule EFFIS est « inconnu » pour les quatre questions : la première étape est donc de **vérifier** dans EFFIS la période du FWI et la possibilité de le ramener au département, avant de trancher.

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1 | Assez de jours où l'on connaît à la fois le niveau de la MdF et les feux en Côte-d'Or : seulement 2 feux sur la période commune | renoncer (reformuler) : calculer la part de jours avec feu par niveau sur la **Bourgogne-Franche-Comté** (43 feux, 37 jours) au lieu de la Côte-d'Or seule | C'est le seul moyen d'utiliser le vrai niveau de la MdF avec un nombre de feux qui n'est pas ridicule | On ne mesure plus la Côte-d'Or seule. On suppose que l'indice se comporte de la même façon dans toute la région, ce que la question 4 doit justement vérifier. 37 jours de feu restent peu. |
| 1 | Le niveau de danger avant juin 2024 et au printemps (32 feux sur 120 en mars-avril) | approximer : construire des indicateurs à partir des données climatologiques quotidiennes (`TX`, `RR`, `UN`, nombre de jours sans pluie) pour les jours de feu et les jours sans feu, de 2012 à 2025 | C'est la seule source qui couvre toute l'année, sur toute la période de la BDIFF, au grain du jour | Ces indicateurs mesurent la météo, pas le niveau officiel de la MdF : ils ne disent pas directement quel seuil choisir. Le vent et l'humidité ne sont mesurés que par quelques stations (9 et 14). |
| 2 | Le coût d'une journée de dispositif renforcé et le budget 2027 | collecter : les demander au SDIS 21, notre commanditaire | Ce sont des données internes : aucune source ouverte ne les donne | Cela dépend du délai de réponse du SDIS 21. Sans réponse, on ne peut exprimer le coût qu'en **nombre de jours** de dispositif, pas en euros. |
| 2 | Plus de 2 saisons de niveaux de la MdF pour compter les jours par seuil | approximer : mêmes indicateurs climatologiques qu'en question 1, ou le FWI d'EFFIS si la vérification est concluante | La MdF n'a que 2 saisons complètes | Un nombre de jours calculé avec un proxy n'est pas exactement le nombre de jours où le seuil MdF aurait été atteint. |
| 3 | Les coordonnées du départ de feu et un découpage en massifs forestiers | approximer : utiliser la **commune** comme zone, et la BD Forêt V2 pour situer les forêts dans chaque commune | La BDIFF ne localise qu'à la commune, et aucune source ne donne de massifs officiels | Une grande commune peut regrouper des feux éloignés les uns des autres. La forêt est dans son état de 2017. Avec 120 feux, beaucoup de communes n'en ont qu'un seul. |
| 4 | Un historique commun plus long que 2 saisons pour comparer les départements | approximer : comparer la Côte-d'Or, la BFC et la France sur les étés 2024-2025 avec la MdF, puis sur 2012-2025 avec les indicateurs climatologiques (un fichier par département) | La MdF et la BDIFF ont la même emprise, mais une période commune très courte | Sur 2 saisons, une différence entre départements peut venir du hasard. Le proxy climatologique ne compare pas le même indice que celui utilisé par la direction. |
