# Fiche d'identité – Admin Express (IGN)

- **Explorée par :** Aissatou Diallo
- **Date d'exploration :** 2026-11-18
- **Page de la source :** https://www.data.gouv.fr/datasets/5808de39c751df1e0679df72 (dans la liste du défi, groupe « Géographie et occupation des sols »)
- **Fichiers ouverts :** les communes de Côte-d'Or (`code_insee_du_departement = 21`) téléchargées en GeoJSON depuis le service en ligne de l'IGN (`https://data.geopf.fr/wfs`), pour trois éditions : la plus récente (`ADMINEXPRESS-COG.LATEST:commune`), 2020 et 2017.
- **Pourquoi cette source :** décidée en groupe le 18/11 pour relier les sources entre elles (communes, départements) et calculer la surface de forêt par commune, ce que les sources explorées ne permettent pas.

## Fiche

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Institut national de l'information géographique et forestière (IGN). Les versions « COG » utilisent le Code officiel géographique de l'INSEE au 1er janvier de l'année (description de la fiche data.gouv.fr). |
| Mode d'accès et format | Deux accès : téléchargement de fichiers **Shapefile** (carte) sur le site de l'IGN, pour toute la France, et **service en ligne WFS** (`https://data.geopf.fr/wfs`), qui permet de ne télécharger qu'une partie (ex. un département) en GeoJSON. Exploré : le service WFS. Les fichiers Shapefile n'ont pas été ouverts. |
| Grain (une ligne = ?) | **Une commune** (édition récente) : nom officiel, code INSEE, codes du canton, de l'arrondissement, du département et de la région, code SIREN, code postal, population, superficie cadastrale et contour de la commune. Le produit contient aussi d'autres couches (départements, régions, cantons, EPCI…). |
| Emprise géographique | France métropolitaine et départements d'outre-mer (description data.gouv.fr). Fichier ouvert : la Côte-d'Or. |
| Période réellement couverte par les données | Une édition par année, de **2017 à 2026** (couches `ADMINEXPRESS-COG.2017` à `.2026` du service WFS, plus `.LATEST`). Chaque édition décrit les communes telles qu'elles existaient à cette date. Pas d'édition avant 2017 dans ce produit. |
| Date de dernière mise à jour affichée sur la fiche | 19 octobre 2026 (data.gouv.fr). |
| Fréquence de mise à jour | Mensuelle (indiquée sur data.gouv.fr). |
| Volumétrie | Côte-d'Or, édition la plus récente : **698 communes**, fichier GeoJSON d'environ 10,7 Mo. Édition 2017 : 704 communes. Taille des fichiers de toute la France : non vérifiée (non téléchargés). |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | **Code INSEE de la commune** (`code_insee`, 5 caractères, ex. `21329`) : aucun code vide ni en double dans le fichier ouvert. **Code du département** (`code_insee_du_departement`, ex. `21`) et **code de la région**. C'est la même clé que la colonne « code INSEE de la commune » de la BDIFF. Attention : **les noms de colonnes changent selon l'édition** (`insee_com` et `insee_dep` en 2017 et 2020, `code_insee` et `code_insee_du_departement` dans l'édition récente). |
| Données personnelles | Aucune : des limites administratives, des codes et des totaux de population. |
| Licence | Licence Ouverte / Open Licence version 2.0 (Etalab), indiquée sur data.gouv.fr. |
| Questions de mon analyse auxquelles elle pourrait répondre | Elle ne répond seule à aucune question : c'est un **référentiel** qui permet de relier les autres sources. **Q1** (reformulée par département) : elle donne les départements et les communes pour rattacher chaque feu de la BDIFF. Pour le groupe : question sur les zones des feux (feux par commune et par km² de forêt, en croisant avec la BD Forêt V2). |

## Ce que j'ai découvert

- **Les fusions de communes changent les codes.** La Côte-d'Or comptait **704 communes en 2017** et en compte **698** depuis 2020 : **6 codes INSEE ont disparu** (21073, 21213, 21486, 21507, 21513, 21621, dont Bierre-lès-Semur, Crimolois, Pluvault et Premières). Un feu enregistré dans la BDIFF avec un ancien code ne se reliera pas à l'édition récente. Il faudra soit utiliser l'édition de l'année du feu, soit une table de passage des anciens codes vers les nouveaux. À vérifier avec l'export de la BDIFF : combien de feux portent un de ces 6 codes.
- **Les colonnes ne s'appellent pas pareil d'une édition à l'autre.** Le chargement devra renommer les colonnes selon l'édition.
- **Système de coordonnées :** le service WFS renvoie les contours en coordonnées GPS (EPSG:4326), alors que la BD Forêt V2 est en Lambert 93. Pour croiser les deux (surface de forêt par commune), il faudra d'abord les mettre dans le même système.
- **La superficie cadastrale** est donnée pour chaque commune (ex. 450 pour Juilly), mais son unité n'est pas indiquée dans le fichier : non vérifiée.
- **Conclusion :** source indispensable pour le schéma de l'entrepôt. Le code INSEE de la commune et le code du département peuvent servir de clés, à condition de gérer les fusions de communes.
