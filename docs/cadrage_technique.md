# Rendu cadrage technique · Groupe 2

Rendu du vendredi 20 novembre 2026. Projet « Prévenir et détecter les feux de forêt », Bourgogne-Franche-Comté.

| Rubrique | Votre réponse |
|---|---|
| Groupe (numéro, membres) | Groupe 2 : Aissatou Diallo (cheffe de projet), Audrey (pipeline et modèle), Jane (sources), Melvyn (qualité et conformité) |
| Décideur et décision | La direction du SDIS 21 (Côte-d'Or) décide, avant la saison des feux 2027, où concentrer ses moyens humains et financiers contre les départs de feu, et à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé (patrouilles, guet). |
| Lien GitHub | https://github.com/msaissatoudiallo/feux-de-foret-bourgogne-franche-comte |
| Accès au dépôt | Public |

## Sources prévues

| Source (nom exact) | Producteur | Lien | Période | Champs utilisés |
|---|---|---|---|---|
| BDIFF – Base de données sur les incendies de forêt en France (export « Incendies », feux de forêt) | Ministère de l'Agriculture | https://bdiff.agriculture.gouv.fr/ | 2006-2025, France entière (analyse centrée sur la Côte-d'Or et la région) | Département, code INSEE de la commune, date et heure de première alerte, surfaces parcourues, nature (cause) |
| Fire danger indices historical data from the Copernicus Emergency Management Service (`cems-fire-historical-v1`) | Copernicus Emergency Management Service | https://ewds.climate.copernicus.eu | 1997-2026 pour les étés, 2012-2025 pour le croisement avec les feux ; zone de la région | `fwinx` (Indice Forêt Météo), `valid_time`, `latitude`, `longitude` |
| Archives de la Météo des forêts | Météo-France | https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets | Juin 2024 à octobre 2026, saison des feux seulement | `date`, `num_dep`, `niveau_j1` |
| Admin Express, couche des communes (édition la plus récente, et 2017 pour les communes fusionnées) | IGN | https://www.data.gouv.fr/datasets/5808de39c751df1e0679df72 | Édition la plus récente, et 2017 | `code_insee`, `code_insee_du_departement`, `population`, contour de la commune |
| BD Forêt V2 | IGN | https://geoservices.ign.fr/bdforet | État de la forêt en 2017 (Côte-d'Or) | `TFV_G11` (type de formation végétale), contour des zones de forêt |
| Données climatologiques de base quotidiennes | Météo-France | https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes | 2006-2025 (stations de Côte-d'Or) | `NUM_POSTE`, `AAAAMMJJ`, `RR` (pluie), `TX` et `TN` (températures), `FFM` (vent), `UN` (humidité) |

Les Interventions des SDIS (Ministère de l'Intérieur) servent seulement à contrôler la complétude de la BDIFF. Chaque source a une fiche d'identité dans `docs/sources/`. Les sources écartées et la raison sont dans le journal des décisions (D013) et dans la réduction des questions (ticket #104).

## Outils choisis

| Usage | Outil | Pourquoi ce choix |
|---|---|---|
| Base de données | DuckDB | Un seul fichier, sans serveur ni mot de passe sur les quatre ordinateurs ; lit directement les CSV et les `.csv.gz` des sources ; requêtes SQL pour les couches silver et gold. L'entrepôt est reconstruit par les scripts et reste hors du dépôt public (licence de la BDIFF). Décision D018. |
| Dataviz | Streamlit, avec Plotly pour les graphiques | Dashboard interactif écrit en Python, qui lit directement l'entrepôt DuckDB ; tout est du code dans le dépôt (dossier `dataviz/`), utilisable sous Windows et Mac ; des captures sont ajoutées pour voir la dataviz sans lancer le code. Power BI est utilisé pour les exercices du cours. Décision D019. |
| Langage / pipeline | Python 3.13 : pandas, pyarrow, geopandas (cartes), xarray et netCDF4 (Copernicus) | Un pipeline en code, reproductible : scripts dans `src/` qui chargent les sources (couche bronze), les nettoient et les relient (silver), puis calculent les indicateurs (gold). Versions fixées dans `requirements.txt`. |
| Autre | GitHub (tickets, branches, pull requests, journal des décisions) et pytest | Suivi du travail et de chaque décision ; tests automatiques de qualité des données. |

## Risques identifiés

- **Données manquantes ou non ouvertes :** le niveau officiel de la Météo des forêts n'existe que depuis juin 2024, et seulement l'été : nous utilisons l'Indice Forêt Météo de Copernicus comme proxy, traduit en classes de danger (D008). Le coût d'une journée de dispositif et l'heure d'arrivée des secours sont des données internes du SDIS : nous raisonnons en nombre de jours de dispositif (D009) et avons écarté la question du délai des secours (D010). Seulement 120 feux en Côte-d'Or en 20 ans : l'étude est élargie à la région et à la France. Cause inconnue pour 100 feux sur 120.
- **Volume ou accès :** la BDIFF s'exporte par le formulaire du portail, qui refuse la France entière sur 2006-2025 en une seule fois : le script l'exporte une année à la fois, et sa licence interdit de la publier modifiée : les données brutes restent hors du dépôt (D005). Copernicus demande un compte gratuit et fournit des fichiers NetCDF. La BD Forêt pèse près de 100 Mo pour la Côte-d'Or. Toutes les données sont téléchargées par les scripts, aucune n'est déposée sur GitHub.
- **Autre :** les codes des communes changent avec les fusions (6 codes disparus en Côte-d'Or depuis 2017) : une table de passage est prévue. Le format des fichiers de la Météo des forêts change selon l'année (séparateur, numéro de département), et ses heures sont en UTC.
