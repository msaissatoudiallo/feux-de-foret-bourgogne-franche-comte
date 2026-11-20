# Schéma de l'entrepôt v0

Ticket #41 (équipe Modélisation : Audrey, Aissatou). Dernière mise à jour : 2026-11-20.

Ce schéma part des **6 questions retenues** (R1 à R6) et des **6 sources retenues** (D020, `docs/perimetre-retenu.md`). L'entrepôt est une base DuckDB (D018), reconstruite par les scripts de `src/`. Le SQL des tables silver est dans [`src/schema_silver.sql`](../src/schema_silver.sql).

## 1. Les trois couches

| Couche | Contenu | Où | Règle |
|---|---|---|---|
| **Bronze** | Les fichiers des sources, tels qu'ils ont été téléchargés | `data/raw/` (hors de Git) | Jamais modifiés (licence de la BDIFF, D005) |
| **Silver** | Les données nettoyées, au **grain le plus fin** de chaque source, reliées par les clés | Tables DuckDB `dim_*`, `fait_*`, `passage_commune` | Testées sur les six dimensions de qualité (équipe Qualité) |
| **Gold** | Les tables prêtes pour les KPI et le dashboard | Tables DuckDB `gold_*` | Recalculées depuis le silver, avec les réglages des KPI (seuil, période, moyenne ou maximum) |

**Pourquoi le grain le plus fin en silver (D023) :** les KPI dépendent de réglages qu'on doit pouvoir faire varier pour tester la solidité des résultats : seuil d'IFM (21,3 ou 30), moyenne ou maximum des mailles, période (2006, 2015 ou 2020 à 2025). Si le silver ne gardait que des moyennes par département, on ne pourrait plus refaire ces calculs. Les résumés par département et par jour sont donc calculés en gold.

**Périmètre :** France métropolitaine, 96 départements (D021). L'outre-mer (`971` à `976` dans la BDIFF) est écarté dès le silver, car la Météo des forêts ne couvre que la métropole : la « France » de référence est la France métropolitaine.

## 2. Vue d'ensemble

```
fait_feu ───────────► dim_date, dim_commune, dim_departement
fait_ifm_jour ──────► dim_date, dim_maille
fait_mdf_jour ──────► dim_date, dim_departement
fait_meteo_jour ────► dim_date, dim_station

dim_commune ────────► dim_departement
passage_commune ────► dim_commune
dim_maille ─────────► dim_departement
dim_station ────────► dim_departement, dim_commune
```

Une flèche va de la table qui porte la clé étrangère vers la table qu'elle désigne.

## 3. Les dimensions (silver)

| Table | Une ligne = | Clé primaire | Clés étrangères | Source | Questions |
|---|---|---|---|---|---|
| `dim_date` | un jour, du 1997-01-01 au 2026-12-31 | `date` | — | Calculée (sans source externe) | Toutes |
| `dim_departement` | un département de métropole | `code_departement` | — | Admin Express | R3, R5, R6 |
| `dim_commune` | une commune de métropole (édition la plus récente) | `code_insee` | `code_departement` | Admin Express, BD Forêt V2 | R1 |
| `passage_commune` | un ancien code de commune disparu après une fusion | `code_insee_ancien` | `code_insee_actuel` → `dim_commune` | Admin Express 2017 et édition récente | R1 |
| `dim_maille` | une maille de 0,25° de l'IFM | `id_maille` | `code_departement` | Copernicus EWDS, Admin Express | R3 à R6 |
| `dim_station` | une station météo | `num_poste` | `code_departement`, `code_insee` | Données climatologiques, Admin Express | R4 |

**Détails :**
- **`dim_date`** : année, mois, jour de la semaine (1 = lundi), week-end, jour férié et son nom (11 jours calculés par règle, H7), été de juin à septembre (H4, H9). De 1997 pour les 30 étés de H9, à 2026.
- **`dim_departement`** : nom, code région, `est_bfc` (région 27). Le code est du texte de 2 caractères : `01`, `21`, `2A`.
- **`dim_commune`** : nom, population, surface calculée depuis le contour (en Lambert 93, car l'unité de la superficie cadastrale n'est pas vérifiée), surface de forêt et part de forêt. **Toutes les communes de métropole (D022)**, pour que chaque feu de la BDIFF ait sa commune ; la surface de forêt n'est remplie que pour la Côte-d'Or (la BD Forêt V2 est téléchargée par département).
- **`passage_commune`** : construite par la carte. Chaque commune de 2017 qui n'existe plus est rattachée à la commune actuelle qui contient un point de son ancien contour. En Côte-d'Or, 6 codes ont disparu, mais **aucun feu de Côte-d'Or n'en porte** (vérifié sur 2006-2025) ; la table sert pour la région et la France.
- **`dim_maille`** : latitude et longitude du centre, et département qui contient le centre (vide si le centre est en mer ou hors de France). Une maille qui déborde sur un département voisin compte pour le département de son centre : c'est une limite à écrire.
- **`dim_station`** : nom, coordonnées, altitude, département (les 2 premiers chiffres de `NUM_POSTE`) et commune qui contient la station.

## 4. Les faits (silver)

