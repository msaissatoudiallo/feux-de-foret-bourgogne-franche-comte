# Fiche source - Archives de la Météo des forêts

Explorée par : Jane, le 17/11/2026
Où je l'ai trouvée : page « Archives de la Météo des forêts » sur data.gouv.fr (lien dans le défi « Prévenir et détecter les feux de forêt »)
Fichier ouvert : `mdf.2026` (csv.gz)

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France (c'est marqué comme producteur sur data.gouv.fr) |
| Mode d'accès (export, API, téléchargement) et format | On télécharge les fichiers sur data.gouv.fr. Il y a un fichier par année : `mdf.2024`, `mdf.2025`, `mdf.2026`. Ce sont des CSV compressés (`csv.gz`). Les colonnes sont séparées par des `;` et pas par des virgules. Il y a aussi 3 fichiers d'explication : un zip d'exemples, une carte des départements (geojson) et un PDF de présentation |
| Grain (une ligne = ?) | Une ligne = un département pour un jour. Il y a 5 colonnes : `date`, `num_dep`, `niveau_j1`, `niveau_j2`, `nom_dep` |
| Emprise géographique | Les 96 départements de France métropolitaine (avec la Corse, `2A` et `2B`). Pas l'outre-mer. Nos 8 départements de Bourgogne-Franche-Comté (21, 25, 39, 58, 70, 71, 89, 90) sont bien dedans |
| Période réellement couverte par les données | Dans le fichier 2026 : du 28 mai au 5 octobre 2026, donc 131 jours, sans jour qui manque. Il n'y a que la saison des feux, pas toute l'année. Sur data.gouv.fr, c'est écrit que les données existent « depuis le 3 juin 2024 ». Je n'ai pas ouvert les fichiers 2024 et 2025, donc pas vérifié pour eux |
| Date de dernière mise à jour affichée sur la fiche | 5 octobre 2026 pour `mdf.2026` (25 juin 2026 pour `mdf.2025`, 24 juin 2026 pour `mdf.2024`) |
| Fréquence de mise à jour | Tous les jours (c'est écrit dans l'onglet « Informations »). Dans le fichier, il y a bien un bulletin par jour, publié vers 16 h 50. Mais data.gouv.fr affiche « Fréquence de mise à jour non respectée », sûrement parce qu'il n'y a plus de mise à jour en dehors de l'été |
| Volumétrie | 12 576 lignes dans `mdf.2026` (96 départements × 131 jours), 470 Ko. Aucune case vide. L'onglet « Structure de données » de data.gouv.fr donne les mêmes chiffres |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `num_dep`, le numéro du département. Il faut le garder en texte car il y a un zéro devant (`01`) et des lettres pour la Corse (`2A`, `2B`). Et `date`, mais il y a aussi l'heure dedans, en heure anglaise (UTC), donc il faudra la transformer pour garder seulement le jour |
| Données personnelles | Aucune. Il n'y a que des dates, des départements et des niveaux de danger |
| Licence | Licence ouverte / Open Licence version 2.0 |
| Questions de mon analyse auxquelles elle pourrait répondre | Question 2 (à quel niveau il y a vraiment des feux) et question 4 (comparer avec les autres départements et la France). Mais il faudra la mélanger avec une source qui liste les feux, comme la BDIFF |

## Ce que j'ai remarqué

- Il y a seulement 3 ans de données (2024, 2025 et 2026). Ça fait peu pour trouver à partir de quel niveau il y a vraiment des feux. Il faudra peut-être regarder EFFIS ou Copernicus qui ont plus d'années.
- Les niveaux vont de 1 à 4 : 1 = vert (faible), 2 = jaune (modéré), 3 = orange (élevé), 4 = rouge (très élevé). C'est expliqué dans la description de Météo-France sur data.gouv.fr.
- ~~Je ne sais pas encore exactement ce que veulent dire j1 et j2.~~ D'après le site feuxdeforet.fr, la carte donne le niveau pour le lendemain et le surlendemain, donc j1 = lendemain et j2 = surlendemain. ~~Mais ce n'est pas un site officiel, donc à vérifier.~~ → Vérifié le 19/11/2026 : le PDF de présentation de Météo-France, publié avec les fichiers sur data.gouv.fr, dit que la Météo des forêts est « délivrée chaque jour à 17h pour les deux prochains jours sous la forme de deux cartes (la première pour le lendemain et la seconde pour le surlendemain) ». Le PDF ne nomme pas les colonnes, mais d'après leur nom, `niveau_j1` correspond à la première carte (lendemain) et `niveau_j2` à la seconde (surlendemain). ~~Si c'est bien ça, il~~ Il faudra donc faire attention en reliant un niveau au jour d'un feu : la ligne datée du jour J donne, dans `niveau_j1`, le niveau prévu pour le jour J+1.
- Pour la Côte-d'Or en 2026, le niveau j1 a été à 1 pendant 62 jours, à 2 pendant 53 jours et à 3 pendant 16 jours. Jamais à 4.
- L'heure dans le fichier est en UTC (le Z à la fin), alors que sur l'aperçu de data.gouv.fr elle est affichée en heure française. Il faudra la convertir.