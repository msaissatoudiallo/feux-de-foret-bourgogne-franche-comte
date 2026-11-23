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
| xarray, netCDF4 | Lire les fichiers NetCDF de l'IFM (Copernicus EWDS) |
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
