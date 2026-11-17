# Fiche source – BDIFF (Base de données sur les incendies de forêt en France)

- **Explorée par :** Audrey, le 2026-11-17
- **Pages de la source :** https://bdiff.agriculture.gouv.fr/ et https://www.data.gouv.fr/datasets/base-de-donnees-sur-les-incendies-de-forets-en-france-bdiff
- **Fichiers ouverts :** export CSV du portail (`Incendies.csv`) pour la Côte-d'Or de 2006 à 2025, plus deux exports de contrôle : Bourgogne-Franche-Comté 2024-2025 et France entière 2024-2025. Les pages « Généralités », « Définitions » et « Recherche » du portail, et le PDF des mentions légales fourni dans l'export.

## Description

La BDIFF centralise depuis 2006 les incendies de forêt en France : Hexagone, Corse et outre-mer. Les fiches sont saisies dans chaque département par les SDIS, les DDT(M), l'ONF et parfois les DRAAF. La police et la gendarmerie peuvent y renseigner la cause du feu. La collecte suit des campagnes annuelles, du 1er janvier au 31 décembre. Les fiches sont validées entre décembre et avril de l'année suivante, puis publiées (source : page « Généralités » du portail).

## Fiche d'identité

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Agriculture et de la Souveraineté Alimentaire (éditeur). Portail conçu et développé par l'IGN, hébergé par OVH. Sur data.gouv.fr, le jeu de données est publié au nom de l'IGN. |
| Mode d'accès et format | Export depuis le portail : on filtre (dates, département, région, surface…), puis le bouton « CSV » télécharge un `.zip`. Ce zip contient `Incendies.csv` (séparateur point-virgule, UTF-8), un PDF de définitions et un PDF de mentions légales. La fiche data.gouv.fr ne contient pas de fichier, seulement un lien vers le portail. |
| Grain (une ligne = ?) | Un incendie de forêt : année, numéro, département, code INSEE et nom de la commune, date et heure de première alerte, surfaces parcourues par type de végétation (en m²), précision des surfaces, nature (cause), dégâts. L'export indique le filtre « Type de feu : F » : il ne contient que les feux classés « forêt ». Le formulaire public n'a aucun filtre sur le type de feu, donc les autres feux de végétation ne peuvent pas être exportés en mode public. Les comptes authentifiés y ont peut-être accès : non vérifiée, faute de compte. |
| Emprise géographique | France entière : Hexagone, Corse et départements d'outre-mer. La localisation se fait à la **commune** (pas de coordonnées dans l'export). |
| Période réellement couverte par les données | Le formulaire propose des années depuis 1973, mais la BDIFF centralise les données depuis 2006. Les feux de 2025 sont publiés. 2026 est « en cours de saisie » et n'est pas diffusée. En Côte-d'Or, l'export 2006-2025 ne contient que **120 incendies**, le premier en 2012 : 2012 (1), 2014 (1), 2015 (8), 2017 (2), 2018 (3), 2019 (15), 2020 (42), 2021 (7), 2022 (32), 2023 (7), 2024 (0), 2025 (2). |
| Date de dernière mise à jour affichée sur la fiche | 13 décembre 2025 sur data.gouv.fr. Cette fiche annonce une couverture 2006-2022, alors que le portail diffuse jusqu'à 2025 : elle est en retard sur les données. |
| Fréquence de mise à jour | Annuelle : une campagne par année civile, publiée après validation (décembre à avril de l'année suivante). |
| Volumétrie | 120 lignes pour la Côte-d'Or (2006-2025) ; 70 lignes pour la Bourgogne-Franche-Comté (2024-2025) ; 3 908 lignes pour la France entière (2024-2025). 24 colonnes. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Le **code INSEE de la commune** (à joindre avec le COG de l'année concernée, car les communes fusionnent), le **code département** et la **date de première alerte**. L'identifiant d'un feu est le couple année + numéro. |
| Données personnelles | Aucune dans les colonnes de l'export : pas de nom, pas d'adresse. La colonne « Nature » (cause du feu) et les colonnes de dégâts (décès, bâtiments) sont sensibles, mais elles sont vides ou agrégées en Côte-d'Or. Ce point est à faire relire par Melvyn (qualité et conformité). |
| Licence | **Divergence.** data.gouv.fr indique la Licence Ouverte 2.0 (Etalab). Les mentions légales jointes à l'export disent autre chose : usage personnel, associatif ou professionnel autorisé, sans vente, avec citation de la source et **sans modification des données**. À trancher en groupe et à noter dans le journal des décisions. |
| Questions de mon analyse auxquelles elle pourrait répondre | **Question 1** et **question 2** : elle donne la date de chaque départ de feu, à croiser avec le niveau du même jour dans la Météo des forêts (source explorée par une autre personne du groupe). **Question 3** : elle donne la commune et la surface brûlée de chaque feu. **Question 4** : elle couvre toute la France. |

## Ce que j'ai découvert en ouvrant les fichiers

- **Très peu de feux pendant la période couverte par la Météo des forêts.** Les deux sources ne se recouvrent que de juin à septembre 2024 et 2025, car 2026 n'est pas encore publiée dans la BDIFF. Sur ces mois, on compte :

  | Emprise | Feux | Jours avec au moins un feu |
  |---|---|---|
  | Côte-d'Or | 2 (le 29 juin et le 30 juillet 2025) | 2 |
  | Bourgogne-Franche-Comté | 43 | 37 |
  | France entière | 2 632 | 233 |

  **Pour la Côte-d'Or seule, les questions 1 et 2 n'ont pas assez de données pour conclure.** Il faudra travailler à l'échelle de la région ou de la France, ou trouver un indice avec un historique plus long (IFM).
