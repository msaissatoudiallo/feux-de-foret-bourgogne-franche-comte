# Spécification du projet – V1

**Projet :** Feux de forêt – Bourgogne-Franche-Comté (Hetic 2026/2027, UE01 – Modélisation et pipeline de données)
**Commanditaire :** direction du SDIS 21 (Côte-d'Or)
**Version :** V1 – 2026-11-19
**Rédaction :** Aissatou Diallo (cheffe de projet), avec Audrey, Jane et Melvyn

Ce document décrit le projet de bout en bout : la demande, le raisonnement, les données, l'architecture, la qualité et l'organisation. Il doit permettre à quelqu'un de refaire le projet sans poser de questions. Il ne recopie pas les autres documents : il les résume et y renvoie. Il est mis à jour à chaque milestone ; tout changement passe par un ticket, une pull request et, si besoin, une décision du journal.

| Document | Contenu |
|---|---|
| `docs/analyse/commande-*.md` | Les quatre analyses individuelles de la commande (questions, termes inconnus, besoins, données idéales, confrontation aux sources) |
| `docs/sources/fiche-*.md` | Une fiche d'identité par source |
| `docs/sources/inventaire.md` | La liste des sources explorées et leur bilan |
| `docs/sources/matrice.md` | La matrice questions × sources |
| `docs/journal-decisions.md` | Toutes les décisions du groupe (D001, D002…) |
| `docs/glossaire.md` | Le sens précis des termes du projet |

## 1. Contexte et commande

La direction du SDIS 21 prépare l'été 2027, où elle attend autant de feux de forêt que l'été 2026, voire davantage. Elle demande de l'aide pour arbitrer **deux décisions** :

1. **Où concentrer les moyens**, humains et financiers, pour lutter contre les départs de feu.
2. **À partir de quel niveau de la Météo des forêts** déclencher le dispositif renforcé (patrouilles, guet).

**Le problème signalé :** le seuil actuel ne convient pas. L'indice annonce souvent un danger élevé alors qu'aucun feu ne se déclare, et des feux partent des jours où l'indice est au plus bas. Le budget ne permet pas de renforcer partout, tout l'été.

**L'emprise :** la Côte-d'Or, comparée aux autres départements de Bourgogne-Franche-Comté et au reste du territoire national.

**L'échéance :** réponse attendue le **11 décembre 2026**.

## 2. La démarche

Le projet suit une démarche descendante, de la décision à la donnée :

```
Commande → Questions → Données idéales → Sources réelles → Matrice → Décisions
        → Hypothèses → Objectifs SMART → KPI → Entrepôt de données (bronze, silver, gold) → Réponse à la direction
```

1. Chaque membre a analysé la commande et formulé quatre questions qui mènent à une décision, avec la donnée idéale pour y répondre (exercice 1).
2. Le groupe a exploré les sources et rédigé une fiche d'identité par source (exercice 2).
3. Les questions ont été confrontées aux sources, individuellement puis dans la matrice du groupe ; chaque manque a donné lieu à une décision (exercice 3, journal D006 à D014).
4. Les hypothèses sont traduites en objectifs SMART et en KPI (partie 3).
5. Les données retenues sont chargées et transformées dans un entrepôt en trois couches (partie 6).

## 3. Hypothèses, objectifs SMART, données et KPI

Chaque hypothèse est testée par une ou plusieurs questions du groupe (partie 4). Un objectif SMART est **S**pécifique, **M**esurable, **A**tteignable, **R**éaliste et **T**emporellement défini.

| # | Hypothèse | Questions | Données | KPI |
|---|---|---|---|---|
| H1 | Les feux se concentrent sur quelques communes boisées. | G1 | BDIFF, BD Forêt V2, Admin Express | Part des feux dans les 10 % de communes les plus touchées ; nombre de feux par km² de forêt |
| H2 | Plus l'indice est élevé, plus il y a de feux. | G4, G8 | BDIFF, Copernicus EWDS, Météo des forêts | Taux de jours avec au moins un feu, pour chaque classe de danger |
| H3 | L'indice déclenche souvent pour rien. | G4, G5 | BDIFF, Copernicus EWDS, Météo des forêts | Taux de fausses alertes : part des jours en danger élevé ou plus sans aucun feu |
| H4 | Une part importante des feux a lieu hors de la période où la Météo des forêts est publiée. | G2 | BDIFF | Part des feux hors juin-septembre |
| H5 | Les feux partent par temps chaud et sec, même quand l'indice est bas. | G7 | BDIFF, Données climatologiques, Copernicus EWDS | Nombre de jours sans pluie avant un feu ; température maximale des jours de feu comparée aux jours sans feu |
| H6 | La Côte-d'Or réagit à l'indice comme la région et la France. | G8 | BDIFF, Copernicus EWDS, Admin Express | Taux de jours avec feu par classe de danger : Côte-d'Or, région, France |
| H7 | Les feux partent surtout à des moments liés à l'activité humaine : le week-end, les jours fériés et certaines heures de la journée. | G3 | BDIFF (date et heure de première alerte) ; jours fériés calculés par règle, sans source externe : 8 dates fixes (1er janvier, 1er mai, 8 mai, 14 juillet, 15 août, 1er novembre, 11 novembre, 25 décembre) et 3 dates liées à Pâques (lundi de Pâques, Ascension, lundi de Pentecôte) | Part des feux partis le week-end ou un jour férié ; part des feux dans le créneau horaire qui en concentre le plus |
| H8 | Les communes où un feu ferait le plus de dégâts, c'est-à-dire à la fois boisées et habitées, sont peu nombreuses. | G10 | Admin Express (`population`, `code_insee`, contours des communes) ; BD Forêt V2 (`TFV_G11` : forêts fermées et ouvertes, sans les landes ni les formations herbacées ; libellés exacts à relever dans le fichier) ; BDIFF (code INSEE de la commune de chaque feu, relié aux 698 communes actuelles par une table de passage des communes fusionnées) | Part des communes à fort enjeu (à la fois très boisées et habitées) ; part des feux survenus dans ces communes |

### Objectifs SMART définis

| Hypothèse | Objectif SMART | KPI et seuil de validation |
|---|---|---|
| H4 | D'ici le 27/11/2026, mesurer sur 2012-2025 la part des feux de Côte-d'Or survenus hors juin-septembre. Si elle dépasse 25 %, recommander d'étendre la surveillance au printemps. | Part des feux hors juin-septembre ; hypothèse confirmée si > 25 %. Première estimation d'après la fiche BDIFF : environ 30 % (à vérifier dans le fichier). |
| H2 et H3 | D'ici le 04/12/2026, déterminer pour la Bourgogne-Franche-Comté, sur 2012-2025, le seuil d'IFM qui couvre au moins 70 % des jours de feu tout en déclenchant le dispositif moins de 30 jours par saison en Côte-d'Or. | Taux de couverture des jours de feu ; nombre de jours de dispositif par saison ; taux de fausses alertes. Les valeurs de 70 % et 30 jours sont des propositions, à ajuster quand le coût du dispositif sera connu (D009). |
| H7 | D'ici le 27/11/2026, mesurer sur 2006-2025 la part des feux de Bourgogne-Franche-Comté (752 feux, D007) et de Côte-d'Or partis un samedi, un dimanche ou un jour férié, et la comparer à la part attendue si les feux étaient répartis au hasard sur la semaine (environ 30 %). Si elle est nettement plus élevée, recommander de renforcer la surveillance ces jours-là, en plus de l'indice. | Part des feux partis le week-end ou un jour férié ; hypothèse confirmée si elle est nettement supérieure à la part attendue (test binomial, seuil de 5 %, convention usuelle en statistique). KPI secondaire : part des feux dans le créneau horaire qui en concentre le plus (durée du créneau : paramètre à tester). Limite : l'heure de la BDIFF est celle de l'alerte, pas celle du départ du feu. |
| H8 | D'ici le 04/12/2026, classer les 698 communes de Côte-d'Or selon deux critères séparés : part de la surface couverte de forêt et population. Une commune est « à fort enjeu » si elle est au-dessus de la médiane pour les deux. Si ces communes sont nettement moins nombreuses que la part attendue si forêt et population n'avaient aucun lien (25 %), recommander d'y concentrer la prévention et la surveillance ; sinon, répartir les moyens selon la fréquence des feux (H1). | Part des communes à fort enjeu ; hypothèse confirmée si elle est nettement inférieure à 25 % (test binomial, seuil de 5 %, comme H7). Les deux critères restent séparés pour que les grandes communes ne dominent pas (une multiplication population × forêt donnerait toujours la même réponse) ; la médiane résiste aux valeurs extrêmes. KPI secondaire : part des feux de 2015-2025 survenus dans ces communes (2015-2025, car les feux d'avant 2015 sont mal saisis d'après la fiche BDIFF). Biais : la population est un proxy (D011), elle ne dit pas si les habitations sont proches de la forêt ; les routes ne sont pas prises en compte ; la forêt est dans son état de 2017. |

Les objectifs SMART des hypothèses H1, H5 et H6 seront définis pour le milestone V1.

## 4. Les questions retenues et leurs décisions

Les 16 questions des analyses ont été regroupées en 11 questions du groupe (détail et auteurs : `docs/sources/matrice.md`).

| # | Question | Décision de la direction éclairée | Traitement décidé |
|---|---|---|---|
| G1 | Où se concentrent les feux et les surfaces brûlées ? | Où concentrer les moyens | Approximer : la commune comme zone, rapportée à la surface de forêt (D006) |
| G2 | À quels mois partent les feux ? | Quand renforcer | Source complète : BDIFF |
| G3 | À quelles heures et quels jours de la semaine ? | Sur quels créneaux renforcer | Approximer : élargir à la région (D007) |
| G4 | Quelle part des jours a un feu, pour chaque niveau ? | Quel seuil | Approximer : IFM de Copernicus EWDS traduit en classes EFFIS (D008) |
| G5 | Combien de jours de dispositif et quelle part des feux couverts, pour chaque seuil ? | Quel seuil, dans le budget | Collecter le coût auprès du SDIS 21, sinon raisonner en nombre de jours (D009) ; indice comme en D008 |
| G6 | À partir de quel niveau les feux deviennent-ils gros ? | Quel seuil | Approximer (D008) |
| G7 | Les feux par indice bas ont-ils des points communs ? | Baisser le seuil ou faire de la prévention | Approximer (D008) |
| G8 | L'indice se comporte-t-il de la même façon en Côte-d'Or, dans la région et en France ? | Seuil propre ou seuil de référence | Approximer (D008) |
| G9 | Les gros feux sont-ils ceux où les secours arrivent le plus tard ? | Où prépositionner des moyens | Collecter auprès du SDIS 21, sinon renoncer au 02/12/2026 (D010) |
| G10 | Où un feu ferait-il le plus de dégâts ? | Où concentrer la prévention | Approximer par la population des communes ; BD TOPO reportée à V1 (D011) |
| G11 | Les jours de danger élevé augmentent-ils d'un été à l'autre ? | Combien de jours prévoir au budget | Source complète : Copernicus EWDS (D012) |

## 5. Les sources retenues

Toute source utilisée dans l'entrepôt ou l'analyse a une fiche d'identité dans `docs/sources/`.

| Source | Producteur | Rôle dans le projet | Statut |
|---|---|---|---|
| BDIFF | Ministère de l'Agriculture (portail IGN) | Les feux de forêt (date, commune, surface) : source centrale | Retenue. Licence : règle la plus stricte (D005) |
| Météo des forêts | Météo-France | Le niveau officiel de danger (1 à 4), depuis juin 2024 | Retenue, pour vérifier la traduction de l'IFM (D008) |
| Copernicus EWDS | Copernicus Emergency Management Service | L'IFM chaque jour depuis 1940 | Retenue (D008, D012) |
| Admin Express | IGN | Contours et codes des communes et des départements : référentiel des jointures | Retenue |
| BD Forêt V2 | IGN | Localisation et type des forêts (état 2017) | Retenue (D006, D011) |
| Données climatologiques quotidiennes | Météo-France | Météo mesurée par station, chaque jour depuis 1950 | En partie redondante avec SIM2 : une seule des deux sera retenue |
| SIM2 | Météo-France | Météo modélisée sur une grille de 8 km, chaque jour depuis 1958 | En partie redondante avec les Données climatologiques |
| Interventions SDIS | Ministère de l'Intérieur | Feux de végétation par département et par an | À interroger : contrôle de la complétude de la BDIFF |
| Statistiques nationales des SDIS | DGSCGC | Effectifs et budgets de chaque SDIS | À interroger : comparaison des moyens |
| EFFIS | JRC (Copernicus) | Même indice que Copernicus EWDS, en images | Écartée pour l'indice (D013) |

## 6. Architecture des données

### Principes

- **Trois couches** :
  - **bronze** : les fichiers des sources, tels quels, jamais modifiés ;
  - **silver** : les données nettoyées, testées sur les six dimensions de qualité et reliées par les clés ;
  - **gold** : les tables prêtes pour calculer les KPI et construire les visualisations.
- **Reconstruction automatique** : un script reconstruit toutes les couches depuis la couche bronze, sans intervention manuelle.
- **Idempotence** : relancer un chargement ne crée pas de doublons.
- **Données brutes hors du dépôt** : le dossier `data/raw/` est exclu de Git (dépôt public, licence de la BDIFF, D005).

### Les clés de jointure

| Clé | Format retenu | Sources concernées |
|---|---|---|
| Code INSEE de la commune | Texte, 5 caractères (`21329`) | BDIFF, Admin Express |
| Code du département | Texte, 2 caractères (`01`, `21`, `2A`) | Météo des forêts, Admin Express, Interventions SDIS, SIM2, Données climatologiques |
| Date | Date du jour (AAAA-MM-JJ), en heure française | Toutes les sources quotidiennes |
| Coordonnées | Mailles ou stations à rattacher aux communes ou aux départements par la carte | Copernicus EWDS, SIM2, Données climatologiques, BD Forêt V2 |

Points d'attention : codes de communes disparus après les fusions (6 en Côte-d'Or depuis 2017) ; département écrit sans zéro (`1`) dans le fichier 2025 de la Météo des forêts, et `2a` / `2b` dans les Statistiques des SDIS ; dates en UTC dans la Météo des forêts ; pour un feu du jour J, le niveau de la Météo des forêts se lit dans `niveau_j1` du bulletin de J-1.

