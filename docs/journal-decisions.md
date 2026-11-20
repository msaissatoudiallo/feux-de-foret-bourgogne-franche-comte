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

## D005 – Licence de la BDIFF : appliquer la règle la plus stricte

- **Date :** 2026-11-19
- **Source :** BDIFF
- **Constat :** divergence entre la Licence Ouverte 2.0 (data.gouv.fr) et les mentions légales du portail (« sans modification »)
- **Décision :** on applique la règle la plus stricte :
  1. le fichier BDIFF est conservé brut, jamais modifié (couche des données brutes) ;
  2. toutes les transformations (nettoyage, jointures, calculs) se font dans des tables dérivées, présentées comme « calculées à partir de la BDIFF » ;
  3. la source est citée partout où ses données sont utilisées ;
  4. le fichier BDIFF n'est pas publié dans le dépôt, qui est public (`data/raw/` est exclu de Git).
- **Raison :** cette option respecte les deux textes à la fois, alors que n'appliquer que la Licence Ouverte reviendrait à ignorer un texte du producteur. Elle correspond aussi à l'architecture en couches prévue, où la couche brute n'est jamais modifiée. On ne contacte pas le producteur pour savoir quel texte s'applique : l'option retenue respecte déjà les deux textes, et une réponse n'arriverait sans doute pas avant le 11/12.
- **Ce que la décision coûte :** presque rien, car c'est ce qu'on aurait fait de toute façon. Seule contrainte : le fichier BDIFF ne peut pas être partagé par le dépôt, chaque membre doit le télécharger lui-même sur le portail.
- **Auteurs :** Jane (responsable sources), avec le groupe
- **Ticket :** #51

---

