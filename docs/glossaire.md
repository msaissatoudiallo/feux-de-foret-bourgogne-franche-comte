# Glossaire — Bourgogne-Franche-Comté

Dernière mise à jour : 2026-11-23

Version 0. Les termes viennent des termes inconnus des quatre analyses de la commande (`docs/analyse/`), des termes rencontrés en ouvrant les sources (`docs/sources/`) et du cours sur les KPI (19/11/2026), puis du schéma de l'entrepôt (`docs/schema-entrepot.md`, ticket #146). Les entrées sont classées par ordre alphabétique. Un terme écarté est listé à la fin, avec la raison.

Statuts : **validé** (définition confirmée par la documentation d'un producteur ou par une décision du groupe consignée dans le journal), **proposé** (définition du groupe, non encore confirmée), **à vérifier** (une information manque), **obsolète**.

## Chef de centre

- **Définition :** responsable d'un centre d'incendie et de secours, c'est-à-dire d'une caserne de sapeurs-pompiers du département.
- **Sources et colonnes :** la commande (« certains chefs de centre estiment… ») ; le sigle CIS (« Centre d'incendie et de secours ») figure dans le glossaire de la plaquette « Les statistiques des services d'incendie et de secours » (DGSCGC, édition 2023).
- **Divergences :** aucune source ouverte ne donne la zone couverte par chaque centre de Côte-d'Or.
- **Règle retenue :** aucune pour l'instant (les zones des centres ne sont pas utilisées, voir D006).
- **Unité ou granularité :** un centre d'incendie et de secours.
- **Exemple :** les chefs de centre qui signalent des feux partis « des jours où l'indice était au plus bas » (commande).
- **Statut :** à vérifier.
- **Origine de la définition :** compréhension du groupe, sigle CIS de la plaquette DGSCGC.
- **Ajouté par :** Aissatou Diallo, Jane, 2026-11-17

## Clé primaire, clé étrangère, clé composée

- **Définition :** la **clé primaire** est la colonne qui identifie chaque ligne d'une table, sans doublon ; la **clé étrangère** est une colonne qui renvoie à la clé primaire d'une autre table, ce qui relie les deux tables ; la **clé composée** est une clé primaire formée de plusieurs colonnes ensemble.
- **Sources et colonnes :** schéma de l'entrepôt (`docs/schema-entrepot.md`, partie 6 ; `src/schema_silver.sql`).
- **Divergences :** la BDIFF n'a pas de clé unique : son numéro de feu est réutilisé d'une année à l'autre (12 916 numéros en double sur 2006-2025).
- **Règle retenue :** la clé de `fait_feu` est `id_feu` = année + numéro (0 doublon vérifié). Les clés sont écrites en texte (`code_departement` sur 2 caractères, `code_insee` sur 5 caractères), et la base vérifie chaque clé étrangère.
- **Unité ou granularité :** une ligne de table.
- **Exemple :** clé primaire `2022-13845` (un feu) ; clé étrangère `code_insee` de `fait_feu`, qui renvoie à `dim_commune` ; clé composée (`id_maille`, `date`) dans `fait_ifm_jour`.
- **Statut :** validé.
- **Origine de la définition :** vocabulaire des bases de données, appliqué dans le schéma v0 (ticket #41).
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Code INSEE de la commune

- **Définition :** code officiel à 5 caractères qui identifie une commune française, attribué par l'INSEE dans le Code officiel géographique (COG), mis à jour chaque 1er janvier.
- **Sources et colonnes :** BDIFF (code INSEE de la commune de chaque feu) ; Admin Express (`code_insee` dans l'édition récente, `insee_com` en 2017 et 2020).
- **Divergences :** les fusions de communes font disparaître des codes : la Côte-d'Or compte 704 communes en 2017 et 698 depuis 2020 (6 codes disparus). Un feu enregistré avec un ancien code ne se relie pas à l'édition récente d'Admin Express.
- **Règle retenue :** clé de jointure entre la BDIFF et Admin Express (D006). La gestion des anciens codes reste à décider (édition de l'année du feu ou table de passage).
- **Unité ou granularité :** une commune.
- **Exemple :** `21329` (Juilly) ; `21213` a disparu après 2017.
- **Statut :** validé.
- **Origine de la définition :** fiche data.gouv.fr d'Admin Express (Code officiel géographique de l'INSEE).
- **Ajouté par :** Aissatou Diallo, Audrey, 2026-11-19

## Couches bronze, silver et gold

- **Définition :** les trois étapes par lesquelles passent les données dans l'entrepôt. **Bronze** : les fichiers tels qu'ils ont été téléchargés. **Silver** : les données nettoyées et reliées par les clés. **Gold** : les tables prêtes pour les indicateurs et le tableau de bord.
- **Sources et colonnes :** bronze : `data/raw/` (hors de Git) ; silver : tables DuckDB `dim_*`, `fait_*` et `passage_commune` ; gold : tables `gold_*` (`docs/schema-entrepot.md`, partie 1).
- **Divergences :** aucune.
- **Règle retenue :** le bronze n'est jamais modifié (licence de la BDIFF, D005) ; le silver garde le grain le plus fin de chaque source (D024) ; le gold est recalculé depuis le silver, avec les réglages des indicateurs (seuil, période).
- **Unité ou granularité :** une couche.
- **Exemple :** le fichier `Incendies.csv` (bronze) devient la table `fait_feu` (silver), qui sert à `gold_commune` (gold).
- **Statut :** validé (D018, D024).
- **Origine de la définition :** architecture dite « médaillon », appliquée dans le schéma v0.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Danger élevé

- **Définition :** niveau de danger de feu où les conditions météorologiques et l'état de la végétation rendent un départ et une propagation de feu probables. Dans la Météo des forêts, c'est le niveau 3 (orange) sur 4.
- **Sources et colonnes :** Météo des forêts (`niveau_j1` = 3) ; classes de danger d'EFFIS pour l'IFM (« High » : 21,3 à 38,0) ; guide de Copernicus EWDS (IFM supérieur à 30).
- **Divergences :** trois définitions chiffrées : niveau 3 de la Météo des forêts, IFM de 21,3 à 38,0 pour EFFIS, IFM supérieur à 30 pour le guide de Copernicus EWDS. On ne sait pas quel niveau les chefs de centre désignent quand ils disent que l'indice « annonce un danger élevé ».
- **Règle retenue :** classe « élevé » d'EFFIS (IFM à partir de 21,3), vérifiée avec la Météo des forêts sur 2024-2026 (D008).
- **Unité ou granularité :** un département et un jour (Météo des forêts) ; une maille et un jour (IFM).
- **Exemple :** 16 jours au niveau 3 en Côte-d'Or en 2026 (fiche Météo des forêts).
- **Statut :** à vérifier (sens exact pour les chefs de centre).
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France) ; page « Fire danger forecast » d'EFFIS.
- **Ajouté par :** Aissatou Diallo, Audrey, 2026-11-17

## Délai d'intervention

- **Définition :** temps entre l'alerte d'un feu et l'arrivée des premiers secours sur place.
- **Sources et colonnes :** aucune source ouverte. La BDIFF donne seulement la date et l'heure de première alerte.
- **Divergences :** on ne sait pas à partir de quel moment le SDIS compte ce délai (appel, alerte des équipes, départ de la caserne).
- **Règle retenue :** donnée à demander au SDIS 21 ; sans réponse avant le 02/12/2026, la question G9 est abandonnée (D010).
- **Unité ou granularité :** un feu ; minutes.
- **Exemple :** non disponible.
- **Statut :** à vérifier.
- **Origine de la définition :** compréhension du groupe.
- **Ajouté par :** Melvyn, 2026-11-17

## Départ de feu

- **Définition :** début d'un feu, compté au moment où l'alerte est donnée, quelle que soit la taille que le feu atteindra.
- **Sources et colonnes :** BDIFF (date et heure de première alerte : « moment où l'information d'un départ de feu parvient au CODIS », page « Définitions » du portail) ; commande (« lutter au mieux contre les départs de feu »).
- **Divergences :** la BDIFF ne compte que les feux classés « forêt » (filtre « Type de feu : F » de l'export) ; les Interventions SDIS comptent des interventions pour feux de végétation. On ne sait pas si la direction compte aussi les feux éteints très vite.
- **Règle retenue :** un départ de feu est une ligne de la BDIFF ; sa date est la date de première alerte.
- **Unité ou granularité :** un feu ; un jour et une heure.
- **Exemple :** feu du 30 juillet 2025 en Côte-d'Or (BDIFF).
- **Statut :** à vérifier (prise en compte des feux éteints très vite).
- **Origine de la définition :** portail BDIFF (page « Définitions »), puis décision du groupe.
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-17

## Département

- **Définition :** division administrative identifiée par un code INSEE à 2 caractères (`21` pour la Côte-d'Or) ; c'est aussi, en général, le territoire d'un SDIS.
- **Sources et colonnes :** Météo des forêts (`num_dep`) ; Interventions SDIS (« Numéro ») ; Statistiques nationales des SDIS (annexes) ; Admin Express (`code_insee_du_departement`) ; SIM2 (`num_dep` dans la table `SHP_SIM_FRANCE`).
- **Divergences :** le territoire d'un SDIS ne coïncide pas toujours avec le département (Paris et la petite couronne sont couverts par la BSPP, Marseille par le BMPM). L'écriture du code change selon les sources : `2A` et `2B` pour la Corse, mais `2a` et `2b` dans les Statistiques nationales des SDIS ; sans zéro devant dans le fichier 2025 de la Météo des forêts (`1` pour l'Ain).
- **Règle retenue :** code INSEE du département, écrit en texte sur 2 caractères (`01`, `21`, `2A`). À consigner dans le journal au moment du chargement.
- **Unité ou granularité :** un département.
- **Exemple :** `21` = Côte-d'Or.
- **Statut :** validé (définition) ; format à décider.
- **Origine de la définition :** Code officiel géographique de l'INSEE (fiche Admin Express) ; fiches des sources.
- **Ajouté par :** Audrey, 2026-11-17

## Dimension et table de faits

- **Définition :** une **table de faits** enregistre des événements ou des mesures (un feu, une valeur d'indice un jour donné) ; une **dimension** décrit ce qui entoure ces mesures (quand, où) et sert à les filtrer et à les regrouper.
- **Sources et colonnes :** schéma de l'entrepôt, parties 3 et 4 : 6 dimensions (`dim_date`, `dim_departement`, `dim_commune`, `dim_maille`, `dim_station`, `passage_commune`) et 4 faits (`fait_feu`, `fait_ifm_jour`, `fait_mdf_jour`, `fait_meteo_jour`).
- **Divergences :** `passage_commune` ne commence pas par `dim_`, mais elle est rangée avec les dimensions.
- **Règle retenue :** les faits ne portent que des clés étrangères vers les dimensions ; les rattachements par la carte (mailles, stations) sont faits une seule fois, dans les dimensions.
- **Unité ou granularité :** une table.
- **Exemple :** `fait_feu` renvoie à `dim_date` (le jour de l'alerte) et à `dim_commune` (la commune du feu).
- **Statut :** validé.
- **Origine de la définition :** vocabulaire de la modélisation en étoile, appliqué dans le schéma v0.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Dispositif renforcé

- **Définition :** moyens supplémentaires que le SDIS déclenche quand le danger de feu est fort : patrouilles, guet, etc.
- **Sources et colonnes :** commande uniquement.
- **Divergences :** son contenu exact, sa zone de déclenchement et le coût d'une journée ne sont pas connus.
- **Règle retenue :** coût demandé au SDIS 21 ; sans réponse, il est exprimé en nombre de jours de dispositif (D009).
- **Unité ou granularité :** un jour de dispositif.
- **Exemple :** non disponible.
- **Statut :** à vérifier.
- **Origine de la définition :** commande.
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-17

## Donnée

- **Définition :** information brute, telle qu'elle est enregistrée dans une source : une case ou une ligne d'un fichier.
- **Sources et colonnes :** toutes les sources (ex. date et heure de première alerte de la BDIFF, `fwinx` de Copernicus EWDS).
- **Divergences :** pendant la semaine, la professeure a employé « donnée », « métrique », « indicateur » et « KPI » comme des synonymes. Le groupe les distingue comme dans ce glossaire.
- **Règle retenue :** une donnée n'est jamais modifiée dans la couche bronze (D005).
- **Unité ou granularité :** celle de la source (un feu, un jour, une maille…).
- **Exemple :** la date et l'heure de première alerte d'un feu dans la BDIFF.
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Enjeux

- **Définition :** ce qu'un feu menace : habitations, routes, zones sensibles.
- **Sources et colonnes :** Admin Express (`population` de chaque commune) ; BD Forêt V2 (localisation des forêts) ; PDF de la Météo des forêts (« 80 % des feux se déclenchent à moins de 50 m des habitations »).
- **Divergences :** aucune source explorée ne localise les habitations ni les routes (la BD TOPO n'a pas été explorée).
- **Règle retenue :** approchés par la population de chaque commune et la surface de forêt (D011).
- **Unité ou granularité :** une commune.
- **Exemple :** Juilly, 41 habitants (Admin Express).
- **Statut :** proposé.
- **Origine de la définition :** compréhension du groupe ; PDF de présentation de la Météo des forêts.
- **Ajouté par :** Melvyn, 2026-11-17

## Feu de forêt

- **Définition :** incendie qui démarre en forêt ou qui se propage en forêt ou au sein de terres boisées.
- **Sources et colonnes :** BDIFF (export filtré sur « Type de feu : F ») ; commande (« feux de forêt »).
- **Divergences :** les Interventions SDIS ne comptent pas les feux de forêt à part, mais des « feux de végétations » (forêts, champs, broussailles). En 2024, la Côte-d'Or compte 0 feu de forêt dans la BDIFF et 161 feux de végétation dans les Interventions SDIS.
- **Règle retenue :** les feux de forêt comptés sont ceux de la BDIFF. À consigner dans le journal.
- **Unité ou granularité :** un feu.
- **Exemple :** 120 feux de forêt en Côte-d'Or de 2006 à 2025 (BDIFF).
- **Statut :** validé.
- **Origine de la définition :** portail BDIFF (page « Définitions »).
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-17

## Feu de végétation

- **Définition :** feu qui brûle de la végétation au sens large : forêts, mais aussi champs, broussailles, landes.
- **Sources et colonnes :** Interventions SDIS (colonne « Feux de végétations »).
- **Divergences :** plus large que le feu de forêt de la BDIFF (voir « Feu de forêt »). Les fichiers 2011 et 2013 des Interventions SDIS ne détaillent pas les feux de végétation (un seul total « Incendies »).
- **Règle retenue :** non utilisé pour compter les feux de forêt ; peut servir à estimer la complétude de la BDIFF (matrice, sources à interroger).
- **Unité ou granularité :** un département sur une année.
- **Exemple :** 161 feux de végétation en Côte-d'Or en 2024.
- **Statut :** à vérifier (définition exacte de la DGSCGC non lue).
- **Origine de la définition :** fiche Interventions SDIS ; compréhension du groupe.
- **Ajouté par :** Melvyn, 2026-11-17

## Grain

- **Définition :** ce que représente une ligne d'une table.
- **Sources et colonnes :** colonne « Une ligne = » des tableaux du schéma de l'entrepôt (`docs/schema-entrepot.md`).
- **Divergences :** le mot « maille » est parfois employé dans ce sens ; dans ce projet, « maille » désigne seulement le carré de l'IFM (voir « Maille »).
- **Règle retenue :** le silver garde le grain le plus fin de chaque source ; les résumés (par département et par jour, par été) sont calculés en gold, pour pouvoir refaire les calculs avec un autre seuil ou une autre période (D024).
- **Unité ou granularité :** une table.
- **Exemple :** `fait_feu` : une ligne = un feu ; `fait_ifm_jour` : une ligne = une maille pour un jour.
- **Statut :** validé (D024).
- **Origine de la définition :** vocabulaire de la modélisation, appliqué dans le schéma v0.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Guet

- **Définition :** surveillance depuis des points hauts pour repérer les fumées au plus tôt.
- **Sources et colonnes :** commande (« patrouilles, guet »).
- **Divergences :** on ne sait pas s'il existe des postes de guet en Côte-d'Or, ni combien.
- **Règle retenue :** aucune.
- **Unité ou granularité :** un poste de guet.
- **Exemple :** non disponible.
- **Statut :** à vérifier.
- **Origine de la définition :** compréhension du groupe.
- **Ajouté par :** Jane, Melvyn, 2026-11-17

## IFM (Indice Forêt Météo)

- **Définition :** indice qui estime le danger météorologique de feu de forêt, en termes de probabilité d'éclosion, de vitesse de propagation et d'intensité du feu. Il est calculé au moment le plus défavorable de la journée à partir de la température, de l'humidité de l'air, de la vitesse du vent et des précipitations. C'est une valeur continue, sans unité.
- **Sources et colonnes :** Copernicus EWDS (`fwinx`, « Fire weather index ») ; EFFIS (cartes du FWI).
- **Divergences :** l'IFM n'est pas le niveau de la Météo des forêts : Météo-France le complète par l'état de sécheresse de la végétation (« Indice de danger intégré »). Les classes de danger de l'IFM diffèrent selon les versions d'EFFIS (voir D008).
- **Règle retenue :** IFM de Copernicus EWDS sur 2012-2025, traduit avec les classes de danger de la page EFFIS en vigueur (D008).
- **Unité ou granularité :** une maille de 0,25° et un jour.
- **Exemple :** 4,8 sur la maille la plus proche de Dijon le 30/07/2025.
- **Statut :** validé.
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France).
- **Ajouté par :** Melvyn, 2026-11-17

## Indicateur

- **Définition :** métrique utilisée pour juger une situation ou un objectif. Dès qu'on mesure un objectif SMART (le « M »), on manipule des indicateurs.
- **Sources et colonnes :** calculé à partir des données des sources.
- **Divergences :** voir « Donnée ».
- **Règle retenue :** chaque indicateur est rattaché à une hypothèse et à un objectif SMART (spec, section 3).
- **Unité ou granularité :** selon le calcul (pourcentage, nombre de jours…).
- **Exemple :** la part des feux de Côte-d'Or hors juin-septembre, comparée au seuil de 25 % de l'objectif SMART de H4 (spec, section 3).
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Indice de danger intégré

- **Définition :** indice calculé chaque jour par Météo-France à partir de l'IFM, complété par une analyse de l'état de sécheresse de la végétation. Il sert à établir le niveau de la Météo des forêts.
- **Sources et colonnes :** non diffusé dans les sources ouvertes explorées ; décrit dans le PDF de présentation de la Météo des forêts.
- **Divergences :** il n'existe pas de table publique de passage de l'IFM au niveau de la Météo des forêts.
- **Règle retenue :** remplacé par l'IFM et les classes d'EFFIS (D008).
- **Unité ou granularité :** non précisée (« échelle géographique très fine » d'après Météo-France).
- **Exemple :** non disponible.
- **Statut :** validé.
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France).
- **Ajouté par :** Aissatou Diallo, 2026-11-19

## Jour de feu

- **Définition :** jour où au moins un départ de feu a été enregistré dans la zone étudiée (commune, département ou région).
- **Sources et colonnes :** BDIFF (date de première alerte).
- **Divergences :** la Météo des forêts donne ses dates en heure UTC ; le fuseau horaire de la date d'alerte de la BDIFF n'a pas été vérifié.
- **Règle retenue :** un jour de feu est une date de première alerte de la BDIFF ; il sert à calculer la part des jours avec feu par niveau (matrice, G4).
- **Unité ou granularité :** un jour et une zone.
- **Exemple :** le 30/07/2025 est un jour de feu en Côte-d'Or.
- **Statut :** proposé.
- **Origine de la définition :** décision du groupe (matrice).
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-19

## KPI (indicateur clé)

- **Définition :** indicateur clé (*Key Performance Indicator*), directement lié à un objectif, dont la valeur peut faire changer une décision. Un KPI primaire par question analytique, et des KPI secondaires si besoin.
- **Sources et colonnes :** calculé à partir des données des sources.
- **Divergences :** voir « Donnée ».
- **Règle retenue :** chaque KPI est vérifié avec la grille RACER (pertinent, accepté, crédible [clair même pour un non-spécialiste], facile, robuste) et documenté dans une fiche indicateur.
- **Unité ou granularité :** selon le calcul.
- **Exemple :** la part des feux partis le week-end ou un jour férié, KPI primaire de H7 (spec, section 3).
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Maille

- **Définition :** carré de 0,25° de côté (environ 530 km² en Côte-d'Or), sur lequel Copernicus calcule une valeur d'IFM chaque jour.
- **Sources et colonnes :** Copernicus EWDS (`cems-fire-historical-v1`, variable `fwinx`) ; tables `dim_maille` et `fait_ifm_jour`.
- **Divergences :** une maille ne suit pas les limites des départements et peut déborder sur un département voisin.
- **Règle retenue :** une maille compte pour le département qui contient son centre ; elle est rattachée une seule fois, par la carte, dans `dim_maille` (département vide si le centre est en mer ou hors de France).
- **Unité ou granularité :** une maille.
- **Exemple :** `47.25_5.00` (centre à 47,25° de latitude et 5,00° de longitude).
- **Statut :** validé.
- **Origine de la définition :** documentation de Copernicus EWDS ; schéma v0.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Massif forestier

- **Définition :** ensemble de forêts d'un seul tenant.
- **Sources et colonnes :** aucune source explorée ne donne de découpage en massifs ; la BD Forêt V2 donne des zones de végétation d'au moins 5 000 m².
- **Divergences :** sans découpage officiel, deux personnes peuvent délimiter un massif différemment.
- **Règle retenue :** la commune remplace le massif comme zone d'étude (D006).
- **Unité ou granularité :** non définie.
- **Exemple :** non disponible.
- **Statut :** à vérifier.
- **Origine de la définition :** compréhension du groupe.
- **Ajouté par :** Audrey, 2026-11-17

## Météo des forêts

- **Définition :** dispositif d'information et de prévention de Météo-France, publié depuis 2023, qui donne chaque jour, pour chaque département de l'Hexagone et de la Corse, le niveau de danger de feu du lendemain et du surlendemain, sur une échelle de 4 niveaux. Il n'indique pas les incendies en cours ou à venir.
- **Sources et colonnes :** archives de la Météo des forêts sur data.gouv.fr (`date`, `num_dep`, `niveau_j1`, `niveau_j2`).
- **Divergences :** archives disponibles seulement depuis le 3 juin 2024, de fin mai ou début juin à l'automne.
- **Règle retenue :** utilisée pour vérifier la traduction de l'IFM en niveaux sur 2024-2026 (D008).
- **Unité ou granularité :** un département et un jour.
- **Exemple :** niveau 1 (faible) en Côte-d'Or pour le 30/07/2025.
- **Statut :** validé.
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France).
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-17

## Métrique

- **Définition :** valeur calculée à partir d'une ou de plusieurs données.
- **Sources et colonnes :** calculée à partir des données des sources.
- **Divergences :** voir « Donnée ».
- **Règle retenue :** chaque métrique a une formule écrite.
- **Unité ou granularité :** selon le calcul (pourcentage, nombre de jours…).
- **Exemple :** le nombre de feux partis le week-end, divisé par le nombre total de feux (BDIFF).
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Moyens humains et financiers

- **Définition :** les sapeurs-pompiers, le matériel et le budget dont dispose le SDIS pour lutter contre les feux.
- **Sources et colonnes :** Statistiques nationales des SDIS (annexes : effectifs professionnels et volontaires, dépenses de fonctionnement et d'investissement de chaque SDIS).
- **Divergences :** les statistiques donnent des totaux annuels pour tout le SDIS ; la commande parle des moyens que la direction peut déplacer d'une zone à une autre, qui ne sont pas connus.
- **Règle retenue :** aucune pour l'instant ; source « à interroger » dans la matrice.
- **Unité ou granularité :** un SDIS sur une année ; personnes et euros.
- **Exemple :** SDIS 21 en 2022 : 308 sapeurs-pompiers professionnels, 1 690 volontaires, 34 M€ de dépenses de fonctionnement.
- **Statut :** à vérifier.
- **Origine de la définition :** commande ; plaquette « Les statistiques des services d'incendie et de secours » (DGSCGC, édition 2023).
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, Melvyn, 2026-11-17

## Niveau de danger

- **Définition :** échelle à 4 niveaux de la Météo des forêts : faible (vert), modéré (jaune), élevé (orange), très élevé (rouge).
- **Sources et colonnes :** Météo des forêts (`niveau_j1`, `niveau_j2`, valeurs de 1 à 4).
- **Divergences :** l'IFM n'a pas de niveaux mais une valeur continue ; EFFIS le découpe en 6 classes (voir « Danger élevé » et D008). La commande parle aussi d'« indice » et de « seuil » pour désigner la même échelle.
- **Règle retenue :** pour 2012-2023, niveau approché par les classes d'EFFIS (D008).
- **Unité ou granularité :** un département et un jour.
- **Exemple :** niveau 1 en Côte-d'Or pour le 30/07/2025.
- **Statut :** validé.
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France).
- **Ajouté par :** Aissatou Diallo, Jane, 2026-11-17

## Niveau j1 / niveau j2

- **Définition :** dans chaque bulletin de la Météo des forêts, `niveau_j1` est le niveau de danger prévu pour le lendemain et `niveau_j2` celui du surlendemain.
- **Sources et colonnes :** Météo des forêts (`niveau_j1`, `niveau_j2`, et `date`, qui est la date du bulletin).
- **Divergences :** la fiche de la Météo des forêts indiquait ce sens comme « à vérifier » (source non officielle) ; il est confirmé par le PDF de Météo-France.
- **Règle retenue :** pour un feu du jour J, on lit `niveau_j1` du bulletin publié la veille (J-1) (D008).
- **Unité ou granularité :** un département et un jour.
- **Exemple :** le bulletin du 29/07/2025 donne `niveau_j1` = 1 pour la Côte-d'Or, c'est-à-dire pour le 30/07/2025.
- **Statut :** validé.
- **Origine de la définition :** PDF de présentation de la Météo des forêts (Météo-France).
- **Ajouté par :** Jane, Aissatou Diallo, 2026-11-19

## Paramètre

- **Définition :** valeur qu'on peut faire varier dans le calcul d'un KPI, pour observer son effet sur le résultat.
- **Sources et colonnes :** choisi par le groupe, pas lu dans une source.
- **Divergences :** aucune.
- **Règle retenue :** chaque paramètre est testé sur plusieurs valeurs, et l'effet de chaque choix est noté dans la fiche indicateur.
- **Unité ou granularité :** selon le paramètre.
- **Exemple :** le seuil d'IFM qui définit un jour de danger élevé : 21,3 pour EFFIS ou 30 pour le guide de Copernicus EWDS (D008).
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Proxy

- **Définition :** mesure indirecte, utilisée quand ce qu'on veut mesurer n'est dans aucune colonne ou ne se mesure pas directement. Chaque proxy a ses propres biais, à documenter.
- **Sources et colonnes :** selon le proxy.
- **Divergences :** les décisions « approximer » du journal (D006 à D012) reposent souvent sur un proxy.
- **Règle retenue :** chaque proxy est signalé, avec ses biais, dans la fiche indicateur.
- **Unité ou granularité :** selon le proxy.
- **Exemple :** la population de chaque commune (Admin Express) pour approcher les enjeux menacés par un feu (D011).
- **Statut :** proposé.
- **Origine de la définition :** cours du 19/11/2026 (KPI, indicateurs et critères RACER).
- **Ajouté par :** Melvyn, 2026-11-19

## Saison des feux

- **Définition :** période de l'année où des feux de forêt se déclarent et où le danger est surveillé.
- **Sources et colonnes :** commande (« l'été », « le printemps et l'été prochains ») ; Météo des forêts (publiée du 3 juin à l'automne) ; BDIFF (date de première alerte).
- **Divergences :** la commande parle de « l'été », la Météo des forêts couvre de juin à l'automne, mais en Côte-d'Or des feux partent dès mars (32 feux sur 120 en mars-avril, BDIFF). La phrase de la commande « autant de feux de forêt que l'été 2026 » ne précise pas s'il s'agit du nombre de feux ou de la surface brûlée.
- **Règle retenue :** aucune pour l'instant ; l'hypothèse sur les feux de printemps est à tester (spec V1).
- **Unité ou granularité :** des mois.
- **Exemple :** feux de Côte-d'Or de mars à octobre (BDIFF, 2006-2025).
- **Statut :** proposé.
- **Origine de la définition :** commande ; PDF de la Météo des forêts ; fiche BDIFF.
- **Ajouté par :** Aissatou Diallo, Audrey, Jane, 2026-11-17

## SDIS

- **Définition :** service départemental d'incendie et de secours : les sapeurs-pompiers d'un département. Avec la BSPP (Paris et petite couronne) et le BMPM (Marseille), ils forment les services d'incendie et de secours (SIS).
- **Sources et colonnes :** Interventions SDIS (une ligne par service) ; Statistiques nationales des SDIS.
- **Divergences :** le territoire d'un SIS ne coïncide pas toujours avec un département (voir « Département »).
- **Règle retenue :** aucune.
- **Unité ou granularité :** un service d'incendie et de secours.
- **Exemple :** SDIS 21 (Côte-d'Or), notre commanditaire.
- **Statut :** validé.
- **Origine de la définition :** description du jeu « Interventions réalisées par les services d'incendie et de secours » (ministère de l'Intérieur, data.gouv.fr).
- **Ajouté par :** Aissatou Diallo, Melvyn, 2026-11-17

## Seuil actuel

- **Définition :** niveau de la Météo des forêts à partir duquel le SDIS 21 déclenche aujourd'hui le dispositif renforcé.
- **Sources et colonnes :** commande (« le seuil actuel ne nous convient pas »).
- **Divergences :** sa valeur n'est pas donnée dans la commande ; on ne sait pas s'il est le même partout dans le département.
- **Règle retenue :** à demander à la direction du SDIS 21.
- **Unité ou granularité :** un niveau de 1 à 4.
- **Exemple :** non disponible.
- **Statut :** à vérifier.
- **Origine de la définition :** commande.
- **Ajouté par :** Audrey, Jane, 2026-11-17

## Station météo

- **Définition :** poste de mesure de Météo-France, qui enregistre chaque jour la pluie, les températures, le vent et l'humidité.
- **Sources et colonnes :** Données climatologiques (`NUM_POSTE`, `RR`, `TX`, `TN`, `FFM`, `UN`) ; tables `dim_station` et `fait_meteo_jour`.
- **Divergences :** toutes les stations ne mesurent pas le vent et l'humidité ; la pluie du jour J est mesurée de J 6 h à J+1 6 h (UTC), et non de minuit à minuit.
- **Règle retenue :** le département est donné par les 2 premiers chiffres de `NUM_POSTE`, la commune est celle qui contient la station (par la carte) ; les valeurs sont déjà en °C, mm, m/s et % et ne doivent pas être divisées par 10.
- **Unité ou granularité :** une station ; un jour.
- **Exemple :** `21056001`, une station de Côte-d'Or.
- **Statut :** validé.
- **Origine de la définition :** documentation des Données climatologiques de Météo-France ; schéma v0.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Surface parcourue

- **Définition :** surface touchée par un feu, détaillée par type de végétation.
- **Sources et colonnes :** BDIFF (colonnes de surfaces parcourues, en m², et colonne de précision des surfaces).
- **Divergences :** en Côte-d'Or, 63 surfaces sur 120 sont estimées et 57 mesurées ; les définitions des surfaces ont changé en 2023 (fusion avec Prométhée), donc les feux de 2022 et avant ne sont pas strictement comparables à ceux de 2023 et après.
- **Règle retenue :** aucune pour l'instant ; à traiter dans le profil qualité de la BDIFF (ticket #42).
- **Unité ou granularité :** un feu ; m² (à convertir en hectares).
- **Exemple :** 439,6 ha parcourus en Côte-d'Or de 2006 à 2025 (BDIFF).
- **Statut :** validé.
- **Origine de la définition :** portail BDIFF (page « Définitions »).
- **Ajouté par :** Audrey, 2026-11-19

## Table de passage des communes fusionnées

- **Définition :** table qui relie chaque ancien code INSEE, disparu après une fusion de communes, au code de la commune actuelle.
- **Sources et colonnes :** Admin Express 2017 et édition la plus récente ; table `passage_commune` (`code_insee_ancien`, `code_insee_actuel`).
- **Divergences :** un feu enregistré avec un ancien code ne se relie pas à l'édition récente d'Admin Express (voir « Code INSEE de la commune »).
- **Règle retenue :** chaque commune de 2017 qui n'existe plus est rattachée à la commune actuelle qui contient un point de son ancien contour (D023) ; `fait_feu` garde le code d'origine (`code_insee_bdiff`) et le code actuel (`code_insee`).
- **Unité ou granularité :** un ancien code de commune.
- **Exemple :** 6 codes ont disparu en Côte-d'Or, dont `21213` ; aucun feu de Côte-d'Or n'en porte (vérifié sur 2006-2025), la table sert pour la région et la France.
- **Statut :** validé (D023).
- **Origine de la définition :** schéma v0 ; Code officiel géographique de l'INSEE.
- **Ajouté par :** Aissatou Diallo, 2026-11-23

## Territoire national

- **Définition :** l'ensemble du territoire français auquel la direction veut comparer la Côte-d'Or.
- **Sources et colonnes :** commande (« par rapport au reste du territoire national ») ; Météo des forêts (`num_dep`) ; BDIFF ; Interventions SDIS.
- **Divergences :** la Météo des forêts ne couvre que l'Hexagone et la Corse (96 départements) ; la BDIFF et les Interventions SDIS comprennent aussi l'outre-mer.
- **Règle retenue :** la France métropolitaine (96 départements, Corse comprise) ; l'outre-mer est écarté dès la couche silver (D022). Il faut écrire « France métropolitaine », et non « France », dans les indicateurs et le tableau de bord.
- **Unité ou granularité :** un département.
- **Exemple :** 2 632 feux en France sur les étés 2024 et 2025 (BDIFF).
- **Statut :** validé (D022).
- **Origine de la définition :** commande ; fiches des sources ; D022.
- **Ajouté par :** Jane, 2026-11-17 ; mis à jour par Aissatou Diallo, 2026-11-23

## Termes écartés

- **« Autant de feux que l'été 2026 »** (proposé par Jane, 2026-11-17) : écarté, car ce n'est pas un terme mais une phrase de la commande. Son ambiguïté (nombre de feux ou surface brûlée ?) est notée dans l'entrée « Saison des feux ».
