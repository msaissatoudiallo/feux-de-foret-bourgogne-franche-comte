# Inventaire des sources

Mise en commun des fiches d'identité de l'exercice 2. Chaque source a sa fiche détaillée dans ce dossier.

Dernière mise à jour : 2026-11-18

## Tableau

| Source | Explorée par | Pertinente pour nos questions ? | Ce que nous avons découvert |
|---|---|---|---|
| [BDIFF](fiche-bdiff.md) – Base de données sur les incendies de forêt en France | Audrey | **Oui, c'est la source centrale.** Elle sert aux questions sur les zones (commune), les périodes (date et heure), la taille des feux (surface) et la comparaison entre départements. | Une ligne = un incendie de forêt, avec la commune, la date et l'heure de première alerte, et la surface parcourue. Seulement **120 feux en Côte-d'Or entre 2006 et 2025**, presque aucun avant 2015 (le producteur demande de la prudence sur les données anciennes hors de l'aire méditerranéenne). Beaucoup de feux au **printemps** (32 en mars-avril). Cause inconnue pour 100 feux sur 120. Les définitions des surfaces ont changé en 2023. **Licence contradictoire** : Licence Ouverte 2.0 sur data.gouv.fr, mais les mentions légales de l'export interdisent de modifier les données. |
| [Météo des forêts](fiche-meteo-des-forets.md) (archives) | Jane | **Oui**, pour les questions sur le seuil de déclenchement et la comparaison entre départements. Elle doit être croisée avec la BDIFF. | Une ligne = un département pour un jour, avec un niveau de 1 (faible) à 4 (très élevé). Données disponibles **seulement depuis juin 2024**, et **seulement pendant la saison** (fin mai à début octobre). Le sens exact des colonnes `niveau_j1` et `niveau_j2` reste à vérifier dans la documentation officielle. Les heures sont en UTC. |
| [EFFIS](fiche-effis.md) – European Forest Fire Information System | Jane | **En partie.** Son indice FWI pourrait compléter l'historique de la Météo des forêts. | Surtout des **cartes** (images WMS), pas des tableaux. Le FWI est donné par carrés de 8 km, sans code département. L'Excel ne donne que des totaux par pays. Les données anciennes sont disponibles **sur demande**, avec un délai inconnu. Licence non lue en détail. |
| [SIM2](fiche-sim2-meteo-france.md) – Météo-France | Melvyn | **En partie**, de façon indirecte (évolution des étés chauds et secs). | Météo quotidienne depuis 1958 sur une grille de 8 km (température, pluie, vent, humidité, sécheresse des sols). Pas d'indice de danger. Le département s'obtient par une table de correspondance. **Volumineux** : environ 137 Mo compressés par an. |
| [BD Forêt V2](fiche-bd-foret-v2.md) – IGN | Melvyn | **En partie**, pour savoir où sont les forêts et de quel type. | Une ligne = une zone de végétation d'au moins 5 000 m². État de la forêt en **2017** pour la Côte-d'Or. Pas de code commune ni de département : la jointure se fait par la position géographique (cartes). |
| [Interventions SDIS](fiche-interventions-sdis.md) – ministère de l'Intérieur | Aissatou | **Faible.** Seulement un ordre de grandeur pour comparer les départements. | Une ligne = un département sur une année (totaux d'interventions par type). La colonne « Feux de végétations » ne compte pas que les feux de forêt. La structure change selon les années (pas de détail des feux en 2011 et 2013). Problème d'encodage sur les nombres de 1 000 et plus. |
| [Statistiques nationales des SDIS](fiche-statistiques-nationales-sdis.md) – DGSCGC | Aissatou | **Faible** pour les feux. Utile pour comparer les **moyens** des SDIS. | Même enquête qu'Interventions SDIS (mêmes chiffres), mais en **PDF**, sans licence indiquée. Apporte en plus les effectifs et les budgets de chaque SDIS. L'édition d'une année décrit l'année précédente. |
| [Données climatologiques de base quotidiennes](fiche-donnees-climatologiques-quotidiennes.md) – Météo-France | Audrey | **Oui, en approximation.** Elle donne la météo réelle de chaque jour de feu, ce qui peut remplacer en partie l'indice là où la Météo des forêts n'existe pas (printemps, années avant 2024). | Une ligne = une station météo pour un jour (pluie, températures, vent, humidité…), de **1950 à 2026**, **toute l'année**. Les 120 jours de feu de Côte-d'Or de la BDIFF sont tous couverts par plusieurs stations. Mais le vent et l'humidité ne sont mesurés que par quelques stations (9 et 14 en Côte-d'Or), les stations n'ont pas de code commune (jointure par les coordonnées), et ce n'est **pas un niveau de danger** : il faudra choisir nos propres indicateurs (jours sans pluie, température maximale…). Volumineux : 1,5 million de lignes pour la seule Côte-d'Or. Licence Ouverte 2.0. |

