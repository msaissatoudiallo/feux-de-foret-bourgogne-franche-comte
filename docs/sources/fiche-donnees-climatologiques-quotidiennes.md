# Fiche source – Données climatologiques de base quotidiennes (Météo-France)

- **Explorée par :** Audrey, le 2026-11-18
- **Page de la source :** https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes
- **Fichiers ouverts (Côte-d'Or) :**
  - `Q_21_previous-1950-2024_RR-T-Vent.csv.gz` et `Q_21_latest-2025-2026_RR-T-Vent.csv.gz` : pluie, températures, vent
  - `Q_21_previous-1950-2024_autres-parametres.csv.gz` et `Q_21_latest-2025-2026_autres-parametres.csv.gz` : humidité, ensoleillement, phénomènes…
  - les descriptifs des champs `Q_descriptif_champs_RR-T-Vent.csv` et `Q_descriptif_champs_autres-parametres.csv`

## Description

Mesures quotidiennes de toutes les stations météo de Météo-France, en métropole et en outre-mer, depuis leur ouverture et pour tous les paramètres disponibles. Les données ont subi un contrôle climatologique (description de la fiche data.gouv.fr). Contrairement à la Météo des forêts, ce ne sont pas des prévisions ni un niveau de danger : ce sont des **mesures réelles**, jour par jour, toute l'année.

## Fiche d'identité

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Les fichiers sont hébergés sur le stockage de Météo-France (`meteofrance.s3.sbg.io.cloud.ovh.net`) et référencés sur data.gouv.fr. |
| Mode d'accès et format | Téléchargement de fichiers publiés : CSV compressés (`.csv.gz`), séparateur point-virgule, UTF-8. Les fichiers sont découpés **par département**, **par période** (avant 1949, 1950 à N-2, N-1 à N) et **par groupe de paramètres** (« RR-T-Vent » et « autres paramètres »). La fiche data.gouv.fr compte 628 fichiers. |
| Grain (une ligne = ?) | **Une station météo × un jour.** Chaque ligne porte le numéro de la station (`NUM_POSTE`), son nom, sa latitude, sa longitude, son altitude, la date (`AAAAMMJJ`) puis les mesures. Chaque mesure a son code qualité (ex. `TX` et `QTX`). |
| Emprise géographique | France métropolitaine et outre-mer. Pour la Côte-d'Or : **111 stations** dans le fichier 1950-2024 et **25 stations** actives en 2025-2026. Chaque station est localisée par ses coordonnées, pas par une commune. |
| Période réellement couverte par les données | Côte-d'Or : du **1er janvier 1950 au 16 novembre 2026** pour les fichiers ouverts. Un fichier « avant 1949 » existe aussi, mais je ne l'ai pas ouvert. Toute l'année est couverte, pas seulement l'été. Le nombre de stations varie : 15 à 19 stations mesurent la température chaque année de 2006 à 2017, puis 20 à 27 à partir de 2018. |
| Date de dernière mise à jour affichée sur la fiche | 17 novembre 2026 (data.gouv.fr). |
| Fréquence de mise à jour | Selon la fiche data.gouv.fr : **quotidienne** pour les deux dernières années, **mensuelle** pour les fichiers de 1950 à N-2, **annuelle** pour les historiques d'avant 1950. |
| Volumétrie | Côte-d'Or : 1 530 067 lignes pour « RR-T-Vent » 1950-2024 (12 Mo compressé) et 16 805 lignes pour 2025-2026. 741 575 lignes pour « autres paramètres » 1950-2024 (5,7 Mo compressé) et 16 805 lignes pour 2025-2026. 62 colonnes pour « RR-T-Vent », 96 pour « autres paramètres ». Aucun doublon station + date. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | La **date** (`AAAAMMJJ`) et le **département** (les 2 premiers chiffres du numéro de station, et le découpage des fichiers). **Pas de code commune** : pour rattacher un feu de la BDIFF (localisé à la commune) à la station la plus proche, il faudra passer par les coordonnées. Le numéro `NUM_POSTE` sert de clé pour la station. |
| Données personnelles | Aucune : ce sont des mesures physiques. Le nom de station est un nom de lieu (ex. « ALOXE CORTON »). |
| Licence | Licence Ouverte / Open Licence 2.0 (Etalab), indiquée sur data.gouv.fr : réutilisation libre avec mention de la source. |
| Questions de mon analyse auxquelles elle pourrait répondre | **Question 1** et **question 2** : on peut connaître la météo réelle de chaque jour de feu de la [BDIFF](fiche-bdiff.md), y compris au printemps et avant 2024, ce que la Météo des forêts ne permet pas. On peut aussi comparer avec les jours sans feu. **Question 4** : les mêmes fichiers existent pour tous les départements. |

## Ce que j'ai découvert en ouvrant les fichiers

- **Toutes les dates de feu de la BDIFF sont couvertes.** Pour chacun des 120 feux de Côte-d'Or (2012-2025), au moins 15 stations mesurent la température maximale ce jour-là, au moins 25 la pluie, au moins 5 le vent et au moins 6 l'humidité.
- **Tous les paramètres ne sont pas mesurés partout.** Depuis 2006 en Côte-d'Or :

  | Paramètre | Stations qui le mesurent |
  |---|---|
  | Pluie (`RR`) | 68 |
  | Températures min. et max. (`TN`, `TX`) | 31 |
  | Humidité minimale (`UN`) | 14 |
  | Vent moyen (`FFM`) | 9 |
  | Évapotranspiration (`ETPMON`) | 3 |

  Le vent et l'humidité, importants pour le danger de feu, ne sont mesurés que par quelques stations : la station la plus proche d'un feu ne les aura souvent pas.
- **Les données récentes sont un peu moins contrôlées.** Les codes qualité indiquent l'état de chaque valeur : 0 (validée définitivement par le climatologue), 1 (validée), 9 (seulement filtrée) ou 2 (douteuse, en cours de vérification). Pour la pluie 1950-2024, 1 517 947 valeurs sont validées (code 1), 11 263 seulement filtrées (code 9) et 839 n'ont pas de code.
- **Pièges de lecture pour le pipeline :**
  - la pluie (`RR`) du jour J est mesurée de 6 h le jour J à 6 h le lendemain ;
  - les heures sont en UTC pour la métropole ;
  - les valeurs sont en dixièmes (ex. `TX` en °C et 1/10).
  
  Ce sont des règles du descriptif des champs, à respecter au chargement.
- **Volume à surveiller :** 1,5 million de lignes pour un seul département. Pour la région ou la France, il faudra filtrer (période 2006-2025, quelques paramètres) dès le chargement.
- **Pas d'indice de danger tout prêt.** La source donne les ingrédients (température, pluie, vent, humidité), mais pas le niveau de danger. Si on veut un indice, il faudra le calculer nous-mêmes ou choisir quelques indicateurs simples : jours sans pluie, température maximale, humidité minimale.
