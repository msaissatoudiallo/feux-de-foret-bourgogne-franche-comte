# Journal des décisions

Chaque décision du groupe est consignée ici : date, contexte, décision, personnes concernées.

---

## D001 – Création du dépôt par la responsable pipeline et modèle

- **Date :** 2026-11-16
- **Contexte :** le sujet prévoit que la cheffe de projet (Audrey) crée le dépôt. Elle était absente lors de la séance de création.
- **Décision :** Aissatou (responsable pipeline et modèle) crée et initialise le dépôt à sa place, puis ajoute les membres comme collaborateurs. Audrey reçoit les droits nécessaires pour reprendre la gestion du dépôt (tickets, checkpoints, journal) dès son retour.
- **Rôles :** inchangés. Il s'agit d'une suppléance ponctuelle, pas d'un changement de rôle.
- **Validée par :** à valider par Audrey à son retour.
- **Mise à jour (2026-11-17) :** décision remplacée par D002. Aissatou devient cheffe de projet et garde la gestion du dépôt.

---

## D002 – Échange des rôles entre Aissatou et Audrey

- **Date :** 2026-11-17
- **Contexte :** Aissatou a créé et initialisé le dépôt (D001) à la place d'Audrey, alors cheffe de projet.
- **Décision :** Aissatou et Audrey échangent leurs rôles :
  - Aissatou Diallo : responsable pipeline et modèle → **cheffe de projet** ;
  - Audrey : cheffe de projet → **responsable pipeline et modèle**.
- **Raison :** Aissatou ayant créé le dépôt, il est plus simple qu'elle en garde la gestion (tickets, checkpoints, journal des décisions).
- **Rôles inchangés :** Jane (responsable sources) et Melvyn (responsable qualité et conformité).
- **Ticket :** #3
- **Validée par :** le groupe.

---

## D003 – Organisation des pull requests