### Schéma de l'entrepôt v0 (proposition, à compléter par l'équipe Modélisation, ticket #41)

| Table | Couche | Une ligne = | Clé primaire | Clés étrangères |
|---|---|---|---|---|
| `dim_date` | silver | un jour | `date` | — |
| `dim_departement` | silver | un département | `code_departement` | — |
| `dim_commune` | silver | une commune (édition COG de l'année) | `code_insee` | `code_departement` |
| `fait_feu` | silver | un feu de forêt (BDIFF) | `id_feu` (année + numéro) | `date_alerte`, `code_insee`, `code_departement` |
| `fait_danger_jour` | silver | un département pour un jour | (`code_departement`, `date`) | `code_departement`, `date` |
| `fait_meteo_jour` | silver | un département pour un jour | (`code_departement`, `date`) | `code_departement`, `date` |
| tables de KPI | gold | selon le KPI | — | — |

`fait_danger_jour` contiendrait le niveau de la Météo des forêts (depuis 2024), l'IFM moyen et maximal du département (Copernicus EWDS) et la classe de danger EFFIS.

## 7. Qualité des données

Chaque source est évaluée selon les **six dimensions** du cours : complétude (au niveau de la cellule, de la ligne et de la période), exactitude, cohérence, validité, unicité et actualité. Les profils détaillés sont en cours (tickets #42 pour la BDIFF, #43 pour la Météo des forêts). Problèmes déjà repérés dans les fiches :

| Source | Dimension | Problème repéré |
|---|---|---|
| BDIFF | Complétude | Cause du feu vide pour 100 feux sur 120 en Côte-d'Or ; très peu de feux avant 2015 (saisie incomplète d'après le producteur) |
| BDIFF | Exactitude | 63 surfaces sur 120 estimées ; définitions des surfaces changées en 2023 |
| Météo des forêts | Complétude (période) | Aucune donnée de mi-octobre à fin mai |
| Météo des forêts | Validité | Séparateur et format du département différents selon les années ; dates en UTC |
| Interventions SDIS | Validité | « ? » à la place du séparateur des milliers dans le fichier 2024 |
| Interventions SDIS | Cohérence | Structure différente selon les années (pas de détail des feux en 2011 et 2013) |
| Admin Express | Cohérence | Noms de colonnes différents selon l'édition ; codes disparus après les fusions de communes |

Les règles de qualité (tests automatiques et seuils de décision) seront définies par l'équipe Qualité pour le milestone V1.

## 8. Organisation du projet

**Rôles :** Aissatou Diallo, cheffe de projet (milestones, tickets, suivi, journal) ; Jane, responsable sources ; Melvyn, responsable qualité et conformité (règles de qualité, tests, données personnelles) ; Audrey, responsable pipeline et modèle (D002, D004).

**Équipes :** Modélisation (Audrey, Aissatou) et Qualité (Melvyn, Jane) (D004).

**Branches :**

```
main ← dev ← documentation   (documentation)
           ← modelisation    (équipe Modélisation)
           ← qualite         (équipe Qualité)
```

Une branche par ticket, créée depuis la branche de rassemblement concernée. Le travail remonte par pull request, relue et validée par le ou la responsable du domaine concerné, jamais par son auteur (D015). `documentation`, `modelisation` et `qualite` remontent vers `dev`, puis `dev` vers `main` aux checkpoints.

**Tickets :** un ticket par tâche, rattaché à un ticket parent (#35 Modélisation, #36 Qualité, #37 Commun) et à un milestone, suivi dans le tableau du projet GitHub (Backlog, In progress, In review, Done).

**Traçabilité :** chaque décision est consignée dans le journal ; chaque terme dans le glossaire ; chaque source dans une fiche d'identité.

## 9. Planning

| Milestone | Échéance | Contenu |
|---|---|---|
| V0 – Socle | 20/11/2026 | Spec V1, journal, glossaire v0, matrice v0, schéma v0, couche bronze |
| V1 – Version enrichie | 02/12/2026 | Couche silver, tests de qualité, objectifs SMART de toutes les hypothèses, spec mise à jour |
| V2 – Version finale | 11/12/2026 | Couche gold, KPI, réponse à la direction, visualisations, soutenance |

Autres échéances annoncées par la professeure : rendu modélisation et pipeline à la fin de la semaine ; rendu KPI la semaine suivante (à confirmer) ; un à deux exemples complets « hypothèse → objectif SMART → KPI » avant décembre.

## 10. Points ouverts et risques

| Point | Conséquence | Suite prévue |
|---|---|---|
| Coût du dispositif et heure d'arrivée des secours : données internes du SDIS 21 | G5 sans coût en euros ; G9 peut être abandonnée | Demande à la direction (D009, D010) |
| Pas de table officielle entre l'IFM et les niveaux de la Météo des forêts | Niveaux approchés pour 2012-2023 | Classes EFFIS vérifiées sur 2024-2026 (D008) |
| Licence de la BDIFF | Données brutes non partagées dans le dépôt ; chaque membre télécharge lui-même le fichier | Règle la plus stricte appliquée (D005) |
| Export de la BDIFF par formulaire | Le chargement automatique n'est peut-être pas possible | À vérifier dans le ticket #39 ; sinon, étape manuelle documentée et consignée dans le journal |
| SIM2 et Données climatologiques en partie redondantes | Double travail | Choisir une seule source (décision à prendre) |
| Peu de feux en Côte-d'Or (120 en vingt ans) | Résultats fragiles à l'échelle du département | Comparaison avec la région et la France (D007, D008) |
