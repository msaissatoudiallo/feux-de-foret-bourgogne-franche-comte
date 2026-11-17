# Fiche source - SIM2 Météo-France

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Les données sortent du modèle SIM (Safran - Isba), qui simule la météo et l'eau dans les sols sur une grille. Nom sur data.gouv.fr : « Données changement climatique - SIM quotidienne ». |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct. Un fichier CSV compressé (.csv.gz) par année, séparateur point-virgule. |
| Grain (une ligne = ?) | Un point de grille (maille d'environ 8 km) et un jour. |
| Emprise géographique | France métropolitaine et Corse. 134 points de grille sont en Côte-d'Or (d'après la table `SHP_SIM_FRANCE`). |
| Période réellement couverte par les données | Du 01/08/1958 au 16/11/2026 d'après les fichiers ouverts. data.gouv.fr indique un début au 01/01/1958, mais le fichier 1958 commence le 01/08/1958. |
| Date de dernière mise à jour affichée sur la fiche | 17/11/2026 sur data.gouv.fr. |
| Fréquence de mise à jour | Quotidienne sur les 60 derniers jours, tous les deux mois pour les quatre dernières années (indiqué sur data.gouv.fr). |
| Volumétrie | Environ 3,6 millions de lignes par an (2025 : 3 610 580 lignes, 9 892 points). Environ 137 Mo compressé par an. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `LAMBX` et `LAMBY` (coordonnées du point en Lambert II étendu, en hectomètres) et `DATE` (format AAAAMMJJ). Pas de code commune ni département dans les fichiers de données : il faut passer par la table `SHP_SIM_FRANCE`, qui donne le département (`num_dep`) de chaque point. |
| Données personnelles | Aucune. Ce sont des valeurs météo calculées sur une grille. |
| Licence | Licence Ouverte 2.0 (Etalab). |
| Questions de votre analyse auxquelles elle pourrait répondre | Q4 (les jours de danger élevé augmentent-ils d'un été à l'autre ?), de façon indirecte : la source ne donne pas le niveau de danger, mais la température, la pluie, le vent, l'humidité et la sécheresse des sols, ce qui permet de compter les jours chauds et secs chaque été. |
