# Analyse de la commande - Aissatou Diallo

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1. **Les communes de Côte-d'Or qui ont le plus de feux sont-elles aussi celles où la Météo des forêts annonce le plus souvent un danger élevé ?**
   - Si oui : l'indice suffit pour savoir où envoyer les moyens, la direction renforce là où l'indice est élevé.
   - Si non : certaines zones brûlent pour d'autres raisons (activité humaine, type de forêt), la direction doit les cibler en plus de l'indice.

2. **À quels mois de l'année les départs de feu se produisent-ils en Côte-d'Or ?**
   - S'ils se concentrent en juillet-août : la direction renforce le dispositif seulement sur ces semaines.
   - S'il y en a aussi au printemps : elle doit prévoir le renfort plus tôt et étaler son budget sur une période plus longue.

3. **À partir de quel niveau de la Météo des forêts les feux deviennent-ils gros (en surface brûlée) ?**
   - Si les gros feux n'arrivent qu'à partir d'un certain niveau : la direction fixe son seuil à ce niveau, quitte à laisser passer quelques petits feux faciles à éteindre.
   - Si des gros feux arrivent à tous les niveaux : l'indice ne suffit pas pour éviter les gros feux, et la direction doit garder des moyens prêts même par indice bas.

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
| 1 | Nombre de départs de feu par commune, et niveau de la Météo des forêts de chaque jour pour la zone où se trouve la commune | Une commune sur une année (nombre de feux + nombre de jours de danger élevé) | Les 10 dernières années au moins, sur la période où l'indice est disponible | Une mise à jour par an suffit (on étudie le passé) | Côte-d'Or, au niveau de la commune |
| 2 | Liste des départs de feu avec leur date (et si possible l'heure) | Un départ de feu | Les 10 dernières années au moins, toute l'année (pas seulement l'été) | Une mise à jour par an suffit | Côte-d'Or |
| 3 | Liste des feux avec leur surface brûlée, et le niveau de la Météo des forêts le jour et à l'endroit du feu | Un feu (surface brûlée + niveau de l'indice ce jour-là) | Toutes les années où l'indice est disponible, sur toute la saison | Une mise à jour par an suffit | Côte-d'Or |
| 4 | Même donnée que la question 3, mais pour tous les départements | Un jour dans un département (niveau de l'indice + nombre de feux) | La même période pour tous les départements, pour pouvoir comparer | Une mise à jour par an suffit | Les 8 départements de Bourgogne-Franche-Comté et toute la France |

Remarque : les questions 1, 3 et 4 demandent de **croiser deux données** (l'indice et les feux). Il faudra pouvoir les relier par la **date** et par la **zone** (département ou commune) : ce seront nos clés de jointure.

## 5. Confrontation de mes questions aux sources

Degrés : **complet** (la source répond au grain, sur la période et l'emprise voulus), **partiel**, **absent**, **inconnu**. Chaque degré renvoie à une rubrique d'une fiche de `docs/sources/` ou à une colonne de fichier.

### 5.1 Ma matrice

| Question | BDIFF | Météo des forêts | EFFIS | SIM2 | BD Forêt V2 | Interventions SDIS | Stats nationales SDIS |
|---|---|---|---|---|---|---|---|
| Q1 Communes avec le plus de feux et indice élevé | partiel (a) | partiel (b) | partiel (c) | absent | absent | absent | absent |
| Q2 Mois des départs de feu | **complet (d)** | absent | inconnu (e) | absent | absent | absent | absent |
| Q3 Niveau de l'indice et taille des feux | partiel (f) | partiel (g) | partiel (c) | partiel (h) | absent | absent | absent |
| Q4 Erreurs de l'indice en Côte-d'Or et ailleurs | partiel (i) | partiel (j) | partiel (c) | absent | absent | partiel (k) | absent (l) |

### 5.2 Raisons

- **(a)** Fiche BDIFF, rubrique Grain : chaque feu a son **code INSEE de commune**. Mais la BDIFF ne contient pas le niveau de l'indice, et la rubrique Période indique seulement 120 feux en Côte-d'Or de 2006 à 2025, presque aucun avant 2015.
- **(b)** Fiche Météo des forêts, rubrique Grain : **un niveau par département et par jour** (colonne `num_dep`). Toutes les communes de Côte-d'Or ont donc le même niveau : impossible de comparer les communes entre elles. Rubrique Période : seulement depuis juin 2024.
- **(c)** Fiche EFFIS, rubriques Grain et Clés : l'indice FWI existe sur une grille de 8 km, donc plus fin que le département, mais **sous forme d'images**, sans code commune ni département. Les années anciennes sont sur demande, avec un délai inconnu.
- **(d)** Fiche BDIFF, rubrique Grain : colonne **date et heure de première alerte** pour chaque feu ; rubrique Période : **2006 à 2025** ; rubrique Emprise : la commune. C'est la donnée idéale décrite en section 4 (un départ de feu, 10 ans au moins, Côte-d'Or). La fiche donne même la répartition par mois en Côte-d'Or (12 en mars, 20 en avril, 31 en juillet, 33 en août…). Limite : le producteur demande de la prudence sur les feux d'avant 2020 hors de l'aire méditerranéenne.
- **(e)** Fiche EFFIS : la carte des zones brûlées couvre 2018 à 2025, mais la fiche n'a pas vérifié si chaque zone a une date, ni si les petits feux de Côte-d'Or y apparaissent.
- **(f)** Fiche BDIFF, rubrique Grain : colonnes de **surfaces parcourues** (en m²) pour chaque feu. Mais pas de niveau d'indice, 63 surfaces sur 120 sont estimées, et les définitions des surfaces ont changé en 2023.
- **(g)** Fiche Météo des forêts, colonne `niveau_j1` : le niveau de chaque jour. Mais rubrique Période : depuis juin 2024 seulement, et uniquement de fin mai à début octobre. D'après la fiche BDIFF, il n'y a que **2 feux en Côte-d'Or** sur la période commune aux deux sources.
- **(h)** Fiche SIM2, rubrique Questions : température, pluie, vent et sécheresse des sols chaque jour depuis 1958, sur une grille de 8 km. Cela décrit les conditions du jour d'un feu, mais **ce n'est pas le niveau de l'indice** : donnée indirecte.
- **(i)** Fiche BDIFF, rubrique Emprise : France entière, avec la date de chaque feu. Mais sur la période commune avec la Météo des forêts, il n'y a que 2 feux en Côte-d'Or (43 en Bourgogne-Franche-Comté, 2 632 en France).
- **(j)** Fiche Météo des forêts, rubrique Emprise : les **96 départements de métropole**, jour par jour. Mais seulement trois saisons (2024 à 2026), sans le printemps.
- **(k)** Fiche Interventions SDIS, rubrique Grain : **un département sur une année**, colonne « Feux de végétations ». On peut comparer les départements, mais sans jour, sans indice, et ces feux ne sont pas tous des feux de forêt.
- **(l)** Fiche Statistiques nationales SDIS, rubrique Grain : les annexes donnent les interventions, les effectifs et les budgets par département, mais **aucun nombre de feux par département**.

Les autres cases « absent » ont la même raison (rubrique Grain de chaque fiche) : SIM2 = météo sur une grille, aucun feu ; BD Forêt V2 = zones de végétation, aucun feu ni indice ; Interventions SDIS et Stats nationales SDIS = un département sur une année, ni commune, ni mois, ni surface ; Météo des forêts pour Q2 = des niveaux de danger, aucun feu.

### 5.3 Décisions

| Question | Source « complet » ? | Décision | Ce qu'on fait | Ce que ça coûte |
|---|---|---|---|---|
| Q1 | Non | **renoncer (reformuler)** | Comparer les **départements** de la région au lieu des communes : les départements avec le plus de feux (BDIFF) sont-ils ceux où l'indice est le plus souvent élevé (Météo des forêts) ? | On perd le détail à l'intérieur de la Côte-d'Or, qui était le cœur de la question. Et la comparaison ne porte que sur les étés 2024 à 2026 |
| Q2 | Oui (BDIFF) | — | Répondre avec la BDIFF, colonne date de première alerte | Prudence sur les années avant 2015, où peu de feux sont saisis |
| Q3 | Non | **approximer** | Utiliser les feux de la **région, voire de la France**, comme approximation de la Côte-d'Or, sur les étés 2024 et 2025 | La région ou la France ne réagissent peut-être pas comme la Côte-d'Or. Et les feux de printemps restent hors de l'analyse |
| Q4 | Non | **approximer** | Comparer la Côte-d'Or, la région et la France sur les **seuls étés 2024 et 2025**, période où les deux sources se recouvrent | Deux saisons seulement : le résultat sera fragile. Les feux partis hors saison (printemps) ne peuvent pas être comparés à l'indice |

### 5.4 Ce qui a changé par rapport à mes prédictions (section 4)

- J'avais supposé que l'indice existait **par zone fine** : il n'existe que par **département**. C'est ce qui fait tomber ma question 1.
- J'avais demandé « toutes les années où l'indice est disponible » sans savoir que cela ne fait que **trois étés** : c'est le principal manque pour mes questions 3 et 4.
- Je pensais que mes deux sources (Interventions SDIS et Stats nationales SDIS) aideraient pour la question 4 : en confrontant, la plaquette des Stats nationales ne contient finalement **aucun feu par département**.
- Ma seule question entièrement couverte (Q2, les mois) est aussi celle qui éclaire le mieux la commande : une partie des feux de Côte-d'Or a lieu au **printemps**, quand la Météo des forêts n'est pas publiée.
