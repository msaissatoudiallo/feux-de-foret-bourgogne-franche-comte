# Fiche source - EFFIS

Explorée par : Jane, le 17/11/2026
Trouvée sur : la page « Données et services » d'EFFIS (Copernicus), lien dans le défi data.gouv
J'ai regardé : la page des données, l'Excel `report_2024.xlsx` (Total par pays 2024), les cartes FWI (ECMWF et Météo-France), la carte des zones brûlées de la saison et les instructions de téléchargement

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | EFFIS, c'est le système européen sur les feux de forêt. C'est géré par la Commission européenne (le JRC) dans le cadre de Copernicus. Pour l'indice FWI il y a 2 versions, une ECMWF et une Météo-France |
| Mode d'accès (export, API, téléchargement) et format | Il n'y a pas un seul fichier, il y a plein de données différentes. La plupart passent par un serveur de cartes (WMS) : on change des paramètres dans le lien (la couche, la zone, la date) et on récupère une image en PNG ou TIFF. Il y a aussi des fichiers à télécharger : un Excel avec les totaux par pays, et les zones brûlées en Shapefile ou SpatiaLite. Pour les vieilles données qui ne sont pas sur le site, il faut faire une demande avec un formulaire |
| Grain (une ligne = ?) | Ça dépend. Dans l'Excel, une ligne = une année et une colonne = un pays. Pour le FWI, c'est une image de l'Europe pour un jour, avec des carrés de 8 km pour la version ECMWF. La taille des carrés de la version Météo-France, je ne l'ai pas trouvée |
| Emprise géographique | Toute l'Europe, et aussi le Moyen-Orient et l'Afrique du Nord (on le voit sur les cartes). Dans l'Excel il y a 31 pays dont la France (`FRA`), mais pas de détail par département. Sur les cartes FWI on voit bien la Bourgogne-Franche-Comté, mais en carrés, pas par département |
| Période réellement couverte par les données | Excel : de 1980 à 2024 pour la France (d'autres pays commencent plus tard). FWI : il faut mettre une date dans le lien (l'exemple des instructions est en 2021), donc on peut avoir des jours passés, mais je ne sais pas jusqu'à quand ça remonte. Cartes de gravité des zones brûlées : de 2018 à 2025 |
| Date de dernière mise à jour affichée sur la fiche | Non vérifiée, il n'y a pas de date de mise à jour sur la page |
| Fréquence de mise à jour | FWI : tous les jours (c'est une prévision à 1 jour). Zones brûlées : « en temps réel » d'après la page. Excel : un fichier par an |
| Volumétrie | Excel : 24 Ko, 2 onglets, 45 lignes (1980 à 2024) et 31 pays. Shapefile des zones brûlées : pas vérifié. FWI : une image par jour |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Excel : l'année et le code du pays (`FRA`). FWI : la date et les coordonnées, mais pas de code département. Pour le relier à nos départements, il faudrait mettre les carrés sur une carte des départements (avec Admin Express par exemple) |
| Données personnelles | Pas vu de données personnelles, il n'y a que des indices, des cartes et des totaux par pays |
| Licence | D'après les instructions, les données sont libres d'accès mais il faut respecter leur licence (page « data-license » sur le site d'EFFIS). Je n'ai pas lu le détail de la licence |
| Questions de mon analyse auxquelles elle pourrait répondre | Questions 2 et 4 : le FWI pourrait remplacer la Météo des forêts pour avoir plus d'années, mais il faut réussir à le ramener au département. Question 4 : l'Excel permet de comparer la France aux autres pays, mais pas la Côte-d'Or. Questions 1 et 3 : les zones brûlées montrent où il y a eu des feux, à voir pour notre région |

## Ce que j'ai remarqué

- EFFIS c'est surtout des cartes, pas des tableaux. Si on veut le FWI de la Côte-d'Or pour un jour, il faut prendre la carte de ce jour et regarder les carrés qui sont dans le département. C'est possible mais long, et il faut des outils pour les cartes.
- On peut avoir le FWI pour des jours passés, donc ça pourrait compléter la Météo des forêts qui n'a que 3 ans. Mais il reste à voir depuis quelle année, et si l'image TIFF donne les vraies valeurs ou juste des couleurs.
- L'Excel s'ouvre facilement mais les chiffres sont mal enregistrés : beaucoup sont en texte avec des espaces dedans (genre `22 176 `), alors que ceux de 2024 sont de vrais nombres. Il faudra les nettoyer. Pour la France en 2024 : 1 452 feux et 2 949 hectares brûlés.
- L'Excel est au niveau des pays, donc ça ne sert pas à comparer la Côte-d'Or avec les départements d'à côté.
- Sur la carte des zones brûlées de la saison, il y a très peu de points en France à part dans le sud. Les petits feux de chez nous ne sont peut-être pas vus par le satellite, à vérifier.
- Pour les données historiques pas dispo sur le site, il faut faire une demande par formulaire. On ne sait pas combien de temps ça prend, donc pas sûr qu'on les ait avant le 11 décembre.