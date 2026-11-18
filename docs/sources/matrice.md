# Matrice questions × sources – v0

Exercice 3, partie B. Construite à partir des sections 5 des quatre analyses (`docs/analyse/commande-*.md`) et des fiches d'identité de `docs/sources/`.

Dernière mise à jour : 2026-11-18

## 1. Les questions retenues par le groupe

Les 16 questions des quatre analyses sont regroupées en 11 questions. Quand plusieurs membres ont posé la même question, elles sont fusionnées et leurs auteurs sont indiqués.

| # | Question du groupe | Décision de la direction qu'elle éclaire | Auteurs |
|---|---|---|---|
| G1 | Où se concentrent les départs de feu et les surfaces brûlées en Côte-d'Or (communes, massifs) ? | Où concentrer les moyens | Jane Q1, Audrey Q3 |
| G2 | À quels mois de l'année partent les feux en Côte-d'Or ? | Quand renforcer le dispositif | Aissatou Q2 |
| G3 | À quelles heures et quels jours de la semaine partent les feux ? | Sur quels créneaux renforcer | Melvyn Q1 |
| G4 | Pour chaque niveau de l'indice, quelle part des jours a connu au moins un départ de feu ? | À quel seuil déclencher | Audrey Q1, Jane Q2 |
| G5 | Pour chaque seuil possible, combien de jours de dispositif renforcé par saison, et quelle part des feux couverts ? | À quel seuil déclencher, dans la limite du budget | Audrey Q2, Jane Q2 |
| G6 | À partir de quel niveau de l'indice les feux deviennent-ils gros ? | À quel seuil déclencher | Aissatou Q3 |
| G7 | Les feux partis par indice bas ont-ils des points communs (moment, lieu, taille, cause) ? | Baisser le seuil ou faire de la prévention | Jane Q3 |
| G8 | Le lien entre l'indice et les feux est-il le même en Côte-d'Or, dans la région et en France ? | Seuil propre à la Côte-d'Or ou seuil de référence | Audrey Q4, Jane Q4, Aissatou Q4, Aissatou Q1 (reformulée par département) |
| G9 | Les feux qui deviennent gros sont-ils ceux où les secours arrivent le plus tard ? | Où prépositionner des moyens | Melvyn Q2 |
| G10 | Où un feu ferait-il le plus de dégâts (forêts proches des habitations, des routes) ? | Où concentrer la prévention | Melvyn Q3 |
| G11 | Le nombre de jours de danger élevé augmente-t-il d'un été à l'autre ? | Combien de jours de renfort prévoir au budget | Melvyn Q4 |

## 2. La matrice

