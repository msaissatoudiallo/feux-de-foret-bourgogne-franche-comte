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
| Cheffe de projet | Aissatou Diallo | Dépôt, tickets, checkpoints, journal des décisions |
| Responsable sources | Jane | Inventaire, fiches d'identité, matrice questions × sources |
| Responsable qualité et conformité | Melvyn | Règles de qualité, tests, données personnelles |
| Responsable pipeline et modèle | Audrey | Chargement, consolidation, entrepôt |

Un rôle confie la responsabilité d'un domaine : la personne relit ce qui le touche et valide les tickets qui en relèvent. Tout changement de rôle est consigné dans le [journal des décisions](docs/journal-decisions.md).

## Organisation du dépôt

```
docs/
├── analyse/                 # Analyses individuelles de la commande (commande-prenom-nom.md)
├── glossaire.md             # Glossaire du projet (à venir)
└── journal-decisions.md     # Journal des décisions du groupe
```

## Règles de travail

- Une branche par ticket, nommée `type/courte-description` (ex. `docs/analyse-commande-jane`).
- Des commits atomiques : un commit = un changement cohérent, avec un message clair.
- Tout passe par une pull request vers `main`, relue par le ou la responsable du domaine concerné.
