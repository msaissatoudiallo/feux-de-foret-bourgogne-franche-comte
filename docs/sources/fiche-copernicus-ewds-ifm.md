# Fiche d'identité – Copernicus EWDS : historique de l'Indice Forêt Météo (IFM)

- **Explorée par :** Aissatou Diallo
- **Date d'exploration :** 2026-11-18
- **Nom exact :** *Fire danger indices historical data from the Copernicus Emergency Management Service* (identifiant `cems-fire-historical-v1`)
- **Page de la source :** https://ewds.climate.copernicus.eu (Copernicus Emergency Management Service – Early Warning Data Store), dans la liste du défi, groupe « Historique de feux »
- **Fichier ouvert :** un extrait téléchargé le 18/11/2026 : variable *Fire weather index*, réanalyse consolidée, **30 juillet 2025**, grille 0,25°, zone autour de la Bourgogne-Franche-Comté (nord 48,5 ; ouest 2,8 ; sud 46,1 ; est 7,2), format NetCDF.
- **Pourquoi cette source :** décidée en groupe le 18/11 pour combler le manque d'historique de la Météo des forêts (disponible seulement depuis juin 2024).

## Fiche

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Copernicus Emergency Management Service (programme de l'Union européenne). Les données sont produites par le Centre européen de prévisions météorologiques à moyen terme (ECMWF) pour le Centre commun de recherche (JRC), qui gère EFFIS. L'indice est calculé à partir de la réanalyse météorologique **ERA5** (description du catalogue). |
| Mode d'accès et format | Formulaire de téléchargement sur le site, **avec un compte gratuit** et l'acceptation des conditions d'utilisation (vérifié). La demande passe dans une file d'attente, puis le fichier se télécharge. On choisit la variable, les dates, la grille (0,25° ou 0,5°) et une zone. Formats : **GRIB** ou **NetCDF**. Le fichier ouvert est un NetCDF converti depuis le GRIB (attribut `history`). Le catalogue indique aussi un accès par programme (API) : non testé. |
| Grain (une ligne = ?) | **Une maille de 0,25° × 0,25° pour un jour** : une valeur d'IFM (variable `fwinx`) par maille. Ce n'est pas un tableau mais une **grille** (latitude × longitude). Par calcul, une maille mesure environ 28 km du nord au sud et 19 km d'est en ouest à la latitude de Dijon. |
| Emprise géographique | Le monde entier (catalogue), avec sélection d'une zone au téléchargement. Fichier ouvert : 10 latitudes × 18 longitudes = **180 mailles** autour de la Bourgogne-Franche-Comté, dont environ 20 sur la Côte-d'Or. |
| Période réellement couverte par les données | D'après le catalogue : **du 3 janvier 1940 au 14 novembre 2026**, un jour par jour, toute l'année. Vérifié dans le fichier : la date du 30 juillet 2025 (colonne `valid_time`, en secondes depuis le 1er janvier 1970, heure UTC). Les autres années : non vérifiées (non téléchargées). |
| Date de dernière mise à jour affichée sur la fiche | 16 novembre 2026 (catalogue). **Avertissement affiché sur la page : les mises à jour s'arrêtent à partir du 16 novembre 2026, jusqu'à nouvel ordre.** Sans conséquence pour nous, qui utilisons l'historique. |
| Fréquence de mise à jour | Quotidienne (catalogue), mais interrompue depuis le 16/11/2026 (voir ci-dessus). |
| Volumétrie | Fichier ouvert : 180 valeurs (un jour, zone de la région), **25 Ko**. Pour 2012 à 2025 sur la même zone, il faudrait environ 5 100 jours : volume non vérifié (non téléchargé). |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | La **date** (`valid_time`) et les **coordonnées** de chaque maille (`latitude`, `longitude`). **Pas de code de commune ni de département** : pour relier l'IFM à un feu de la BDIFF ou à un département, il faudra superposer les mailles aux contours des communes d'[Admin Express](fiche-admin-express.md). |
| Données personnelles | Aucune : des valeurs d'indice calculées sur une grille. |
| Licence | **CC-BY 4.0** (catalogue) : réutilisation libre, à condition de citer la source. L'acceptation des conditions d'utilisation est demandée avant le téléchargement. |
| Questions de mon analyse auxquelles elle pourrait répondre | **Q3** (taille des feux selon le niveau de l'indice) et **Q4** (erreurs de l'indice en Côte-d'Or et ailleurs) : elle donne l'IFM **pour chaque jour de feu de la BDIFF depuis 2012**, printemps compris, au lieu de 2 étés seulement. **Q1** (reformulée par département) : en moyennant les mailles de chaque département. |

## Ce que j'ai découvert

- **Un exemple concret de « feu par indice bas » :** le 30 juillet 2025, jour d'un feu en Côte-d'Or dans la BDIFF, l'IFM des mailles de Côte-d'Or va de **1,6 à 7,5** (4,8 pour la maille la plus proche de Dijon). Le même jour, la **Météo des forêts** donnait le **niveau 1 (faible)** pour la Côte-d'Or (fichier `mdf_2025.csv.gz`, colonne `niveau_j1`, bulletins du 29 et du 30 juillet). C'est exactement la situation décrite par les chefs de centre dans la commande.
- **Même famille que EFFIS :** la description indique que ces données font partie du jeu produit pour [EFFIS](fiche-effis.md). EFFIS montre le même indice (FWI) sous forme d'**images** ; Copernicus EWDS donne les **valeurs numériques** sur un long historique. Pour l'indice, Copernicus EWDS est donc la version exploitable. EFFIS garde ce qui lui est propre : les zones brûlées et les totaux par pays.
- **L'IFM n'est pas le niveau de la Météo des forêts.** L'IFM est une valeur continue (de 0,08 à 13,7 dans le fichier ouvert), alors que la Météo des forêts donne un niveau de 1 à 4. La correspondance entre les deux n'est pas donnée par la source : non vérifiée. On pourra l'estimer en comparant les deux sources sur 2024 à 2026.
- **Il faudra un traitement géographique :** les mailles ne suivent pas les limites des communes ni des départements (une maille peut chevaucher deux départements).
- **Format plus technique :** le NetCDF demande une bibliothèque spécialisée pour être lu (pas de simple CSV).
- **Conclusion :** c'est la source qui réduit le plus le manque principal du projet (l'historique de l'indice). Elle demande un compte, un format technique et une jointure par la carte.
