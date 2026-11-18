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
