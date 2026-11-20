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
| requests | Télécharger les fichiers publiés (data.gouv.fr, Météo-France) |
| pytest | Les tests de qualité |
| ipykernel | Les notebooks d'exploration dans VS Code |

Quand une bibliothèque est ajoutée, l'écrire dans `requirements.txt` avec sa version, puis relancer l'installation. Pour connaître la version installée : `pip show nom` (ligne `Version`), qui marche sur macOS, Linux et Windows.

### Les dossiers `src/` et `data/`

- `src/` : le code du pipeline, un script par étape (chargement de la couche bronze, nettoyage et jointures en silver, tables des KPI en gold).
- `data/raw/` : la couche **bronze**, avec les fichiers des sources tels qu'ils ont été téléchargés, jamais modifiés. Ce dossier est **hors de Git**. Chaque membre télécharge lui-même les fichiers bruts (D005 pour la BDIFF).
- L'entrepôt DuckDB (`*.duckdb`) est aussi hors de Git : les scripts le reconstruisent depuis `data/raw/`.

## Charger les données (couche bronze)

Les scripts de chargement déposent les fichiers des sources **tels quels** dans `data/raw/`, hors de Git. Chaque membre les lance sur son ordinateur, environnement activé, depuis la racine du dépôt.

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

## Règles de travail

- Une branche par ticket, nommée `type/courte-description` (ex. `docs/analyse-commande-jane`, `feat/chargement-bdiff`).
- Des commits atomiques : un commit = un changement cohérent, avec un message clair.
- Personne ne travaille directement sur `main`, `dev`, `documentation`, `modelisation` ou `qualite`. Chaque branche de tâche part de la branche de son domaine (voir D016) :
  - `documentation` pour les documents (journal, README, glossaire, fiches de sources, fiches indicateur, inventaire, matrice, et la spec sauf ses parties 6 et 7) ;
  - `modelisation` pour le schéma de l'entrepôt, le chargement de la BDIFF et la partie 6 de la spec (équipe Modélisation) ;
  - `qualite` pour les profils qualité, le chargement de la Météo des forêts et la partie 7 de la spec (équipe Qualité).
- Le travail remonte par pull requests : branche de tâche → branche de domaine → `dev` (en fin de semaine) → `main` (aux checkpoints).
- Chaque pull request est relue et validée par le ou la **responsable du domaine concerné** : Jane pour les sources, Audrey pour le pipeline et le modèle, Melvyn pour la qualité, Aissatou pour la gestion du projet (journal, README, spec). Jane valide en plus chaque nouvelle source, et Melvyn vérifie que les tests ont tourné. Personne ne valide sa propre pull request (voir D015 et D017 dans le [journal des décisions](docs/journal-decisions.md)).
- Chaque tâche a un ticket, rattaché à un ticket parent et à un milestone (V0, V1, V2), et suivi dans le tableau du projet GitHub (Backlog, In progress, In review, Done).
- Après la fusion d'une pull request vers `documentation`, `modelisation` ou `qualite`, le ticket est fermé à la main (GitHub ne le fait que pour la branche par défaut, `dev`).
