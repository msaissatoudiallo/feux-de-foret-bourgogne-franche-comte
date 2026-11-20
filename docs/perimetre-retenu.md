# Périmètre retenu : questions, hypothèses et sources (analyse SWOT)

Réduction validée par le groupe le 20/11/2026 (décision D020, ticket #104).

Les 11 questions du groupe (G1 à G11, `docs/sources/matrice.md`) sont trop nombreuses pour un tableau de bord, qui doit répondre à 3 questions avec 5 à 7 indicateurs (kit projet HETIC). Chaque question a été évaluée selon quatre critères :

- **Forces** : ce qui la rend faisable (données complètes, source fiable) ;
- **Faiblesses** : ses limites (peu de feux, proxy, données partielles) ;
- **Opportunités** : ce qu'elle apporte à la décision du SDIS 21 (où mettre les moyens, quel seuil) ;
- **Menaces** : ce qui peut la faire échouer avant le 11/12.

Les degrés de données viennent de la matrice ; les décisions citées, du journal.

## Analyse SWOT

| Question | Forces | Faiblesses | Opportunités | Menaces | Résultat |
|---|---|---|---|---|---|
| G1 Où partent les feux ? | Commune de chaque feu (BDIFF), forêt (BD Forêt V2), référentiel (Admin Express) | Pas de coordonnées, 120 feux, forêt de 2017 (D006) | Répond à la décision « où concentrer les moyens » | Jointure par la carte, communes fusionnées | Gardée, fusionnée avec G10 (R1) |
| G2 Quels mois ? | Source « complet » : BDIFF 2006-2025, toute l'année | Peu de feux par mois | Dit quand renforcer ; montre les feux de printemps (H4) | Aucune | Gardée, fusionnée avec G3 (R2) |
| G3 Quelles heures, quels jours ? | Heure d'alerte (BDIFF), région élargie (D007), fiche indicateur faite (H7) | 120 feux en Côte-d'Or ; heure d'alerte et non de départ | Créneaux de patrouille | Lien faible avec les deux décisions de la commande | Fusionnée avec G2 (R2) |
| G4 Feux par niveau d'indice | IFM chaque jour depuis 1940 (Copernicus EWDS), traduit en classes (D008) | L'IFM n'est pas le niveau officiel (proxy) | Cœur de la décision sur le seuil | Traduction IFM → niveau à vérifier | Gardée (R3) |
| G5 Seuil et jours de dispositif | Jours au-dessus de chaque seuil, comptés avec Copernicus EWDS | Pas de coût d'une journée de dispositif (D009) | Réponse concrète : quel seuil, pour combien de jours | Coût jamais reçu : raisonnement en jours | Gardée (R5) |
| G6 Taille des feux selon le niveau | Surface de chaque feu (BDIFF) | 63 surfaces sur 120 estimées ; définitions changées en 2023 | Seuil pour les gros feux | Résultats peu fiables avec si peu de feux | Fusionnée avec G4 (R3) |
| G7 Feux par indice bas | IFM toute l'année, printemps compris | Cause inconnue pour 100 feux sur 120 | Répond à la plainte des chefs de centre (commande) | Explication limitée sans la cause | Gardée (R4) |
| G8 Côte-d'Or, région, France | France entière dans la BDIFF, IFM sur toute l'Europe | Mailles à ramener aux départements | Sert de référence aux indicateurs | Volume des données France entière | Fusionnée avec G4 (R3) : la région et la France servent de référence |
| G9 Délai des secours | Aucune | Heure d'arrivée des secours absente (D010) | Prépositionner des moyens | Données internes du SDIS, jamais reçues | Écartée |
| G10 Dégâts possibles | Population (Admin Express), forêt (BD Forêt V2), fiche indicateur faite (H8) | Population comme proxy (D011) ; pas de routes | Où faire la prévention | Jointure par la carte, forêt de 2017 | Fusionnée avec G1 (R1) |
| G11 Jours de danger d'un été à l'autre | Source « complet » : IFM 1940-2026 (D012), fiche indicateur faite (H9) | L'IFM n'est pas le niveau officiel | Combien de jours prévoir au budget | Aucune majeure | Gardée (R6) |

## Les 6 questions retenues

| # | Question retenue | Regroupe | Décision éclairée |
|---|---|---|---|
| R1 | Où partent les feux, et où feraient-ils le plus de dégâts ? | G1, G10 | Où concentrer les moyens et la prévention |
| R2 | Quand partent les feux (mois, jours, heures) ? | G2, G3 | Quand renforcer |
| R3 | Comment l'indice se comporte-t-il face aux feux, en Côte-d'Or comparée à la région et à la France ? | G4, G6, G8 | À quel seuil déclencher |
| R4 | Pourquoi des feux partent-ils quand l'indice est bas ? | G7 | Baisser le seuil ou faire de la prévention |
| R5 | Quel seuil, pour combien de jours de dispositif par saison ? | G5 | À quel seuil déclencher, dans le budget |
| R6 | Les jours de danger élevé augmentent-ils d'un été à l'autre ? | G11 | Combien de jours prévoir au budget |

Écartée : G9 (délai des secours), faute de données (D010).

## Hypothèses

- H1, H2, H3, H4, H5, H8 et H9 sont gardées.
- H6 (la Côte-d'Or réagit à l'indice comme la région et la France) est intégrée à H2 : la région et la France deviennent la référence de H2.
- H7 (feux le week-end et les jours fériés) est gardée comme hypothèse secondaire, hors des indicateurs principaux du tableau de bord.
- Aucune hypothèse n'était rattachée à G9.

## Sources

| Source | Résultat | Raison |
|---|---|---|
| BDIFF | Retenue | Source des feux, pour toutes les questions |
| Copernicus EWDS | Retenue | L'indice, pour R3 à R6 |
| Météo des forêts | Retenue | Vérifier la traduction de l'IFM en niveaux (D008) |
| Admin Express | Retenue | Communes, population, référentiel des jointures (R1) |
| BD Forêt V2 | Retenue | Surface de forêt par commune (R1) |
| Données climatologiques | Retenue | Météo mesurée des jours de feu (R4, H5) |
| SIM2 | Écartée | Redondante avec les Données climatologiques, qui sont mesurées et non modélisées |
| Statistiques nationales des SDIS | Écartée | Ne sert à aucune question retenue |
| Interventions SDIS | Contrôle qualité | Comparer ses feux de végétation à la BDIFF (profil qualité, #42) ; pas une source du tableau de bord |
| EFFIS | Écartée | Déjà écartée pour l'indice (D013) |

## Pour la fiche de cadrage (ticket #105)

Proposition de passage aux 3 questions du tableau de bord, à finaliser par Jane :

| Question du tableau de bord | Questions retenues | Indicateurs possibles |
|---|---|---|
| Où en est-on ? | R1, R2, R6 | Nombre de feux et surface brûlée par an, comparés à la moyenne ; part des feux hors juin-septembre (H4) ; jours de danger élevé par été (H9) |
| Pourquoi ? | R3, R4 | Taux de jours avec feu par classe d'indice, Côte-d'Or comparée à la région (H2) ; part des feux partis par indice bas (H5) |
| Que fait-on ? | R5, R1 | Jours de dispositif par saison et part des feux couverts, pour chaque seuil (H3) ; part des feux dans les communes à fort enjeu (H8) |