- **Date :** 2026-11-17
- **Contexte :** chaque membre travaille sur ses propres branches (analyse de la commande, fiches d'identité des sources). Ouvrir et fusionner les pull requests au fil de l'eau risquait de créer des conflits entre les branches.
- **Décision :** les pull requests vers `documentation` sont ouvertes **une fois toutes les fiches d'identité des sources terminées**.
- **Relecture :** les pull requests sont relues par Aissatou Diallo, cheffe de projet.
- **Exceptions :** la pull request de Jane (#2), ouverte avant cette décision, reste ouverte et sera traitée avec les autres. La pull request d'Audrey (#14, analyse de la commande) a été fusionnée dans `documentation` avant que la décision ne soit partagée.
- **Ordre de fusion dans `documentation` :**
  1. **Analyses de la commande** : #2 (Jane), #12 (Melvyn), puis l'analyse d'Aissatou (ticket #1).
  2. **Organisation** : changement de rôles (ticket #3), **puis** cette décision D003 (ticket #7), car les deux modifient ce journal. La correction des règles du README (ticket #17) peut passer à n'importe quel moment de cette étape.
  3. **Fiches d'identité** : #15 (Jane, Météo des forêts et EFFIS) **avant** les fiches d'Aissatou (tickets #4 et #6), qui contiennent un commit de la branche de Jane. Les fiches de Melvyn (#13) et d'Audrey (#16) peuvent passer à n'importe quel moment de cette étape.
- **Ensuite :** `documentation` → `dev` en fin de semaine, puis `dev` → `main` au checkpoint.
- **Ticket :** #7
- **Validée par :** le groupe.

---

## D004 – Organisation en deux équipes et validation des pull requests

- **Date :** 2026-11-18
- **Contexte :** la professeure recommande de diviser le groupe en deux équipes qui travaillent en parallèle, et précise les rôles : la cheffe de projet définit les milestones et attribue les tickets ; le responsable qualité et conformité valide les nouvelles sources, vérifie les tests et valide les pull requests.
- **Décision 1 – Deux équipes :**
  - **Équipe 1 – Schéma et architecture** (tables, clés primaires et étrangères, couches bronze / silver / gold) : Audrey et Aissatou. Ticket parent #35.
  - **Équipe 2 – Qualité des données** (complétude, exactitude, cohérence, validité, unicité, actualité) : Melvyn et Jane. Ticket parent #36.
  - Les tâches communes (inventaire, matrice, glossaire, spec, journal) sont regroupées dans le ticket parent #37.
- **Décision 2 – Validation des pull requests :** les pull requests sont relues et validées par **Melvyn**, responsable qualité et conformité. Cette décision **remplace la règle de relecture de D003** (« relues par la cheffe de projet »). Une pull request de Melvyn est validée par un autre membre du groupe.
- **Décision 3 – Milestones :** le travail est découpé en trois versions : **V0 – Socle** (20/11/2026), **V1 – Version enrichie** (02/12/2026), **V2 – Version finale** (11/12/2026). Chaque ticket est rattaché à un milestone et suivi dans le tableau du projet GitHub (colonnes Backlog, In progress, In review, Done).
- **Décision 4 – Inventaire et matrice :** l'ordinateur de Jane, responsable sources, étant en panne le 18/11 :
  - la mise à jour de l'inventaire (#45) est assignée à Aissatou ;
  - la matrice du groupe (#46) est une tâche de groupe, assignée aux quatre membres : Aissatou la rédige et la coordonne, les autres membres complètent et relisent.
- **Raison :** travailler en parallèle pour tenir les livrables de fin de semaine (spec V1, journal, couche brute), et suivre les rôles définis par la professeure.
- **Ce que la décision coûte :** Aissatou coordonne plus de tâches communes cette semaine ; la relecture repose en grande partie sur une seule personne (Melvyn).
- **Ticket :** #50
- **Validée par :** le groupe.

---

> **Décisions D006 à D014 : issues de la matrice questions × sources** (`docs/sources/matrice.md`, exercice 3, partie B, PR #63). Chaque décision porte sur une question du groupe (G1 à G11) ou sur une source. Le numéro D005 est réservé à la décision sur la licence de la BDIFF (ticket #51).

## D006 – G1 : localiser les feux à la commune

- **Date :** 2026-11-19
- **Question :** G1 – Où se concentrent les départs de feu et les surfaces brûlées en Côte-d'Or ?
- **Manque :** la localisation précise des feux. La BDIFF s'arrête à la commune (pas de coordonnées) et aucune source ne donne de massifs forestiers.
- **Décision :** **approximer**. La zone d'étude est la commune ; le nombre de feux de chaque commune est rapporté à sa surface de forêt (BD Forêt V2 croisée avec les contours des communes d'Admin Express).
- **Raison :** c'est le grain le plus fin disponible dans la BDIFF, et Admin Express permet de relier les deux sources.
- **Ce que la décision coûte :** une grande commune peut regrouper des feux éloignés ; la forêt est dans son état de 2017 ; avec 120 feux, beaucoup de communes n'en ont qu'un seul.
- **Auteurs :** Jane (Q1), Audrey (Q3), décision du groupe.
- **Ticket :** #52

## D007 – G3 : élargir l'étude des heures et des jours à la région

- **Date :** 2026-11-19
- **Question :** G3 – À quelles heures et quels jours de la semaine partent les feux ?
- **Manque :** assez de feux (120 en Côte-d'Or) pour les répartir par heure et par jour, et l'été 2026, absent de la BDIFF.
- **Décision :** **approximer**. Étudier les heures et les jours sur les feux de Bourgogne-Franche-Comté (752 feux de 2006 à 2025), en plus de la Côte-d'Or.
- **Raison :** la région a six fois plus de feux, avec la même colonne d'heure de première alerte.
- **Ce que la décision coûte :** le résultat ne sera pas propre à la Côte-d'Or, et l'été 2026 reste absent.
- **Auteurs :** Melvyn (Q1), décision du groupe.
- **Ticket :** #52

## D008 – G4, G6, G7, G8 : utiliser l'IFM de Copernicus EWDS à la place du niveau de la Météo des forêts

- **Date :** 2026-11-19
- **Questions :** G4 (part des jours avec feu par niveau), G6 (taille des feux selon le niveau), G7 (feux par indice bas), G8 (Côte-d'Or, région et France).
- **Manque :** un indice sur une longue période. La Météo des forêts n'existe que depuis juin 2024, l'été seulement : 2 feux en Côte-d'Or sur la période commune avec la BDIFF.
- **Décision :** **approximer**. Utiliser l'Indice Forêt Météo (IFM) de Copernicus EWDS pour chaque jour de 2012 à 2025, ramené au département (ou à la commune) avec Admin Express, puis le traduire en classes de danger :
  - **première traduction : les classes de danger de la page EFFIS en vigueur** (« Fire danger forecast », https://forest-fire.emergency.copernicus.eu/about-effis/technical-background/fire-danger-forecast, consultée le 19/11/2026), identiques pour tous les pays : faible < 11,2 ; modéré 11,2 à 21,3 ; **élevé 21,3 à 38,0** ; très élevé 38,0 à 50,0 ; extrême 50,0 à 70,0 ; très extrême > 70,0 (classe introduite en juin 2021, d'après la même page) ;
  - **autres versions, signalées par la relecture de Melvyn :** les publications plus anciennes d'EFFIS (documentation ECMWF, article de Camia et Amatulli, 2010) découpent la classe « faible » en « très faible < 5,2 » et « faible 5,2 à 11,2 », et n'ont pas la classe « très extrême ». Le guide utilisateur de Copernicus EWDS donne seulement une règle générale : un IFM supérieur à 30 indique un danger élevé. **Le seuil « élevé » (21,3), le seul utilisé pour nos questions, est le même dans toutes les versions d'EFFIS** ; l'écart avec le seuil de 30 du guide sera à tester lors de la vérification ci-dessous ;
  - **vérification** : comparer ces classes aux niveaux de la Météo des forêts en Côte-d'Or sur 2024-2026, et les ajuster si l'écart est important. Pour un jour J, le niveau de la Météo des forêts à comparer est la colonne `niveau_j1` du bulletin publié la veille (J-1), puisque `niveau_j1` donne le niveau du lendemain (PDF de présentation de la Météo des forêts, Météo-France).
- **Raison :** l'IFM est la base de l'indice utilisé par Météo-France ; Copernicus EWDS le donne toute l'année depuis 1940, pour chacun des 120 feux de Côte-d'Or. Il n'existe pas de table publique de passage de l'IFM aux niveaux de la Météo des forêts : d'après le PDF de présentation de Météo-France, ces niveaux sont calculés à partir d'un « Indice de danger intégré » (IFM complété par l'état de sécheresse de la végétation), de la surface de forêts et des interfaces forêt-habitat du département, des zones sensibles aux feux (climatologie sur 30 ans) et de l'analyse des prévisionnistes.
- **Ce que la décision coûte :** ce n'est pas le niveau officiel utilisé par la direction ; les classes EFFIS sont européennes (6 classes, non adaptées à la France) et la traduction vers les 4 niveaux de la Météo des forêts restera approximative ; il faut un traitement géographique (mailles d'environ 19 × 28 km) et un format technique (NetCDF).
- **Auteurs :** Audrey (Q1, Q4), Jane (Q2, Q3, Q4), Aissatou (Q1, Q3, Q4), décision du groupe.
- **Ticket :** #52

## D009 – G5 : demander le coût du dispositif renforcé au SDIS 21

- **Date :** 2026-11-19
- **Question :** G5 – Pour chaque seuil possible, combien de jours de dispositif renforcé par saison, et quelle part des feux couverts ?
- **Manque :** le coût d'une journée de dispositif renforcé et le budget 2027 : ce sont des données internes du SDIS 21.
- **Décision :** **collecter** : les demander à la direction du SDIS 21, notre commanditaire. Sans réponse, exprimer le coût en **nombre de jours** de dispositif, et non en euros.
- **Raison :** aucune source ouverte ne contient ces données.
- **Ce que la décision coûte :** dépend du délai de réponse du SDIS 21 ; sans réponse, la recommandation ne pourra pas être chiffrée en euros.
- **Auteurs :** Audrey (Q2), Jane (Q2), décision du groupe.
- **Ticket :** #52

## D010 – G9 : demander l'heure d'arrivée des secours au SDIS 21, sinon renoncer

- **Date :** 2026-11-19
- **Question :** G9 – Les feux qui deviennent gros sont-ils ceux où les secours arrivent le plus tard ?
- **Manque :** l'heure d'arrivée des secours sur chaque feu : aucune source ouverte ne la contient.
- **Décision :** **collecter** auprès du SDIS 21. Sans réponse avant le milestone V1 (02/12/2026), **renoncer** à la question.
- **Raison :** c'est une donnée interne du SDIS ; la question n'est pas centrale pour les deux décisions de la commande.
- **Ce que la décision coûte :** la question risque d'être abandonnée ; elle dépend d'une réponse extérieure.
- **Auteurs :** Melvyn (Q2), décision du groupe.
- **Ticket :** #52

## D011 – G10 : approcher les enjeux par la population des communes

- **Date :** 2026-11-19
- **Question :** G10 – Où un feu ferait-il le plus de dégâts (forêts proches des habitations, des routes) ?
- **Manque :** la localisation des habitations et des routes. La BD TOPO, qui les contient, n'a pas été explorée.
- **Décision :** **approximer** pour le milestone V0 : utiliser la population de chaque commune (colonne `population` d'Admin Express) et la surface de forêt (BD Forêt V2). L'exploration de la BD TOPO est reportée au milestone V1, s'il reste du temps.
- **Raison :** la BD TOPO est une source lourde, à croiser par la carte ; le temps est limité avant le 11/12.
- **Ce que la décision coûte :** la population d'une commune ne dit pas si les habitations sont proches de la forêt ; les routes ne sont pas prises en compte.
- **Auteurs :** Melvyn (Q3), décision du groupe.
- **Ticket :** #52

## D012 – G11 : utiliser Copernicus EWDS pour suivre les jours de danger d'un été à l'autre

- **Date :** 2026-11-19
- **Question :** G11 – Le nombre de jours de danger élevé augmente-t-il d'un été à l'autre ?
- **Manque :** aucun : Copernicus EWDS est « complet » pour cette question (IFM chaque jour de 1940 à 2026, colonne `fwinx`).
- **Décision :** **collecter** les données de Copernicus EWDS. Cette décision **remplace** celle de la section 5 de Melvyn (« approximer avec SIM2 »), prise avant l'ajout de Copernicus EWDS.
- **Raison :** Copernicus EWDS donne directement l'indice, alors que SIM2 ne donne que la météo (donnée indirecte).
- **Ce que la décision coûte :** il faut fixer la valeur d'IFM qui correspond à un « danger élevé » (voir D008) ; compte gratuit et format NetCDF nécessaires.
- **Auteurs :** Melvyn (Q4), décision du groupe.
- **Ticket :** #52

## D013 – EFFIS écartée pour l'indice

- **Date :** 2026-11-19
- **Source :** EFFIS.
- **Constat :** EFFIS donne le même indice (FWI) que Copernicus EWDS, mais seulement sous forme d'images, sans département. Ses zones brûlées n'ont pas été vérifiées.
- **Décision :** **écarter** EFFIS pour l'indice, au profit de Copernicus EWDS. Ses zones brûlées ne seront vérifiées que si elles deviennent nécessaires.
- **Raison :** Copernicus EWDS donne les mêmes valeurs sous une forme exploitable (fiche Copernicus EWDS, « Ce que j'ai découvert »).
- **Ce que la décision coûte :** rien pour l'indice ; l'éventuel apport des zones brûlées reste inconnu.
- **Auteurs :** décision du groupe.
- **Ticket :** #52

## D014 – Sources ajoutées après les sections 5 individuelles

- **Date :** 2026-11-19
- **Constat :** trois sources (Données climatologiques quotidiennes, Copernicus EWDS, Admin Express) ont été ajoutées à l'inventaire après que certains membres ont écrit leur section 5 : les sections 5 n'ont donc pas toutes le même nombre de sources (7 ou 8).
- **Décision :** les sections 5 individuelles ne sont **pas modifiées**. Les nouvelles sources sont prises en compte **seulement dans la matrice du groupe**, où leurs degrés sont établis à partir de leurs fiches.
- **Raison :** les sections 5 gardent la trace de ce que chacun savait au moment de l'écrire, comme le demande l'exercice 3 (« l'écart entre vos prédictions et la réalité »).
- **Ce que la décision coûte :** les sections 5 et la matrice ne comptent pas le même nombre de sources ; c'est expliqué dans la matrice.
- **Auteurs :** décision du groupe.
- **Ticket :** #52
