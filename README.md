# Feux de forêt – Bourgogne-Franche-Comté

Projet de modélisation et pipeline de données (UE01 – Stratégie business data-driven, Hetic 2026/2027).

**Commanditaire :** Direction du SDIS 21 (Côte-d'Or) – Saison feux 2027
**Région :** Bourgogne-Franche-Comté
**Rendu final :** 11 décembre 2026

## La commande

La direction du SDIS 21 veut arbitrer deux points pour l'été 2027 :

1. **Où concentrer les moyens** (humains et financiers) pour lutter au mieux contre les départs de feu ?
2. **À partir de quel niveau de la Météo des forêts** déclencher le dispositif renforcé (patrouilles, guet, etc.) ?

Elle souhaite comprendre le comportement de l'indice en Côte-d'Or, dans les autres départements de la région, et situer le département par rapport au reste du territoire national.

## L'équipe

| Rôle | Membre | Responsable de |
|---|---|---|
| Cheffe de projet | Aissatou Diallo | Dépôt, milestones, attribution et suivi des tickets, checkpoints, journal des décisions, validation du glossaire |
| Responsable sources | Jane | Inventaire, fiches d'identité, matrice questions × sources, validation des nouvelles sources |
| Responsable qualité et conformité | Melvyn | Règles de qualité, tests, données personnelles |
| Responsable pipeline et modèle | Audrey | Chargement, consolidation, entrepôt |

Un rôle confie la responsabilité d'un domaine : la personne relit ce qui le touche et valide les tickets et les pull requests qui en relèvent. Tout changement de rôle est consigné dans le [journal des décisions](docs/journal-decisions.md).

Le groupe travaille en deux équipes (D004) : **Modélisation** (Audrey, Aissatou) et **Qualité** (Melvyn, Jane), chacune avec sa branche (D016).

## Organisation du dépôt

```
docs/
├── analyse/                 # Analyses individuelles de la commande (commande-prenom-nom.md)
├── indicateurs/             # Fiches indicateur, une par KPI (fiche-kpi-*.md)
├── sources/                 # Fiches d'identité des sources (fiche-*.md), inventaire.md, matrice.md
├── cadrage_technique.md     # Rendu du cadrage technique : sources prévues, outils, risques (20/11)
├── glossaire.md             # Glossaire du projet
├── journal-decisions.md     # Journal des décisions du groupe
└── spec.md                  # Spécification du projet (point d'entrée pour comprendre le projet)
```

Pour comprendre le projet, commencer par la [spécification](docs/spec.md).

## Règles de travail

- Une branche par ticket, nommée `type/courte-description` (ex. `docs/analyse-commande-jane`, `feat/chargement-bdiff`).
- Des commits atomiques : un commit = un changement cohérent, avec un message clair.
- Personne ne travaille directement sur `main`, `dev`, `documentation`, `modelisation` ou `qualite`. Chaque branche de tâche part de la branche de son domaine (voir D016) :
  - `documentation` pour les documents (journal, README, glossaire, fiches de sources, fiches indicateur, inventaire, matrice, et la spec sauf ses parties 6 et 7) ;
  - `modelisation` pour le schéma de l'entrepôt, le chargement de la BDIFF et la partie 6 de la spec (équipe Modélisation) ;
  - `qualite` pour les profils qualité, le chargement de la Météo des forêts et la partie 7 de la spec (équipe Qualité).
- Le travail remonte par pull requests : branche de tâche → branche de domaine → `dev` (en fin de semaine) → `main` (aux checkpoints).
- Pour récupérer le travail arrivé dans `dev`, une branche d'équipe est mise à jour par une pull request `dev` → branche d'équipe (base : `modelisation` ou `qualite`, compare : `dev`). Chaque membre part ensuite de sa branche d'équipe à jour ; une branche de tâche en cours récupère la mise à jour avec `git pull origin <branche d'équipe>`.
- Les parties techniques du README (environnement, chargement des données) et `requirements.txt` sont modifiées avec le code, sur la branche d'équipe. Pour éviter les conflits entre équipes : une bibliothèque par ligne, ajoutée dans sa rubrique de `requirements.txt`, et chaque équipe écrit dans sa propre partie du README.
- Chaque pull request est relue et validée par le ou la **responsable du domaine concerné** : Jane pour les sources, Audrey pour le pipeline et le modèle, Melvyn pour la qualité, Aissatou pour la gestion du projet (journal, README, spec). Jane valide en plus chaque nouvelle source, et Melvyn vérifie que les tests ont tourné. Personne ne valide sa propre pull request (voir D015 et D017 dans le [journal des décisions](docs/journal-decisions.md)).
- Chaque tâche a un ticket, rattaché à un ticket parent et à un milestone (V0, V1, V2), et suivi dans le tableau du projet GitHub (Backlog, In progress, In review, Done).
- Après la fusion d'une pull request vers `documentation`, `modelisation` ou `qualite`, le ticket est fermé à la main (GitHub ne le fait que pour la branche par défaut, `dev`).