- **Beaucoup de feux au printemps :** 32 des 120 feux de Côte-d'Or ont eu lieu en mars-avril. La Météo des forêts ne couvre pas cette période. Cela peut expliquer les « feux partis des jours où l'indice était au plus bas » dont parle la commande.
- **Cause rarement renseignée :** la colonne « Nature » est vide pour 100 des 120 feux de Côte-d'Or.
- **Colonnes entièrement vides en Côte-d'Or :** type de peuplement, nombre de décès, bâtiments détruits, précision de la donnée.
- **Surfaces souvent estimées :** 63 feux sur 120 ont une surface estimée, 57 une surface mesurée. 70 feux font moins d'un hectare.
- **Changement de modèle en 2023 :** à la fusion avec Prométhée, les définitions des surfaces ont changé (portail, page « Définitions »). Les feux de 2022 et avant ne sont pas strictement comparables à ceux de 2023 et après.
- **Prudence demandée par le producteur :** la page « Généralités » demande d'analyser avec prudence les feux antérieurs à 2020 hors de l'aire méditerranéenne, ce qui est notre cas. Le pic de 2020 (42 feux) reflète peut-être en partie une meilleure saisie.
- **Une définition utile pour le glossaire :** le portail définit l'incendie de forêt comme un « incendie qui démarre en forêt ou qui se propage en forêt ou au sein de terres boisées », et la date d'alerte comme le moment où « l'information d'un départ de feu parvient au CODIS ».

## Vérifications complémentaires : la Côte-d'Or dans la région

Export de la Bourgogne-Franche-Comté, 2006-2025 : **752 incendies de forêt**, sous le même filtre « Type de feu : F ».

**Nombre de feux par département et par année :**

| Dép. | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 21 Côte-d'Or | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 8 | 0 | 2 | 3 | 15 | 42 | 7 | 32 | 7 | 0 | 2 | 120 |
| 25 Doubs | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 33 |
| 39 Jura | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 11 | 0 | 34 | 15 | 9 | 33 | 0 | 1 | 5 | 114 |
| 58 Nièvre | 1 | 0 | 0 | 1 | 3 | 6 | 3 | 0 | 0 | 8 | 9 | 1 | 2 | 13 | 6 | 0 | 9 | 4 | 1 | 11 | 78 |
| 70 Haute-Saône | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 1 | 0 | 0 | 0 | 44 | 0 | 4 | 0 | 0 | 2 | 58 |
| 71 Saône-et-Loire | 3 | 2 | 1 | 4 | 5 | 57 | 32 | 5 | 6 | 23 | 0 | 6 | 2 | 9 | 9 | 2 | 45 | 5 | 0 | 12 | 228 |
| 89 Yonne | 1 | 1 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 35 | 6 | 16 | 5 | 1 | 5 | 77 |
| 90 Territoire de Belfort | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 15 | 2 | 0 | 6 | 44 |

**Synthèse par département :**

| Dép. | Feux | Surface parcourue (ha) | Mars-avril | Juin-septembre | Cause vide |
|---|---|---|---|---|---|
| 21 Côte-d'Or | 120 | 439,6 | 32 | 84 | 100 |
| 25 Doubs | 33 | 43,2 | 6 | 16 | 26 |
| 39 Jura | 114 | 1 211,3 | 49 | 42 | 82 |
| 58 Nièvre | 78 | 310,5 | 14 | 59 | 48 |
| 70 Haute-Saône | 58 | 29,8 | 22 | 30 | 49 |
| 71 Saône-et-Loire | 228 | 459,0 | 69 | 116 | 203 |
| 89 Yonne | 77 | 200,8 | 17 | 55 | 60 |
| 90 Territoire de Belfort | 44 | 5,2 | 10 | 27 | 22 |

**Feux par mois, Côte-d'Or (2006-2025) :** mars 12, avril 20, mai 2, juin 10, juillet 31, août 33, septembre 10, octobre 2. Aucun en janvier, février, novembre ni décembre.

**Feux par mois, région (2006-2025) :** janvier 7, février 25, mars 93, avril 126, mai 61, juin 48, juillet 171, août 154, septembre 56, octobre 5, novembre 2, décembre 4.

**Ce que ces chiffres montrent :**
- **La Côte-d'Or est le 2e département de la région en nombre de feux** (120), derrière la Saône-et-Loire (228) et juste devant le Jura (114). Pour la surface brûlée, le Jura est loin devant (1 211 ha contre 440 ha).
- **Deux saisons de feux.** Sur la région, mars-avril (219 feux) pèse presque autant que juillet-août (325 feux). La Météo des forêts n'est publiée qu'à partir de fin mai ou début juin : le pic de printemps lui échappe.
- **Les années se ressemblent d'un département à l'autre.** 2020 et 2022 sont des années fortes presque partout (sécheresse). 2024 est quasi vide, sauf dans le Doubs (24 feux).
- **Avant 2015, les chiffres sont très faibles** dans presque tous les départements, à l'exception de la Saône-et-Loire en 2011-2012. Cela confirme l'avertissement du producteur sur les données anciennes hors aire méditerranéenne : l'absence de feu avant 2015 peut venir d'une saisie incomplète, pas d'une absence réelle de feux.
- **La cause du feu est rarement connue** : la colonne « Nature » est vide pour 590 feux sur 752 dans la région.
