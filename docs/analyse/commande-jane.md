# Analyse de la commande - Jane

 Commande des pompiers de Côte-d'Or (SDIS 21), région Bourgogne-Franche-Comté.

## 1. Les questions

1. **Où il y a le plus de feux en Côte-d'Or ?** (par commune ou par zone de caserne, sur les derniers étés)
   - Si c'est toujours aux mêmes endroits, on envoie les patrouilles et l'argent là-bas.
   - Si c'est un peu partout, pas la peine de cibler, on mise plutôt sur des équipes qui bougent et de la prévention partout.

2. **Quand la Météo des forêts annonce tel niveau, est-ce qu'il y a vraiment des feux ? Et ça arrive combien de jours par été ?**
   - Si les feux arrivent surtout à partir d'un certain niveau, et qu'on a assez d'argent pour renforcer tous ces jours-là → on met le seuil à ce niveau.
   - Si les feux arrivent à n'importe quel niveau → l'indice seul ne suffit pas, il faut le mélanger avec autre chose (les endroits à risque de la question 1, ou certaines périodes).

3. **Les feux qui partent alors que l'indice est bas, ils ont un truc en commun ?** (même cause, même moment comme les moissons, même endroit, même taille)
   - S'ils ont la même cause (travaux dans les champs, gens qui brûlent des déchets…), on fait de la prévention là-dessus, pas besoin de baisser le seuil.
   - S'il y en a peu et qu'ils sont petits, on laisse le seuil comme il est.
   - S'il y en a beaucoup et qu'ils sont gros → on baisse le seuil.

4. **Avec le même niveau d'indice, est-ce que la Côte-d'Or a autant de feux que les départements voisins et que le reste de la France ?**
   - Si oui, on peut copier le seuil des voisins et s'organiser avec eux.
   - Si non, on fait un seuil rien que pour la Côte-d'Or, et on sait pourquoi.



## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| Météo des forêts | Une carte de Météo-France qui dit chaque jour si le risque de feu est faible ou fort | Qui la fait, depuis quand, est-ce qu'on peut voir les anciens jours, c'est par département ou par zone plus petite |
| Niveau / indice | Le niveau de danger affiché sur la carte | Il y a combien de niveaux ? « Indice » et « niveau », c'est pareil ? |
| Feu de forêt | Un feu dans une forêt | À partir de quelle taille ça compte ? Les feux de buissons ou de champs, ça compte aussi ? |
| Départ de feu | Là où le feu commence, et quand | Les tout petits feux éteints direct, on les compte ? |
| Dispositif renforcé | Les moyens en plus quand le risque est fort : patrouilles, surveillance… | Il y a quoi dedans exactement, et ça coûte combien par jour ? |
| Seuil actuel | Le niveau à partir duquel les pompiers renforcent aujourd'hui | C'est quel niveau ? Partout dans le département ou juste à certains endroits ? |
| Moyens humains et financiers | Les pompiers, les camions et l'argent | On compte comment : en nombre de personnes, en jours, en euros ? |
| Été / saison des feux | De juin à septembre | Le mail parle aussi du printemps, donc c'est quelle période ? |
| « Autant de feux que l'été 2026 » | Le nombre de feux de l'été 2026 | On parle du nombre de feux ou de la surface brûlée ? Le chiffre vient d'où ? |
| Territoire national | La France métropolitaine | Avec l'outre-mer ou pas ? |
| Guet | Surveiller depuis un endroit en hauteur pour voir les fumées | Il y a des tours de guet en Côte-d'Or ? |
| Chef de centre | Le chef d'une caserne de pompiers | On peut découper le département par zone de caserne ? |

## 3. Les besoins

La décision à éclairer, en une phrase :

**Où et à partir de quel niveau de la Météo des forêts les pompiers de Côte-d'Or doivent renforcer la surveillance l'été prochain, vu qu'ils n'ont pas assez d'argent pour le faire partout et tout le temps ?**

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
- Le seuil utilisé en ce moment.
- Le budget : on peut payer le renfort combien de jours, et sur combien de zones.
- Le prix d'une journée de renfort.
- Ce qu'ils veulent dire par « où » : une commune, une forêt, la zone d'une caserne ?
- Ce que les pompiers appellent un « feu de forêt » (les feux de champs, ça compte ?).
- Si on peut avoir les données des interventions des pompiers de Côte-d'Or.
- Ce qui les embête le plus : les alertes pour rien, ou les feux qui arrivent sans renfort ?
- La période exacte à regarder (avec le printemps ou pas).

## 4. Les données



| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | La liste des feux avec la date, la commune, la surface brûlée et la cause, plus les zones des casernes et la surface de forêt par commune | Un feu | Les 10 derniers étés à peu près, 2026 compris | Avec tout l'été 2026 | Côte-d'Or, par commune |
| 2 | Le niveau de la météo des forêts de chaque jour, avec le nombre de feux ce jour-là | Un jour dans une zone | Tous les étés depuis que la météo des forêts existe | Avec tout l'été 2026 | Côte-d'Or, par zone de prévision |
| 3 | La liste des feux de la question 1, avec la cause, l'heure, la surface et le niveau d'indice du jour | Un feu | Même période que la question 1 | Avec tout l'été 2026 | Côte-d'Or |
| 4 | Le niveau de la météo des forêts de chaque jour et le nombre de feux de chaque jour, pour chaque département | Un jour dans un département | Même période que la question 2 | Avec tout l'été 2026 | Les 8 départements de Bourgogne-Franche-Comté et toute la France métropolitaine |

## 5. Confrontation aux sources

### Matrice

| Question | BDIFF | Météo des forêts | EFFIS | SIM2 | BD Forêt V2 | Interventions SDIS | Stats SDIS |
|---|---|---|---|---|---|---|---|
| 1 | partiel : la commune, la date et la surface de chaque feu, mais pas l'été 2026 et la cause est vide pour 100 feux sur 120 (Grain, Période) | absent : un niveau par département, aucun feu (Grain) | inconnu : la carte des zones brûlées 2018-2025 n'a pas été vérifiée, les petits feux ne sont peut-être pas vus | absent : de la météo, aucun feu (Grain) | partiel : où sont les forêts, mais état de 2017 et pas de code commune (Période, Clés) | absent : un total par département et par an (Grain) | absent : un total par département et par an (Grain) |
| 2 | partiel : la date de chaque feu, mais pas de niveau d'indice (Grain) | partiel : colonne `niveau_j1`, mais seulement depuis juin 2024 et pendant la saison (Période) | partiel : le FWI sur plusieurs années, mais en images et sans département (Grain, Clés) | partiel : la météo de chaque jour, mais pas le niveau de l'indice (Grain) | absent : des zones de végétation, aucun feu (Grain) | absent : un total par an, pas de jour (Grain) | absent : un total par an, pas de jour (Grain) |
| 3 | partiel : l'heure, la commune et la surface de chaque feu, mais la cause est vide pour 100 feux sur 120 (colonne « Nature ») | partiel : colonne `niveau_j1`, mais pas au printemps, alors que 32 feux sur 120 sont en mars-avril (Période) | partiel : le FWI en images, sans département (Grain, Clés) | partiel : la météo de chaque jour, printemps compris, mais pas le niveau de l'indice (Grain) | absent : des zones de végétation, aucun feu (Grain) | absent : un total par an (Grain) | absent : un total par an (Grain) |
| 4 | partiel : toute la France avec la date de chaque feu, mais seulement 2 feux en Côte-d'Or sur la période de l'indice (Emprise, Période) | partiel : les 96 départements jour par jour, mais 3 saisons seulement (Emprise, Période) | partiel : le FWI en images, sans département (Grain, Clés) | absent : pas de niveau d'indice ni de feu (Grain) | absent : aucun feu ni indice (Grain) | partiel : colonne « Feux de végétations » par département et par an, mais sans jour ni indice (Grain) | absent : pas de nombre de feux par département (Grain) |

### Écarts avec la section 4

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1 | BDIFF | = | les 10 derniers étés → 2006 à 2025, presque rien avant 2015 | avec l'été 2026 → jusqu'à 2025 | = |
| 2 | BDIFF + Météo des forêts | un jour dans une zone → un jour dans un département | tous les étés de l'indice → étés 2024 et 2025 seulement | avec l'été 2026 → jusqu'à 2025 pour les feux | Côte-d'Or par zone → 2 feux seulement en Côte-d'Or |
| 3 | BDIFF + Météo des forêts | = | même période que la question 1 → étés 2024 et 2025 seulement, sans le printemps | avec l'été 2026 → jusqu'à 2025 | Côte-d'Or → 2 feux seulement |
| 4 | BDIFF + Météo des forêts | = | même période que la question 2 → étés 2024 et 2025 seulement | avec l'été 2026 → jusqu'à 2025 pour les feux | = |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1 | L'été 2026 et les zones des casernes | renoncer | On reformule : où il y a le plus de feux par commune, de 2015 à 2025. Les zones des casernes ne sont dans aucune source ouverte | Pas d'info sur 2026, et pas de découpage par caserne |
| 2 | Assez de feux en Côte-d'Or quand l'indice existe | approximer | On prend les feux de la région (43) et de la France (2 632) sur les étés 2024 et 2025 | Deux étés seulement, et la région ne réagit peut-être pas comme la Côte-d'Or |
| 3 | La cause des feux, et l'indice au printemps | approximer | On compare le moment (mois, heure), la commune et la taille des feux, à la place de la cause | On ne saura pas pourquoi les feux partent, et les feux de printemps restent sans niveau d'indice |
| 4 | Plus de 2 feux en Côte-d'Or sur la période de l'indice | approximer | On compare la région et la France sur les étés 2024 et 2025, et la Côte-d'Or seulement en nombre de feux | Résultat fragile, et pas de seuil propre à la Côte-d'Or |