## Bilan

### Quelles questions de nos analyses n'ont encore aucune source ?

- **Le coût d'une journée de dispositif renforcé et le budget disponible** : ce sont des données internes du SDIS 21, qu'aucune source ouverte ne donne.
- **Le délai d'arrivée des secours sur un feu** : aucune source explorée ne le contient.
- **Le niveau de danger au printemps** : la Météo des forêts n'est publiée que de fin mai à début octobre, alors qu'une partie importante des feux de Côte-d'Or a lieu en mars-avril. *Mise à jour du 18/11 : les Données climatologiques quotidiennes donnent la météo réelle au printemps. Ce n'est pas le niveau de danger officiel, mais c'est une approximation possible.*
- **Le seuil de déclenchement pour la Côte-d'Or seule** : la Météo des forêts et la BDIFF ne se recouvrent que sur les étés 2024 et 2025, et on ne compte que **2 feux** en Côte-d'Or sur cette période. C'est trop peu pour conclure. Il faudra travailler à l'échelle de la région ou de la France, ou trouver un indice avec un historique plus long. *Mise à jour du 18/11 : les Données climatologiques quotidiennes couvrent les 120 jours de feu de Côte-d'Or depuis 2012. On peut donc étudier la météo des jours de feu sur toute la période, mais avec nos propres indicateurs, pas avec l'indice officiel.*
- **Les enjeux menacés par un feu (habitations, routes)** : couverts seulement en partie. La BD Forêt V2 localise les forêts, mais aucune source explorée ne localise les habitations ni les routes (la BD TOPO, présente dans la liste du défi, n'a pas encore été explorée).

### Quelle source nous a surpris, et pourquoi ?

**La BDIFF.** Nous nous attendions à beaucoup de feux en Côte-d'Or. Il n'y en a que 120 en vingt ans, presque autant au printemps qu'en été, et la cause est rarement connue. Elle montre aussi que les plaintes des chefs de centre (« des feux partis des jours où l'indice était au plus bas ») peuvent s'expliquer par les feux de printemps, période où la Météo des forêts n'est pas publiée.

### Quelle source semble utile mais inexploitable dans le temps du projet ?

**EFFIS.** Son indice FWI aurait l'historique qui manque à la Météo des forêts. Mais il n'est disponible que sous forme d'images, sans découpage par département, et les données anciennes doivent être demandées par formulaire, avec un délai inconnu. L'exploiter avant le 11 décembre semble difficile.

## Points à trancher en groupe

- **La licence de la BDIFF** (divergence entre data.gouv.fr et les mentions légales du portail) : décision à prendre et à consigner dans le journal des décisions.
- **L'échelle de travail pour la question du seuil** (Côte-d'Or, région ou France), vu le très petit nombre de feux en Côte-d'Or sur la période couverte par la Météo des forêts : décision à prendre et à consigner dans le journal des décisions.