Degrés : **complet** (la source répond au grain, sur la période et l'emprise voulus), **partiel**, **absent**, **inconnu** (non vérifié). Chaque degré renvoie à une rubrique de la fiche de la source ou à une colonne du fichier.

Les trois dernières sources de l'inventaire (Données climatologiques, Copernicus EWDS, Admin Express) ont été ajoutées après les sections 5 individuelles : leurs degrés ont été établis par le groupe à partir de leurs fiches.

| Question | BDIFF | Météo des forêts | EFFIS | Copernicus EWDS | SIM2 | Données climatologiques | BD Forêt V2 | Admin Express | Interventions SDIS | Stats nationales SDIS |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1** Où | partiel : code INSEE de la commune et surfaces de chaque feu, mais pas de coordonnées, 120 feux et pas l'été 2026 (Grain, Période) | absent : un niveau par département, aucun feu (Grain) | inconnu : zones brûlées 2018-2025 non ouvertes (Ce que j'ai remarqué) | absent : un indice, aucun feu (Grain) | absent : météo, aucun feu (Grain) | absent : météo, aucun feu (Grain) | partiel : forêts et essences (`TFV`, `ESSENCE`), état 2017, sans code commune (Période, Clés) | partiel : contours et `code_insee` des communes, pour rapporter les feux à la surface de forêt (Grain, Clés) | absent : un total par département et par an (Grain) | absent : un total par département et par an (Grain) |
| **G2** Mois | **complet** : date de première alerte de chaque feu, 2006-2025, toute l'année, Côte-d'Or (Grain, Période, Emprise) | absent : niveaux de danger, aucun feu (Grain) | inconnu : dates des zones brûlées non vérifiées | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : référentiel, aucun feu (Grain) | absent : un total par an, pas de mois (Grain) | absent : un total par an, pas de mois (Grain) |
| **G3** Heures, jours | partiel : heure de première alerte, mais 120 feux et pas l'été 2026 (Grain, Volumétrie) | absent : aucun feu (Grain) | absent : aucun feu à l'heure (Grain) | absent : une valeur par jour, aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : un total par an (Grain) | absent : un total par an (Grain) |
| **G4** Feux par niveau | partiel : jours de feu (date de première alerte), sans niveau d'indice (Grain) | partiel : `niveau_j1` par département et par jour, mais depuis juin 2024 et l'été seulement (Période) | partiel : FWI en images, sans département (Grain, Clés) | partiel : IFM (`fwinx`) chaque jour depuis 1940, toute l'année, mais valeur continue (pas un niveau de 1 à 4) et grille sans département (Grain, Clés) | partiel : météo par jour, donnée indirecte (Questions) | partiel : météo réelle des 120 jours de feu, donnée indirecte (Questions) | absent : aucun feu ni indice (Grain) | partiel : référentiel pour ramener les mailles au département (Clés) | absent : pas de jour (Grain) | absent : pas de jour (Grain) |
| **G5** Seuil × budget | partiel : jours de feu, sans niveau ni coût (Grain) | partiel : `niveau_j1` permet de compter les jours au-dessus d'un seuil, mais 2 saisons complètes (Période) | partiel : FWI en images (Grain) | partiel : IFM sur de nombreuses saisons pour compter les jours au-dessus d'un seuil, mais valeur continue et aucun coût (Grain) | partiel : donnée indirecte (Questions) | partiel : donnée indirecte (Questions) | absent : ni jour ni coût (Grain) | partiel : référentiel (Clés) | absent : ni jour ni coût (Grain) | absent : dépenses annuelles du SDIS, pas le coût d'une journée de dispositif (Ce que j'ai découvert) |
| **G6** Taille des feux × niveau | partiel : surfaces parcourues de chaque feu, mais 63 sur 120 estimées et définitions changées en 2023 (Grain, Ce que j'ai découvert) | partiel : `niveau_j1`, mais 2 feux en Côte-d'Or sur la période commune (Période) | partiel : FWI en images (Grain) | partiel : IFM le jour de chacun des 120 feux, mais valeur continue et grille (Grain, Clés) | partiel : conditions météo du jour, donnée indirecte (Questions) | partiel : météo réelle du jour de chaque feu, donnée indirecte (Questions) | absent : aucun feu (Grain) | partiel : référentiel (Clés) | absent : pas de surface (Grain) | absent : pas de surface par feu (Grain) |
| **G7** Feux par indice bas | partiel : heure, commune et surface de chaque feu, mais cause vide pour 100 feux sur 120 (colonne « Nature ») | partiel : `niveau_j1`, mais pas au printemps, alors que 32 feux sur 120 sont en mars-avril (Période) | partiel : FWI en images (Grain) | partiel : IFM toute l'année, printemps compris, pour repérer les feux par indice bas, mais valeur continue (Grain, Période) | partiel : météo de chaque jour, donnée indirecte (Grain) | partiel : météo réelle de chaque jour de feu, toute l'année, donnée indirecte (Période, Questions) | absent : aucun feu (Grain) | partiel : référentiel (Clés) | absent : un total par an (Grain) | absent : un total par an (Grain) |
| **G8** Côte-d'Or, région, France | partiel : toute la France avec la date de chaque feu, mais recouvrement court avec la Météo des forêts (Emprise, Période) | partiel : 96 départements jour par jour, mais 3 saisons (Emprise, Période) | partiel : FWI en images ; l'Excel est par pays (Grain, Clés) | partiel : IFM sur toute l'Europe depuis 1940, à ramener aux départements (Emprise, Clés) | partiel : `num_dep` par la table `SHP_SIM_FRANCE`, donnée indirecte (Clés) | partiel : un fichier par département, donnée indirecte (Mode d'accès) | absent : aucun feu ni indice (Grain) | partiel : contours des départements pour moyenner les mailles (Grain) | partiel : « Feux de végétations » par département et par an, sans jour ni indice (Grain) | absent : aucun nombre de feux par département (Grain) |
| **G9** Délai des secours | partiel : heure d'alerte et surface, mais pas d'heure d'arrivée des secours (Grain) | absent : aucun feu (Grain) | absent : aucune intervention (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : aucun feu (Grain) | absent : totaux annuels, pas de délai (Grain) | absent : pas de délai par feu (Grain) |
| **G10** Dégâts possibles | partiel : commune de chaque feu, mais colonnes de dégâts vides en Côte-d'Or (Clés, Grain) | absent : rien de plus fin que le département (Grain) | inconnu : zones habitées citées par la liste du défi, non vérifiées | absent : aucun enjeu (Grain) | absent : météo (Grain) | absent : météo (Grain) | partiel : forêts et leur type, état 2017, sans habitations ni routes (Grain, Période) | partiel : colonne `population` de chaque commune, mais pas la localisation des habitations ni des routes (Grain) | absent : un total par département (Grain) | absent : un total par département (Grain) |
| **G11** Jours de danger d'un été à l'autre | absent : des feux, pas de niveau de danger (Grain) | partiel : `niveau_j1`, mais 3 étés seulement (Période) | partiel : FWI en images, années anciennes sur demande (Grain, Clés) | **complet** : colonne `fwinx` (IFM) chaque jour de 1940 à 2026, sur une grille qui couvre la Côte-d'Or et la région (Période, Emprise). Il reste à fixer la valeur d'IFM qui correspond à un « danger élevé » | partiel : chaleur, pluie, humidité et sécheresse des sols depuis 1958, mais pas d'indice (`TSUP_H`, `PRELIQ`, `HU`, `SSWI_10J`) | partiel : météo réelle depuis 1950, donnée indirecte (Questions) | absent : aucun indice (Grain) | partiel : référentiel (Clés) | absent : interventions par an (Grain) | absent : interventions et moyens par an (Grain) |