> **Décisions D006 à D014 : issues de la matrice questions × sources** (`docs/sources/matrice.md`, exercice 3, partie B, PR #63). Chaque décision porte sur une question du groupe (G1 à G11) ou sur une source.

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

---

## D015 – Validation des pull requests par le responsable du domaine concerné

- **Date :** 2026-11-19
- **Contexte :** la professeure a précisé que chaque pull request est validée par le ou la responsable du domaine qu'elle touche. La décision 2 de D004 confiait toutes les validations à Melvyn.
- **Décision :** cette règle **remplace la décision 2 de D004** :
  - les pull requests sur les sources (fiches, inventaire, matrice) sont validées par **Jane** ;
  - celles sur le pipeline, le chargement et le schéma de l'entrepôt par **Audrey** ;
  - celles sur la qualité (profils, tests, données personnelles) par **Melvyn** ;
  - celles sur la gestion du projet (journal, README, spec, planning) par **Aissatou** ;
  - Melvyn valide en plus chaque nouvelle source et vérifie que les tests ont tourné ;
  - personne ne valide sa propre pull request : un autre membre la relit.
- **Raison :** suivre la consigne de la professeure, et faire relire chaque travail par la personne qui connaît le mieux son domaine.
- **Ce que la décision coûte :** chaque membre doit relire les pull requests de son domaine ; une pull request peut attendre si son responsable est absent.
- **Auteurs :** décision du groupe, sur consigne de la professeure.
- **Ticket :** #71

---

## D016 – Branches d'équipe `modelisation` et `qualite`

- **Date :** 2026-11-19
- **Contexte :** depuis D004, le groupe travaille en deux équipes : Modélisation (Audrey, Aissatou) et Qualité (Melvyn, Jane). Jusqu'ici, toutes les branches de tâches partent de `documentation`, ce qui convient aux documents. À partir du milestone V0, les équipes vont aussi écrire du code (chargement des données, profils qualité) et travailler en parallèle.
- **Décision :**
  - deux branches d'équipe sont créées depuis `dev` : `modelisation` (Audrey, Aissatou) et `qualite` (Melvyn, Jane), après la fusion de `documentation` dans `dev` et l'ajout de l'environnement Python (#38) ;
  - chaque branche de tâche part de la branche de son domaine et y revient par pull request :
    - documents de gestion et de sources (journal, README, glossaire, fiches, inventaire, matrice) → `documentation` ;
    - schéma de l'entrepôt et chargement de la BDIFF → `modelisation` ;
    - profils qualité et chargement de la Météo des forêts → `qualite` ;
  - dans la spec, la partie 6 (architecture) est modifiée par l'équipe Modélisation sur `modelisation`, la partie 7 (qualité) par l'équipe Qualité sur `qualite`, et le reste par la cheffe de projet sur `documentation` ;
  - chaque branche de domaine est fusionnée dans `dev` par pull request en fin de semaine, puis `dev` dans `main` aux checkpoints ;
  - la validation des pull requests reste celle de D015.
- **Raison :** les deux équipes avancent en même temps sans toucher au travail de l'autre. Chaque fichier, et chaque partie de la spec, n'a qu'un seul chemin vers `dev`, ce qui évite les conflits. L'environnement est ajouté à `dev` avant la création des branches, pour que les deux équipes travaillent avec le même.
- **Ce que la décision coûte :** plus de branches à suivre. Chaque branche d'équipe doit récupérer régulièrement les nouveautés de `dev`, et chaque équipe ouvre une pull request de plus par semaine.
- **Auteurs :** décision du groupe.
- **Ticket :** #76

---

## D017 – Validation des nouvelles sources rendue à Jane

- **Date :** 2026-11-19
- **Contexte :** la validation des nouvelles sources relève du domaine de Jane, responsable sources. Pendant la panne de son ordinateur, elle était assurée par Melvyn (D004, D015). Jane a maintenant un nouvel ordinateur.
- **Décision :** cette règle **remplace ce point de D015** :
  - Jane valide chaque nouvelle source ;
  - Melvyn vérifie que les tests ont tourné ;
  - le reste de D015 est inchangé.
- **Raison :** rendre à chaque membre la validation de son domaine, dès que la cause de la répartition provisoire a disparu.
- **Ce que la décision coûte :** Jane relit davantage de pull requests ; Melvyn n'est plus le deuxième regard sur les nouvelles sources.
- **Auteurs :** décision du groupe.
- **Ticket :** #86

---

## D018 – DuckDB pour l'entrepôt plutôt que PostgreSQL

- **Date :** 2026-11-20
- **Contexte :** l'environnement Python du projet (ticket #38, PR #99) doit fournir un outil pour l'entrepôt, c'est-à-dire les couches silver et gold. Les deux options envisagées étaient PostgreSQL (une base de données avec un serveur) et DuckDB (une base SQL dans un seul fichier, sans serveur).
- **Décision :** l'entrepôt est une base **DuckDB** :
  - les couches silver et gold sont des tables DuckDB, construites par les scripts de `src/` à partir des fichiers bruts de `data/raw/` (couche bronze) ;
  - le fichier de l'entrepôt (`*.duckdb`) est exclu de Git : chaque membre le reconstruit sur son ordinateur en relançant les scripts ;
  - la version est fixée dans `requirements.txt` (`duckdb==2.0.0`).
- **Raison :**
  - pas de serveur à installer ni de mot de passe à gérer sur les quatre ordinateurs ;
  - DuckDB lit directement les fichiers des sources, y compris les `.csv.gz` de la Météo des forêts ;
  - les données brutes et l'entrepôt restent hors du dépôt public, ce qui respecte la licence de la BDIFF (D005) ;
  - tout le monde obtient les mêmes tables à partir des mêmes scripts, ce qui oblige à rendre le pipeline reproductible.
- **Ce que la décision coûte :** il n'y a pas de base partagée entre les membres : chacun a sa propre copie de l'entrepôt et doit relancer les scripts après chaque changement ; DuckDB est fait pour l'analyse sur un seul ordinateur, pas pour plusieurs utilisateurs qui écrivent en même temps (ce dont le projet n'a pas besoin).
- **Auteurs :** proposée par Audrey (PR #99), décision du groupe.
- **Ticket :** #100

---

## D019 – Streamlit pour la dataviz du projet, dans un dossier dataviz/

- **Date :** 2026-11-20
- **Contexte :** le module de datavisualisation évalue le pipeline, la dataviz et la proposition au client. La dataviz évaluée doit être disponible sur GitHub : l'enseignant clone le dépôt à partir du 6/12 (kit projet HETIC). Aucun outil n'est imposé ; Power BI est l'outil des exercices en cours.
- **Décision :**
  - le dashboard du projet est développé avec **Streamlit** (Python), avec **Plotly** pour les graphiques ;
  - Power BI reste l'outil des exercices du cours : les captures Power BI du 20/11 viennent de ces exercices ;
  - tout ce qui concerne la dataviz est rangé dans un dossier **`dataviz/`** à la racine du dépôt (code du dashboard, captures, export), comme le conseille le kit ;
  - `streamlit` et `plotly` seront ajoutés à `requirements.txt` au démarrage de la dataviz.
- **Raison :** Streamlit lit directement l'entrepôt DuckDB (D018) ; tout est du code dans le dépôt, donc vérifiable en le clonant, alors qu'un fichier Power BI ne s'affiche pas sur GitHub ; il fonctionne sous Windows et Mac ; le pipeline est déjà en Python. Un dossier unique permet à l'enseignant de trouver la dataviz tout de suite.
- **Ce que la décision coûte :** Streamlit demande plus de temps de prise en main que Power BI, car chaque graphique est codé ; des captures doivent être ajoutées pour que la dataviz soit visible sans lancer le code.
- **Auteurs :** dossier `dataviz/` proposé par Audrey, décision du groupe.
- **Ticket :** #103

---

## D020 – Réduction des questions, des hypothèses et des sources

- **Date :** 2026-11-20
- **Contexte :** les 11 questions du groupe (G1 à G11) sont trop nombreuses pour un tableau de bord, qui doit répondre à 3 questions avec 5 à 7 indicateurs (kit projet HETIC). En cours, il a été conseillé de les réduire par une analyse SWOT.
- **Décision :** à partir de l'analyse SWOT de `docs/perimetre-retenu.md` :
  - les 11 questions sont réduites à **6 questions retenues** (R1 à R6) : G1 et G10 fusionnées, G2 et G3 fusionnées, G4, G6 et G8 fusionnées, G5, G7 et G11 gardées, **G9 écartée** faute de données (D010) ;
  - **H6 est intégrée à H2** (la région et la France deviennent la référence) ; **H7 devient secondaire** ; les autres hypothèses sont gardées ;
  - **6 sources retenues** : BDIFF, Copernicus EWDS, Météo des forêts, Admin Express, BD Forêt V2, Données climatologiques ; **SIM2 et les Statistiques nationales des SDIS sont écartées** ; les Interventions SDIS servent seulement au contrôle de la complétude de la BDIFF.
- **Raison :** garder les questions dont les données sont solides et qui éclairent directement les deux décisions de la commande (où concentrer les moyens, à quel seuil déclencher) ; un tableau de bord efficace répond à peu de questions.
- **Ce que la décision coûte :** les créneaux horaires (G3) et la taille des feux (G6) ne sont plus que des éléments secondaires ; la question du délai des secours (G9) est abandonnée.
- **Auteurs :** réduction proposée par Aissatou, validée par le groupe.
- **Ticket :** #104

---

## D021 – Périmètre de l'entrepôt : la France métropolitaine, sans l'outre-mer

- **Date :** 2026-11-20
- **Contexte :** l'export de la BDIFF couvre toute la France, outre-mer compris : départements `971`, `972`, `974` et `976`, avec des codes de 3 caractères. La Météo des forêts ne couvre que les 96 départements de métropole, et la spec fixe le code département à 2 caractères. Il fallait décider si l'outre-mer entre dans l'entrepôt (schéma v0, ticket #41).
- **Décision :**
  - l'outre-mer est écarté dès la couche silver : il reste dans les fichiers bruts (bronze), mais aucune table silver ou gold ne le contient ;
  - la « France » de référence des indicateurs (R3, H2) est la **France métropolitaine** (96 départements, Corse comprise) ;
  - le code département reste du texte de 2 caractères (`01`, `21`, `2A`), et une contrainte de la base le vérifie.
- **Raison :** la Météo des forêts, qui sert à vérifier la traduction de l'IFM en niveaux (D008), n'existe pas en outre-mer. Les climats tropicaux ne sont pas comparables à la Côte-d'Or. On garde ainsi une seule règle pour le code département.
- **Ce que la décision coûte :** les feux d'outre-mer ne sont pas comptés dans la comparaison avec la France. Il faut toujours écrire « France métropolitaine » dans les indicateurs et le dashboard, et non « France ».
- **Auteurs :** proposée par Audrey, validée par Audrey et Aissatou (équipe Modélisation).
- **Ticket :** #41

---

## D022 – La dimension des communes couvre toute la métropole

- **Date :** 2026-11-20
- **Contexte :** la table `dim_commune` décrit les communes (code INSEE, population, surface, forêt). La BDIFF contient des feux dans toute la France, mais la BD Forêt V2 n'a été téléchargée que pour la Côte-d'Or. Il fallait choisir entre la Côte-d'Or seule, la région ou toute la métropole.
- **Décision :**
  - `dim_commune` contient **toutes les communes de France métropolitaine**, dans l'édition la plus récente d'Admin Express ;
  - la surface de forêt (`surface_foret_km2`, `part_foret`) n'est remplie que pour la **Côte-d'Or**, et reste vide ailleurs ;
  - les codes de communes disparus après une fusion passent par la table `passage_commune`, construite en comparant Admin Express 2017 et l'édition récente.
- **Raison :** chaque feu de la BDIFF doit trouver sa commune, sinon la clé étrangère `code_insee` de `fait_feu` échoue pour la région et la France, alors que ces feux servent de référence (D007). Les questions sur la forêt (R1, H1, H8) ne portent que sur la Côte-d'Or.
- **Ce que la décision coûte :** il faut télécharger Admin Express pour toute la métropole (environ 35 000 communes), et pas seulement pour la Côte-d'Or. Un indicateur de forêt calculé hors de la Côte-d'Or serait faux : la colonne vide doit l'empêcher.
- **Auteurs :** proposée par Audrey, validée par Audrey et Aissatou (équipe Modélisation).
- **Ticket :** #41

---

## D023 – La couche silver garde le grain le plus fin de chaque source

- **Date :** 2026-11-20
- **Contexte :** la première proposition de la spec (partie 6) ramenait l'IFM et la météo à un département pour un jour dès la couche silver (`fait_danger_jour`, `fait_meteo_jour`). Mais les KPI dépendent de réglages à faire varier pour tester leur solidité : seuil d'IFM (21,3 ou 30), moyenne ou maximum des mailles, période (2006, 2015 ou 2020 à 2025).
- **Décision :**
  - en silver, chaque source garde son grain d'origine : **une maille pour un jour** pour l'IFM (`fait_ifm_jour`), **une station pour un jour** pour la météo (`fait_meteo_jour`), **un feu** pour la BDIFF (`fait_feu`) ;
  - les mailles et les stations sont rattachées aux départements et aux communes **par la carte, une seule fois**, dans les dimensions `dim_maille` et `dim_station` ;
  - les résumés par département et par jour, et les classes de danger, sont calculés en **gold** (`gold_departement_jour`, `gold_ete_departement`) ;
  - le décalage de la Météo des forêts (pour un feu du jour J, `niveau_j1` du bulletin de J-1, D008) est fait **une seule fois**, au chargement de `fait_mdf_jour`, et contrôlé par une contrainte de la base.
- **Raison :** on peut refaire chaque KPI avec d'autres réglages sans recharger les sources, et vérifier que la conclusion tient. On peut aussi retrouver la station la plus proche d'un feu (H5). Faire le décalage de la Météo des forêts une seule fois évite l'erreur la plus facile à faire sur la question du seuil.
- **Ce que la décision coûte :** le silver est plus volumineux (environ 5 millions de lignes pour l'IFM en métropole sur 2012-2025). Il faut une étape gold de plus avant le dashboard. C'est un écart avec la première proposition de la spec, qui a été mise à jour (partie 6).
- **Auteurs :** proposée par Audrey, validée par Audrey et Aissatou (équipe Modélisation).
- **Ticket :** #41