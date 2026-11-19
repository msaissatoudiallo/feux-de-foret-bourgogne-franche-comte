# Glossaire — Bourgogne-Franche-Comté

Dernière mise à jour : 2026-11-19

Version 0. Les termes viennent des termes inconnus des quatre analyses de la commande (`docs/analyse/`) et des termes rencontrés en ouvrant les sources (`docs/sources/`). Les entrées sont classées par ordre alphabétique. Un terme écarté est listé à la fin, avec la raison.

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

## Territoire national

- **Définition :** l'ensemble du territoire français auquel la direction veut comparer la Côte-d'Or.
- **Sources et colonnes :** commande (« par rapport au reste du territoire national ») ; Météo des forêts (`num_dep`) ; BDIFF ; Interventions SDIS.
- **Divergences :** la Météo des forêts ne couvre que l'Hexagone et la Corse (96 départements) ; la BDIFF et les Interventions SDIS comprennent aussi l'outre-mer.
- **Règle retenue :** proposition : la France métropolitaine (Hexagone et Corse), seule emprise commune aux sources de l'indice. À consigner dans le journal.
- **Unité ou granularité :** un département.
- **Exemple :** 2 632 feux en France sur les étés 2024 et 2025 (BDIFF).
- **Statut :** proposé.
- **Origine de la définition :** commande ; fiches des sources.
- **Ajouté par :** Jane, 2026-11-17

## Termes écartés

- **« Autant de feux que l'été 2026 »** (proposé par Jane, 2026-11-17) : écarté, car ce n'est pas un terme mais une phrase de la commande. Son ambiguïté (nombre de feux ou surface brûlée ?) est notée dans l'entrée « Saison des feux ».