## 3. Les désaccords tranchés

Quand les sections 5 donnaient des degrés différents pour la même case, le groupe est retourné à la fiche :

| Case | Degrés des sections 5 | Degré retenu | Raison |
|---|---|---|---|
| EFFIS, questions sur l'indice (G4 à G8) | inconnu (Audrey) ; partiel (Jane, Aissatou) | **partiel** | La fiche EFFIS (rubriques Grain et Clés) vérifie que le FWI existe en images, sans département. La fiche Copernicus EWDS confirme que c'est le même indice. |
| SIM2, G8 | partiel (Audrey) ; absent (Aissatou) | **partiel** | La fiche SIM2 (rubrique Clés) donne `num_dep` pour chaque point par la table `SHP_SIM_FRANCE` : une comparaison indirecte entre départements est possible. |
| Stats nationales SDIS, G8 | partiel (Audrey) ; absent (Aissatou) | **absent** | La fiche (rubrique Grain et « Ce que j'ai découvert ») montre que la plaquette ne contient aucun nombre de feux par département : elle compare des moyens, pas le lien entre l'indice et les feux. |

## 4. Lecture dans les deux sens

### Questions sans source « complet » : les manques

Seules **G2** (BDIFF) et **G11** (Copernicus EWDS) ont une source « complet ». Pour les autres :

| Question | Ce qui manque | Piste de décision |
|---|---|---|
| G1 | La localisation précise des feux (la BDIFF s'arrête à la commune) | **approximer** : la commune comme zone, rapportée à la surface de forêt (BD Forêt V2 + Admin Express) |
| G3 | Assez de feux (120 en Côte-d'Or) | **approximer** : élargir à la région |
| G4, G6, G7, G8 | Un indice sur une longue période, exprimé en niveaux | **approximer** : l'IFM de Copernicus EWDS sur 2012-2025, traduit en niveaux en le comparant à la Météo des forêts sur 2024-2026 |
| G5 | Le coût d'une journée de dispositif renforcé et le budget 2027 | **collecter** : les demander au SDIS 21 ; sans réponse, exprimer le coût en nombre de jours |
| G9 | L'heure d'arrivée des secours | **collecter** auprès du SDIS 21, sinon **renoncer** |
| G10 | La localisation des habitations et des routes | **collecter** : explorer la BD TOPO (IGN, dans la liste du défi), ou **renoncer** faute de temps |

### Sources sans question : à écarter ou à interroger

| Source | Constat | Piste de décision |
|---|---|---|
| Statistiques nationales des SDIS | « absent » partout | **à interroger** : elle pourrait répondre à une question que nous n'avons pas posée, sur les **moyens** du SDIS 21 comparés aux autres départements (premier point de la commande). Sinon, à écarter. |
| Interventions SDIS | « partiel » seulement pour G8 | **à interroger** : comparer ses « feux de végétations » au nombre de feux de la BDIFF pour estimer la complétude de la BDIFF (question de qualité, non posée). |
| EFFIS | Remplacée par Copernicus EWDS pour l'indice ; zones brûlées « inconnu » | **à écarter** pour l'indice ; à vérifier seulement si les zones brûlées deviennent nécessaires. |
| SIM2 et Données climatologiques | Les deux donnent la météo de chaque jour (partiel indirect sur les mêmes questions) | **en partie redondantes** : n'en garder qu'une pour le pipeline. |

## 5. Suites à donner

- Chaque décision de la partie 4 est à consigner dans le journal des décisions, une entrée par décision (ticket #52).
- Termes à ajouter ou préciser dans le glossaire (ticket #47) : « départ de feu », « feu de forêt » et « feu de végétation » (BDIFF et Interventions SDIS ne comptent pas la même chose), « IFM » et « niveau de danger » (valeur continue et niveau de 1 à 4), « jour de feu ».
