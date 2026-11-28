# Feux de forêt – Bourgogne-Franche-Comté

Projet de modélisation et pipeline de données (UE01 – Stratégie business data-driven, Hetic 2026/2027).

**Commanditaire :** Direction du SDIS 21 (Côte-d'Or) – Saison feux 2027
**Région :** Bourgogne-Franche-Comté
**Rendu final :** 11 décembre 2026

## La commande

La direction du SDIS 21 veut arbitrer deux points pour l'été 2027 :

1. **Où concentrer les moyens** (humains et financiers) pour lutter au mieux contre les départs de feu ?
2. **À partir de quel niveau de la Météo des forêts** déclencher le dispositif renforcé (patrouilles, guet, etc.) ?

Elle souhaite comprendre le comportement de l'indice en Côte-d'Or, dans les autres départements de la région, et situer le département par rapport au reste du territoire national.

## L'équipe

| Rôle | Membre | Responsable de |
|---|---|---|
| Cheffe de projet | Aissatou Diallo | Dépôt, milestones, attribution et suivi des tickets, checkpoints, journal des décisions, validation du glossaire |
| Responsable sources | Jane | Inventaire, fiches d'identité, matrice questions × sources, validation des nouvelles sources |
| Responsable qualité et conformité | Melvyn | Règles de qualité, tests, données personnelles |
| Responsable pipeline et modèle | Audrey | Chargement, consolidation, entrepôt |

Un rôle confie la responsabilité d'un domaine : la personne relit ce qui le touche et valide les tickets et les pull requests qui en relèvent. Tout changement de rôle est consigné dans le [journal des décisions](docs/journal-decisions.md).

Le groupe travaille en deux équipes (D004) : **Modélisation** (Audrey, Aissatou) et **Qualité** (Melvyn, Jane), chacune avec sa branche (D016).

## Organisation du dépôt

```
src/                         # Code du pipeline (chargement, nettoyage, tables des KPI)
data/
└── raw/                     # Couche bronze : fichiers bruts des sources (hors de Git)
requirements.txt             # Bibliothèques Python du projet
docs/
├── analyse/                 # Analyses individuelles de la commande (commande-prenom-nom.md)
├── indicateurs/             # Fiches indicateur, une par KPI (fiche-kpi-*.md)
├── sources/                 # Fiches d'identité des sources (fiche-*.md), inventaire.md, matrice.md
├── cadrage_technique.md     # Rendu du cadrage technique : sources prévues, outils, risques (20/11)
├── glossaire.md             # Glossaire du projet
├── journal-decisions.md     # Journal des décisions du groupe
└── spec.md                  # Spécification du projet (point d'entrée pour comprendre le projet)
```

Pour comprendre le projet, commencer par la [spécification](docs/spec.md).

## Environnement Python

Le projet utilise **Python 3.13** et un environnement virtuel `.venv/`, exclu de Git. Chaque membre le crée une fois sur son ordinateur, à la racine du dépôt.

### Activation de l'environnement

**1. Créer l'environnement** (une seule fois) :

```
python3.13 -m venv .venv
```

Sous Windows : `py -3.13 -m venv .venv`. Pour connaître sa version : `python3 --version` (Windows : `py --version`).

**2. L'activer** (à refaire dans chaque nouveau terminal) :

- macOS / Linux : `source .venv/bin/activate`
- Windows (PowerShell) : `.venv\Scripts\Activate.ps1`

  Si PowerShell bloque le script la première fois (« l'exécution de scripts est désactivée sur ce système »), autoriser les scripts pour son compte, une seule fois, puis relancer l'activation :

  ```
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

Le nom `(.venv)` apparaît alors au début de la ligne du terminal. Pour quitter l'environnement : `deactivate`.

Dans VS Code, choisir l'interpréteur `.venv` : `Cmd + Maj + P` (ou `Ctrl + Maj + P`) → « Python: Select Interpreter ».

### Activation de la stack

**1. Installer les bibliothèques** (environnement activé) :

```
pip install -r requirements.txt
```

**2. Vérifier l'installation** :

```
python -c "import pandas, duckdb, geopandas, xarray; print('ok')"
```

**Ce que contient la stack (`requirements.txt`) :**

| Bibliothèque | À quoi elle sert |
|---|---|
| pandas, pyarrow | Lire et préparer les tableaux (CSV de la BDIFF, de la Météo des forêts, des données climatologiques) |
| DuckDB | L'entrepôt : une base SQL dans un seul fichier, sans serveur, pour les couches silver et gold |
| geopandas | Les cartes (Admin Express, BD Forêt V2) et les jointures par la position (stations, mailles → communes) |
| py7zr | Ouvrir et contrôler les archives .7z de la BD Forêt V2 (IGN) |
| xarray, netCDF4 | Lire les fichiers NetCDF de l'IFM (Copernicus EWDS) |
| cdsapi | Demander l'IFM à Copernicus EWDS par programme (avec la clé du fichier `.env`) |
| requests | Télécharger les fichiers publiés (data.gouv.fr, Météo-France, BDIFF) |
| truststore | Vérifier les certificats des sites avec ceux du système (le portail de la BDIFF a une chaîne de certificats incomplète) |
| pytest | Les tests de qualité |
| ipykernel | Les notebooks d'exploration dans VS Code |

Quand une bibliothèque est ajoutée, l'écrire dans `requirements.txt` avec sa version, puis relancer l'installation. Pour connaître la version installée : `pip show nom` (ligne `Version`), qui marche sur macOS, Linux et Windows.

### Les dossiers `src/` et `data/`

- `src/` : le code du pipeline, un script par étape (chargement de la couche bronze, nettoyage et jointures en silver, tables des KPI en gold).
- `data/raw/` : la couche **bronze**, avec les fichiers des sources tels qu'ils ont été téléchargés, jamais modifiés. Ce dossier est **hors de Git**. Chaque membre télécharge lui-même les fichiers bruts (D005 pour la BDIFF).
- L'entrepôt DuckDB (`*.duckdb`) est aussi hors de Git : les scripts le reconstruisent depuis `data/raw/`.

## Charger les données (couche bronze)

Les scripts de chargement déposent les fichiers des sources **tels quels** dans `data/raw/`, hors de Git. Chaque membre les lance sur son ordinateur, environnement activé, depuis la racine du dépôt.

### BDIFF

```
python src/charger_bdiff.py
```

- **Ce que fait le script :** il refait la recherche du portail [bdiff.agriculture.gouv.fr](https://bdiff.agriculture.gouv.fr/incendies) pour la **France entière, une année à la fois, de 2006 à 2025**, et enregistre chaque export dans `data/raw/bdiff/bdiff_AAAA.zip`.
- **Les fichiers ne sont jamais modifiés** : chaque zip garde `Incendies.csv`, les définitions et les mentions légales du producteur (licence, D005).
- **Une année par fichier**, car le portail refuse l'export de la France entière sur toute la période en une seule fois.
- **Relancer le script ne crée pas de doublons** : une année déjà présente est ignorée. Pour retélécharger : `python src/charger_bdiff.py --force`.
- **Choisir les années :** `python src/charger_bdiff.py --debut 2024 --fin 2025`.
- **Résultat attendu :** 20 fichiers (environ 12 Mo), soit **52 811 incendies**, dont 120 en Côte-d'Or.

### Données climatologiques quotidiennes

```
python src/charger_climatologie.py
```

- **Ce que fait le script :** il lit le catalogue de [data.gouv.fr](https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes) et enregistre dans `data/raw/climatologie/` les mesures des stations de la **Côte-d'Or** (fichiers `Q_21_…`) :
  - période ancienne (`previous-1950-2024`) et récente (`latest-2025-2026`) ;
  - pour chaque période, les deux groupes de paramètres : `RR-T-Vent` (pluie, températures, vent) et `autres-parametres` (dont l'humidité) ;
  - les descriptifs des champs (`Q_descriptif_champs_….csv`) et le descriptif général (PDF).
- **Les fichiers ne sont jamais décompressés ni modifiés** (`.csv.gz` de Météo-France, Licence Ouverte 2.0). Le fichier « avant 1949 » n'est pas pris.
- **Le fichier reçu est contrôlé** : taille annoncée par le serveur, gzip lisible jusqu'au bout, colonnes attendues (`NUM_POSTE`, `AAAAMMJJ`…) et stations du bon département. Sinon, rien n'est écrit.
- **Relancer le script ne crée pas de doublons** : un fichier déjà présent est ignoré. La période récente est mise à jour **chaque jour** par Météo-France : pour la rafraîchir, `python src/charger_climatologie.py --force`.
- **Changement d'année :** les noms des périodes changent (par exemple `previous-1950-2025` en 2027). Le script prend seul les nouveaux noms et signale les anciens fichiers, à supprimer à la main pour éviter des dates en double.
- **Un autre département :** `python src/charger_climatologie.py --departement 89`.
- **Résultat attendu :** 7 fichiers (environ 18 Mo), soit **1 530 067 lignes** de 1950 à 2024 et environ 17 000 lignes depuis 2025 pour `RR-T-Vent`, sur 111 stations.

### BD Forêt V2

```
python src/charger_bd_foret.py
```

- **Ce que fait le script :** il cherche dans le catalogue de l'IGN ([data.geopf.fr](https://data.geopf.fr/telechargement/resource/BDFORET)) l'édition **V2 de la Côte-d'Or** et enregistre l'archive dans `data/raw/bd_foret/`, sous le nom donné par l'IGN : `BDFORET_2-0__SHP_LAMB93_D021_2017-10-04.7z` (édition de 2017).
- **L'archive n'est jamais décompressée ni modifiée** : elle garde la carte `FORMATION_VEGETALE` (shapefile, Lambert 93), les métadonnées et le LISEZ-MOI de l'IGN. Elle est ouverte en silver avec `py7zr`.
- **Le fichier reçu est contrôlé** : taille annoncée par l'IGN, archive intacte (contrôle de chaque fichier) et carte complète (`.shp`, `.shx`, `.dbf`, `.prj`). Sinon, rien n'est écrit.
- **Relancer le script ne crée pas de doublons** : une archive déjà présente est ignorée. Pour retélécharger : `python src/charger_bd_foret.py --force`.
- **Un autre département :** `python src/charger_bd_foret.py --departement 89`. Le schéma n'utilise que la Côte-d'Or (D023).
- **Résultat attendu :** 1 fichier de 32 Mo, soit **25 831 zones de forêt**.

### Météo des forêts

```
python src/charger_meteo_des_forets.py
```

- **Ce que fait le script :** il télécharge les archives de la Météo des forêts (Météo-France, jeu « Archives de la Météo des forêts » sur [data.gouv.fr](https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets)), **une année par fichier, de 2024 à 2026**, dans `data/raw/meteo_des_forets/mdf_AAAA.csv.gz`.
- **Les fichiers ne sont jamais modifiés** : ils sont enregistrés compressés, comme ils sont publiés. Les différences entre les années (séparateur, `num_dep` sans zéro en 2024 et 2025, heure en UTC) sont traitées dans la couche silver (`docs/sources/fiche-meteo-des-forets.md`).
- **Relancer le script ne crée pas de doublons** : une année déjà présente est ignorée. Pour retélécharger : `python src/charger_meteo_des_forets.py --force`.
- **Pendant la saison des feux**, Météo-France complète chaque jour le fichier de l'année en cours : relancer avec `--force` pour avoir la dernière version (le fichier est remplacé, pas complété).
- **Choisir les années :** `python src/charger_meteo_des_forets.py --debut 2026 --fin 2026`.
- **Résultat attendu :** 3 fichiers (environ 130 Ko), soit **35 616 lignes** : 11 520 en 2024 et en 2025 (séparateur `,`), 12 576 en 2026 (séparateur `;`).

### Copernicus EWDS (IFM)

**1. Créer la clé (une seule fois par personne) :**
- créer un compte gratuit sur [ewds.climate.copernicus.eu](https://ewds.climate.copernicus.eu), puis **accepter la licence** du jeu *Fire danger indices historical data* (onglet « Download », en bas de la page) : sans cela, les demandes sont refusées ;
- copier la clé personnelle (page « Your profile », rubrique « API Token ») ;
- à la racine du dépôt, copier le modèle puis y coller la clé :

  ```
  cp .env.exemple .env          # macOS
  copy .env.exemple .env        # Windows
  ```

  ```
  COPERNICUS_EWDS_CLE=votre-clé
  ```

  Le fichier `.env` est **hors de Git** (`.gitignore`) : la clé n'est jamais publiée. Seul le modèle `.env.exemple`, sans clé, est dans le dépôt.

**2. Lancer le script :**

```
python src/charger_copernicus.py
```

- **Ce que fait le script :** il demande à Copernicus l'IFM (variable *Fire weather index*, réanalyse **consolidée**, jeu `cems-fire-historical-v1`, grille 0,25°, NetCDF) et enregistre **un fichier par zone et par année** dans `data/raw/copernicus/` :
  - `ifm_region_AAAA.nc` : Bourgogne-Franche-Comté, **de 1996 à 2026**, toute l'année (indicateur 2 : étés ; indicateurs 3, 4 et 6 : feux de printemps). 1996 est pris en plus pour pouvoir compter 30 étés complets sur 1996-2025 (D025) ;
  - `ifm_france_AAAA.nc` : France métropolitaine et Corse, **de 2015 à 2025**, toute l'année (indicateur 3 : comparaison Côte-d'Or, région, France).
- **Les fichiers ne sont jamais modifiés.** Les deux zones se recouvrent sur 2015-2025 : en silver, on prend l'une **ou** l'autre, sans les empiler (sinon des mailles seraient en double).
- **Le fichier reçu est contrôlé** : NetCDF lisible, variable `fwinx` présente, un pas de temps pour chaque jour demandé, aucune valeur négative. Sinon, rien n'est écrit.
- **Relancer le script ne crée pas de doublons** : une année déjà présente est ignorée. Pour la redemander : `--force`.
- **File d'attente :** chaque année est une demande à Copernicus, qui peut attendre plusieurs minutes. Le premier chargement complet (42 demandes) prend donc du temps : on peut le faire en plusieurs fois, par exemple `python src/charger_copernicus.py --zone region --debut 1996 --fin 2010`.
- **2026 est incomplète :** la réanalyse consolidée est publiée avec quelques mois de retard (fin août 2026 au catalogue le 28/11/2026), et Copernicus a suspendu ses mises à jour depuis le 16/11/2026. Le script lit les jours disponibles dans le catalogue et ne demande que les mois complets. Pour compléter plus tard : `python src/charger_copernicus.py --zone region --debut 2026 --force`.
- **Message `WARNING … updates to this dataset will cease` :** c'est l'avertissement de Copernicus sur la suspension des mises à jour, pas une erreur du script.
- **Résultat attendu :** pour la région, un fichier d'environ 220 Ko par année, avec **209 mailles** (11 latitudes × 19 longitudes) et 365 jours (366 les années bissextiles). Contrôle fait sur 2025 : le 30/07/2025, l'IFM des mailles de Côte-d'Or va de 1,5 à 7,2, comme dans la fiche source.

### Admin Express

```
python src/charger_admin_express.py
```

- **Ce que fait le script :** il demande au service en ligne de l'IGN ([data.geopf.fr/wfs](https://data.geopf.fr/wfs)) les contours d'Admin Express COG, pour les **96 départements de France métropolitaine** (D022, D023), et les enregistre en GeoJSON dans `data/raw/admin_express/` :
  - `communes_AAAA_DD.geojson` : les communes de l'**édition la plus récente** (AAAA, 2026 au 28/11/2026), un fichier par département (DD : `01`, `21`, `2A`…) ;
  - `communes_2017_DD.geojson` : les communes de l'**édition 2017**, pour la table de passage des communes fusionnées (D023) ;
  - `departements_AAAA.geojson` : les contours des 96 départements, pour rattacher les mailles de Copernicus et les stations météo aux départements.
- **L'édition la plus récente est trouvée seule** dans le catalogue du service, et son année est écrite dans le nom des fichiers : quand l'IGN publiera une nouvelle édition, les fichiers ne seront pas mélangés.
- **Version précise (COG), pas la version simplifiée (CARTO)** : la surface des communes et leur part de forêt (H1, H8) sont calculées sur ces contours.
- **Les fichiers ne sont jamais modifiés.** Les noms des colonnes changent selon l'édition (`insee_com` et `insee_dep` en 2017, `code_insee` et `code_insee_du_departement` dans l'édition récente) : c'est traité en silver (`docs/sources/fiche-admin-express.md`).
- **Le fichier reçu est contrôlé** : GeoJSON lisible, nombre de communes égal au nombre annoncé par l'IGN, toutes du bon département, codes INSEE de 5 caractères sans doublon. Sinon, rien n'est écrit.
- **Relancer le script ne crée pas de doublons** : un fichier déjà présent est ignoré. Pour retélécharger : `python src/charger_admin_express.py --force`.
- **Essai sur un seul département :** `python src/charger_admin_express.py --departement 21` (environ 40 secondes).
- **Résultat attendu :** 193 fichiers (environ 980 Mo, dont 110 Mo pour les départements), soit **34 746 communes** dans l'édition 2026 et **35 287** dans l'édition 2017. Le service de l'IGN en annonce 2 de plus en 2026 : ce sont les communes de Saint-Pierre-et-Miquelon (code de département `NR`), qui sont en outre-mer et donc écartées (D022). Pour la Côte-d'Or : **698 communes** en 2026 et **704** en 2017 ; les 6 codes disparus (21073, 21213, 21486, 21507, 21513, 21621) sont ceux de la fiche source.

## Règles de travail

- Une branche par ticket, nommée `type/courte-description` (ex. `docs/analyse-commande-jane`, `feat/chargement-bdiff`).
- Des commits atomiques : un commit = un changement cohérent, avec un message clair.
- Personne ne travaille directement sur `main`, `dev`, `documentation`, `modelisation` ou `qualite`. Chaque branche de tâche part de la branche de son domaine (voir D016) :
  - `documentation` pour les documents (journal, README, glossaire, fiches de sources, fiches indicateur, inventaire, matrice, et la spec sauf ses parties 6 et 7) ;
  - `modelisation` pour le schéma de l'entrepôt, le chargement de la BDIFF et la partie 6 de la spec (équipe Modélisation) ;
  - `qualite` pour les profils qualité, le chargement de la Météo des forêts et la partie 7 de la spec (équipe Qualité).
- Le travail remonte par pull requests : branche de tâche → branche de domaine → `dev` (en fin de semaine) → `main` (aux checkpoints).
- Pour récupérer le travail arrivé dans `dev`, une branche d'équipe est mise à jour par une pull request `dev` → branche d'équipe (base : `modelisation` ou `qualite`, compare : `dev`). Chaque membre part ensuite de sa branche d'équipe à jour ; une branche de tâche en cours récupère la mise à jour avec `git pull origin <branche d'équipe>`.
- Les parties techniques du README (environnement, chargement des données) et `requirements.txt` sont modifiées avec le code, sur la branche d'équipe. Pour éviter les conflits entre équipes : une bibliothèque par ligne, ajoutée dans sa rubrique de `requirements.txt`, et chaque équipe écrit dans sa propre partie du README.
- Chaque pull request est relue et validée par le ou la **responsable du domaine concerné** : Jane pour les sources, Audrey pour le pipeline et le modèle, Melvyn pour la qualité, Aissatou pour la gestion du projet (journal, README, spec). Jane valide en plus chaque nouvelle source, et Melvyn vérifie que les tests ont tourné. Personne ne valide sa propre pull request (voir D015 et D017 dans le [journal des décisions](docs/journal-decisions.md)).
- Chaque tâche a un ticket, rattaché à un ticket parent et à un milestone (V0, V1, V2), et suivi dans le tableau du projet GitHub (Backlog, In progress, In review, Done).
- Après la fusion d'une pull request vers `documentation`, `modelisation` ou `qualite`, le ticket est fermé à la main (GitHub ne le fait que pour la branche par défaut, `dev`).