| Table | Une ligne = | Clé primaire | Clés étrangères | Source | Questions |
|---|---|---|---|---|---|
| `fait_feu` | un feu de forêt | `id_feu` | `date_alerte`, `code_insee`, `code_departement` | BDIFF | Toutes |
| `fait_ifm_jour` | une maille pour un jour | (`id_maille`, `date`) | `id_maille`, `date` | Copernicus EWDS | R3 à R6 |
| `fait_mdf_jour` | un département pour le jour visé | (`code_departement`, `date`) | `code_departement`, `date` | Météo des forêts | R3, R6 (contrôle de l'IFM) |
| `fait_meteo_jour` | une station pour un jour | (`num_poste`, `date`) | `num_poste`, `date` | Données climatologiques | R4 |

**Détails et pièges traités au chargement :**

- **`fait_feu`**
  - `id_feu` = `année-numéro` (ex. `2022-13845`). Vérifié sur les 52 811 feux de 2006-2025 : **0 doublon** pour le couple année + numéro, mais **12 916 numéros en double** d'une année à l'autre. Le numéro seul ne peut pas servir de clé.
  - `code_insee_bdiff` garde le code écrit dans la BDIFF ; `code_insee` est le code actuel, après passage par `passage_commune`.
  - `heure_alerte` : 135 feux ont l'heure `00:00`, peut-être une heure non saisie (à vérifier par l'équipe Qualité pour H7).
  - `nature` (cause) peut être vide : 100 feux sur 120 en Côte-d'Or.
  - `ancien_formulaire` vaut vrai pour les feux de 2022 et avant : les définitions des surfaces ont changé en 2023.
- **`fait_ifm_jour`** : la valeur `fwinx` de chaque maille, chaque jour. La classe de danger (faible, modéré, élevé…) n'est **pas** stockée ici : elle dépend du seuil choisi, elle est calculée en gold.
- **`fait_mdf_jour`** : `date` est le **jour visé**, c'est-à-dire la date du bulletin convertie de UTC en heure française, plus un jour ; `niveau` est `niveau_j1` de ce bulletin (D008). Le décalage est fait **une seule fois, au chargement**, et une contrainte vérifie que `date = date_bulletin + 1`. Ainsi, pour un feu du jour J, il suffit de joindre sur `date = J`, sans risque d'erreur plus tard. Le chargement gère aussi les formats différents selon l'année (séparateur, zéro devant le département, colonne `dep_nom`), ticket #40.
- **`fait_meteo_jour`** : pluie (`RR`), températures maximale et minimale (`TX`, `TN`), vent moyen (`FFM`), humidité minimale (`UN`), avec leur code qualité. Vérifié dans le fichier : les valeurs sont **déjà en °C, mm, m/s et %**, avec une décimale ; il ne faut pas les diviser par 10. La pluie du jour J est mesurée de J 6 h à J+1 6 h (UTC) : à prendre en compte pour compter les jours sans pluie avant un feu (H5).

## 5. Les tables gold (pour les KPI)

| Table | Une ligne = | Clé primaire | Construite depuis | Questions et hypothèses |
|---|---|---|---|---|
| `gold_departement_jour` | un département pour un jour (2012-2025) | (`code_departement`, `date`) | `fait_feu`, `fait_ifm_jour`, `dim_maille`, `fait_mdf_jour` | R3, R4, R5 (H2, H3, H5) |
| `gold_commune` | une commune de Côte-d'Or | `code_insee` | `dim_commune`, `fait_feu` | R1 (H1, H8) |
| `gold_ete_departement` | un département pour un été (1997-2026) | (`code_departement`, `annee`) | `fait_ifm_jour`, `dim_maille`, `fait_mdf_jour` | R6 (H9) |

- **`gold_departement_jour`** : nombre de feux, IFM moyen et maximal des mailles du département, classe de danger selon le seuil choisi, niveau de la Météo des forêts (depuis 2024). C'est la base des taux de jours avec feu par classe (H2), des fausses alertes (H3) et des jours de dispositif par seuil (R5).
- **`gold_commune`** : nombre de feux de 2015-2025, surface de forêt, population, feux par km² de forêt (H1), commune à fort enjeu (H8).
- **`gold_ete_departement`** : nombre de jours de danger élevé par été (H9), et jours au niveau 3 ou plus de la Météo des forêts pour le contrôle sur 2024-2026.

Les R2 (mois, jours, heures) se calculent directement depuis `fait_feu` et `dim_date`, sans table gold dédiée.

**Hors schéma :** les Interventions SDIS servent seulement au contrôle de la complétude de la BDIFF (#42). Elles restent en bronze.

## 6. Les clés de jointure

| Clé | Format | Tables |
|---|---|---|
| `date` | `DATE` (AAAA-MM-JJ), en heure française | Tous les faits, `dim_date` |
| `code_departement` | Texte, 2 caractères (`01`, `21`, `2A`) | `dim_departement`, `dim_commune`, `dim_maille`, `dim_station`, `fait_feu`, `fait_mdf_jour` |
| `code_insee` | Texte, 5 caractères (`21231`) | `dim_commune`, `passage_commune`, `dim_station`, `fait_feu` |
| `id_maille` | Texte `latitude_longitude` du centre | `dim_maille`, `fait_ifm_jour` |
| `num_poste` | Texte, 8 caractères (`21056001`) | `dim_station`, `fait_meteo_jour` |

Les sources sans code (mailles de l'IFM, stations, zones de forêt) sont rattachées aux communes et aux départements **par la carte** (geopandas), une seule fois, dans les dimensions. Les faits n'ont ensuite que des jointures par clé.

## 7. Limites du schéma

- **L'IFM n'est pas le niveau officiel** de la Météo des forêts (proxy, D008).
- **Une maille compte pour le département de son centre**, même si elle déborde sur un voisin.
- **La forêt est dans son état de 2017**, et seulement pour la Côte-d'Or.
- **La station météo la plus proche d'un feu ne mesure pas toujours le vent et l'humidité** (9 et 14 stations en Côte-d'Or).
- **Volume de l'IFM pour la France entière :** environ 1 000 mailles sur la France métropolitaine (550 000 km² pour des mailles d'environ 530 km²) × 5 100 jours (2012-2025), soit environ 5 millions de lignes. C'est supportable par DuckDB, mais le téléchargement depuis Copernicus (compte, file d'attente) est à prévoir.
