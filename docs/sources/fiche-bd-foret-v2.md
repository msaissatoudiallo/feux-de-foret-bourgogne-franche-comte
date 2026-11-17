# Fiche source - BD Forêt V2

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | IGN (Institut national de l'information géographique et forestière). Les zones de forêt sont dessinées à partir des photos aériennes de la BD ORTHO. |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement d'une archive .7z par département sur le site de l'IGN (geoservices.ign.fr). Format shapefile (carte), projection Lambert 93. Aussi disponible en flux WMS / WFS. |
| Grain (une ligne = ?) | Une zone de végétation d'au moins 5 000 m², avec son type de forêt et son essence. |
| Emprise géographique | Le fichier ouvert couvre la Côte-d'Or. La base existe pour tous les départements de France métropolitaine. |
| Période réellement couverte par les données | État de la forêt en 2017 pour la Côte-d'Or (photos de 2017, d'après les métadonnées du fichier). |
| Date de dernière mise à jour affichée sur la fiche | 16/11/2026 sur data.gouv.fr. Cette date vient de la mise à jour des liens WMS, pas des données. |
| Fréquence de mise à jour | Irrégulière (indiqué sur data.gouv.fr). |
| Volumétrie | 25 831 zones en Côte-d'Or. Archive de 30 Mo, fichier carte de 98 Mo une fois décompressé. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Un identifiant par zone (`ID`). Pas de code commune ni de code département dans la table : la jointure avec d'autres données doit se faire par la position géographique. |
| Données personnelles | Aucune. Les colonnes sont `ID`, `CODE_TFV`, `TFV`, `TFV_G11` et `ESSENCE` : elles décrivent seulement la végétation. |
| Licence | Licence Ouverte 2.0 (Etalab). |
| Questions de votre analyse auxquelles elle pourrait répondre | Q3 (où un feu ferait le plus de dégâts) : elle dit où sont les forêts et de quel type. Il faudra la croiser avec une autre source pour les habitations et les routes. |
