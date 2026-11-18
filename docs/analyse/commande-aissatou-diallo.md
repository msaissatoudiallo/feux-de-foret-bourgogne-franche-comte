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

## 5. Confrontation aux sources

Degrés : **complet**, **partiel**, **absent**, **inconnu**. Chaque raison renvoie à une rubrique d'une fiche de `docs/sources/` ou à une colonne de fichier.

### Matrice

| Question | BDIFF | Météo des forêts | EFFIS | SIM2 | BD Forêt V2 | Interventions SDIS | Stats nationales SDIS |
|---|---|---|---|---|---|---|---|
| 1. Communes avec le plus de feux et indice élevé | partiel : chaque feu a son code INSEE de commune (rubrique Grain), mais pas de niveau d'indice | partiel : un seul niveau par département et par jour, colonne `num_dep` (rubrique Grain) : impossible de comparer les communes | partiel : FWI sur une grille de 8 km, mais en images, sans code commune ni département (rubriques Grain et Clés) | absent : météo sur une grille, aucun feu ni indice (rubrique Grain) | absent : zones de végétation, aucun feu ni indice (rubrique Grain) | absent : un département sur une année, pas de commune (rubrique Grain) | absent : un département sur une année, pas de commune (rubrique Grain) |
| 2. Mois des départs de feu | **complet** : colonne date et heure de première alerte pour chaque feu (rubrique Grain), 2006 à 2025 (rubrique Période), Côte-d'Or par commune (rubrique Emprise) | absent : des niveaux de danger, aucun feu (rubrique Grain) | inconnu : la carte des zones brûlées 2018-2025 n'a pas été vérifiée (date de chaque zone, petits feux visibles ?) | absent : météo sur une grille, aucun feu (rubrique Grain) | absent : zones de végétation, aucun feu (rubrique Grain) | absent : un seul total par an, pas de mois (rubrique Grain) | absent : un seul total par an, pas de mois (rubrique Grain) |
| 3. Niveau de l'indice et taille des feux | partiel : colonnes de surfaces parcourues pour chaque feu (rubrique Grain), mais pas de niveau d'indice ; 63 surfaces sur 120 estimées | partiel : colonne `niveau_j1`, mais seulement depuis juin 2024 et de fin mai à début octobre (rubrique Période) : 2 feux en Côte-d'Or sur la période commune | partiel : FWI sur plusieurs années, mais en images et sans département (rubriques Grain et Clés) | partiel : température, pluie, vent et sécheresse des sols depuis 1958 (rubrique Questions) : conditions du jour, mais pas le niveau de l'indice | absent : zones de végétation, aucun feu (rubrique Grain) | absent : pas de surface, pas d'indice (rubrique Grain) | absent : pas de surface par feu, pas d'indice (rubrique Grain) |
| 4. Erreurs de l'indice en Côte-d'Or et ailleurs | partiel : France entière avec la date de chaque feu (rubrique Emprise), mais seulement 2 feux en Côte-d'Or, 43 dans la région et 2 632 en France sur la période commune avec l'indice | partiel : les 96 départements de métropole, jour par jour (rubrique Emprise), mais trois saisons seulement, sans le printemps (rubrique Période) | partiel : FWI sur plusieurs années, mais en images et sans département (rubriques Grain et Clés) | absent : pas de niveau d'indice ni de feu (rubrique Grain) | absent : aucun feu ni indice (rubrique Grain) | partiel : colonne « Feux de végétations » par département et par an (rubrique Grain), mais sans jour ni indice, et pas seulement des feux de forêt | absent : les annexes donnent interventions, effectifs et budgets, mais aucun nombre de feux par département (rubrique Grain) |

### Écarts avec la section 4

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1 | BDIFF + Météo des forêts | indice par zone fine → **indice par département seulement** | 10 ans au moins → feux 2006-2025 (peu avant 2015), indice **depuis juin 2024** | = | Côte-d'Or par commune → feux par commune, mais indice **par département** |
| 2 | BDIFF | = | 10 ans au moins, toute l'année → 2006-2025, toute l'année (mais peu de feux saisis avant 2015) | = (publication annuelle après validation) | = |
| 3 | BDIFF + Météo des forêts | = (un feu, relié au niveau du jour par la date et le département) | toutes les années de l'indice, toute la saison → **étés 2024 et 2025 seulement** (2026 pas encore publié dans la BDIFF) | = | Côte-d'Or → **2 feux seulement** sur la période commune : il faut passer à la région ou à la France |
| 4 | BDIFF + Météo des forêts | = (un jour dans un département) | même période partout → = , mais **étés 2024 et 2025 seulement** | = | 8 départements de la région et toute la France → = pour la métropole (la Météo des forêts ne couvre pas l'outre-mer) |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1 | Un niveau d'indice plus fin que le département | **renoncer** (reformuler) | La Météo des forêts n'existe que par département. Je reformule : les **départements** de la région qui ont le plus de feux sont-ils ceux où l'indice est le plus souvent élevé ? | On perd le détail à l'intérieur de la Côte-d'Or, qui était le cœur de la question. La comparaison ne porte que sur les étés 2024 à 2026 |
| 2 | Rien : la BDIFF est « complet » | — | La colonne date de première alerte répond à la question | Prudence sur les années avant 2015, où peu de feux sont saisis |
| 3 | Assez de feux en Côte-d'Or sur la période où l'indice existe | **approximer** | Utiliser les feux de la **région, voire de la France**, à la place de ceux de la Côte-d'Or, sur les étés 2024 et 2025 | La région ou la France ne réagissent peut-être pas comme la Côte-d'Or. Les feux de printemps restent hors de l'analyse |
| 4 | Un historique de l'indice plus long que trois saisons | **approximer** | Comparer la Côte-d'Or, la région et la France sur les **seuls étés 2024 et 2025**, période où les deux sources se recouvrent | Deux saisons seulement : le résultat sera fragile. Les feux de printemps ne peuvent pas être comparés à l'indice |
