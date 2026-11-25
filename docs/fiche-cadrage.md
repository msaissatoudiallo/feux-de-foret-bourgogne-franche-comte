# Fiche de cadrage du tableau de bord

- **Groupe :** groupe 2 (Aissatou, Audrey, Jane, Melvyn)
- **Rédigée par :** Jane, le 2026-11-20, avec la relecture qualité de Melvyn
- **Statut :** brouillon, à valider par le groupe puis par le formateur
- **Ticket :** #105

Cette fiche suit le modèle « Fiche de cadrage du tableau de bord » du kit HETIC (séance 1). Elle part du périmètre retenu par le groupe (`docs/perimetre-retenu.md`, D020) et corrige la liste des KPI (point 8 du point d'étape du 20/11).

## La fiche

| Rubrique | Contenu |
|---|---|
| **Le décideur** | La direction du SDIS 21 (Service départemental d'incendie et de secours de la Côte-d'Or). |
| **La décision** | Avant l'été 2027 : **où concentrer les moyens** contre les départs de feu (communes, période de l'année), et **à partir de quel niveau d'indice déclencher le dispositif renforcé** (patrouilles, guet), pour un nombre de jours compatible avec le budget. Rendu au SDIS : 11/12/2026. |
| **Question 1 · Où en est-on ?** | Combien de feux en Côte-d'Or, à quelle période de l'année, et le danger augmente-t-il d'un été à l'autre ? (R2, R6) |
| **Question 2 · Pourquoi ?** | Où partent les feux, et l'indice de danger les annonce-t-il bien, en Côte-d'Or comparée à la région et à la France ? Pourquoi des feux partent-ils quand l'indice est bas ? (R1, R3, R4) |
| **Question 3 · Que fait-on ?** | Quel seuil retenir, pour combien de jours de dispositif par saison, et quelles communes surveiller en priorité ? (R5, R1) |
| **5 à 7 indicateurs** | 7 indicateurs, détaillés dans le tableau ci-dessous. |
| **Sources** | BDIFF, Copernicus EWDS, Météo des forêts, Admin Express, BD Forêt V2, Données climatologiques (détail ci-dessous). |
| **Validation formateur** | Date : ............ Visa : ............ |

## Les 7 indicateurs

Chaque indicateur est comparé à une référence et affiché **avec le nombre de feux sur lequel il est calculé**, car les petits nombres (120 feux en Côte-d'Or) rendent une part fragile.

| # | Question du tableau de bord | Indicateur | Question retenue, hypothèse | Référence | Territoire |
|---|---|---|---|---|---|
| 1 | Où en est-on ? | **Part des feux hors juin-septembre** | R2, H4 | Seuil de 25 % (objectif SMART de H4) | Côte-d'Or |
| 2 | Où en est-on ? | **Jours de danger élevé du dernier été** (IFM ≥ 21,3, D008) | R6, H9 | Moyenne des 30 étés 1997-2026 ; tendance en jours gagnés ou perdus par été | Côte-d'Or |
| 3 | Pourquoi ? | **Taux de jours avec au moins un feu, par classe d'indice** | R3, H2 (H6 intégrée) | Le même taux pour la région et pour la France (IFM téléchargé sur la France, #114) | Côte-d'Or, région, France |
| 4 | Pourquoi ? | **Part des feux partis par indice bas** (IFM < 11,2, classe « faible » d'EFFIS, D008) | R4, H5 | Part des jours à indice bas sur la même période | Côte-d'Or et région |
| 5 | Pourquoi ? | **Feux par 100 km² de forêt**, par commune. Calculé seulement pour les communes qui ont au moins 1 km² de forêt (paramètre à tester : 1 ou 5 km²) ; les autres sont regroupées en une seule ligne « petites surfaces de forêt ». Sinon, une commune avec 0,5 km² de forêt et un seul feu atteindrait 200 feux pour 100 km² | R1, H1 | Moyenne de la Côte-d'Or | Côte-d'Or |
| 6 | Que fait-on ? | **Pour chaque seuil d'indice : part des jours de feu couverts et jours de dispositif par saison**. Un jour de feu est un jour avec au moins un feu (un jour avec 3 feux compte pour 1) ; il est couvert si l'indice atteint le seuil ce jour-là | R5, H2 et H3 | Objectif SMART : au moins 70 % des jours de feu couverts, moins de 30 jours de dispositif par saison (valeurs à ajuster, D009) | Couverture : région ; jours de dispositif : Côte-d'Or |
| 7 | Que fait-on ? | **Part des communes à fort enjeu** (à la fois très boisées et habitées) | R1, H8 | 25 % attendus si forêt et population n'avaient aucun lien | Côte-d'Or (698 communes) |

### Ce qui change par rapport à la spec

- **H1** : l'ancien KPI « part des feux dans les 10 % de communes les plus touchées » est abandonné. Les 120 feux de Côte-d'Or sont dans 85 communes sur 698 : les 70 communes les plus touchées regroupent forcément 105 feux, soit 87,5 %, et l'hypothèse serait confirmée quoi qu'il arrive. Il est remplacé par les **feux par 100 km² de forêt** (indicateur 5).
- **H3** : le taux de fausses alertes serait proche de 100 % en Côte-d'Or, faute de feux. Il est remplacé par le couple **part des jours de feu couverts / jours de dispositif** (indicateur 6), avec la couverture calculée sur la région (D007).
- **H5** : l'« indice bas » est défini (IFM < 11,2) et comparé à la part des jours à indice bas (indicateur 4).
- **H7** (week-end et jours fériés) sort de la liste principale : hypothèse secondaire depuis D020. Sa fiche reste une analyse complémentaire.
- **Lisibilité** : le tableau de bord montre une valeur simple et sa référence. Les tests statistiques des fiches indicateur (test binomial, test de Fisher, Mann-Kendall) restent dans l'analyse.

### Règle commune de période (D021)

- **2015-2025** pour les indicateurs qui comptent des feux (1, 3, 4, 5, 6) : les feux d'avant 2015 sont mal saisis hors de l'aire méditerranéenne (fiche BDIFF). La prudence demandée par le producteur avant 2020 est rappelée dans les limites.
- **1997-2026** pour l'indicateur qui n'utilise que l'indice (2) : 30 étés, la durée d'une normale climatique.
- **Indicateur 7** : pas de période de feux ; forêt dans son état de 2017 (BD Forêt V2), population de l'édition récente d'Admin Express.

La spec est alignée sur cette règle : les objectifs SMART de H4 et de H2-H3 portent maintenant sur 2015-2025 (PR #138 et #145).

## Sources

| Source | Fichier | Période utilisée | Territoire | Indicateurs |
|---|---|---|---|---|
| BDIFF | Export CSV du portail (`Incendies.csv`, « Type de feu : F ») | 2015-2025 | Côte-d'Or, Bourgogne-Franche-Comté, France | 1, 3, 4, 5, 6 |
| Copernicus EWDS | `cems-fire-historical-v1`, variable *Fire weather index* | 1997-2026, étés seulement (indicateur 2) ; 2015-2025, **toute l'année** pour tenir compte des feux de printemps (3, 4, 6) (ticket #114) | Côte-d'Or et région ; France métropolitaine sur 2015-2025 (#114) | 2, 3, 4, 6 |
| Météo des forêts | `mdf.2024`, `mdf.2025`, `mdf.2026` | 2024-2026 | Côte-d'Or | Contrôle de la traduction de l'IFM en niveaux (D008) |
| Admin Express | Communes, édition la plus récente ; contours des départements ; édition 2017 des communes (table de passage des communes fusionnées), comme prévu dans le ticket #116 | Édition récente ; édition 2017 | Côte-d'Or (communes) ; région et France (départements) | 3, 4, 5, 6, 7 |
| BD Forêt V2 | Côte-d'Or | État 2017 | Côte-d'Or | 5, 7 |
| Données climatologiques | Données quotidiennes Météo-France | 2015-2025 | Côte-d'Or | Complément de l'indicateur 4 (temps chaud et sec des jours de feu, H5) |

Les données de la BDIFF ne sont pas publiées dans le dépôt (D005).

## Les pages du tableau de bord

Le kit demande trois niveaux : Synthèse, Pourquoi, Détail.

| Page | Contenu |
|---|---|
| Synthèse | Question 1 et question 3 : indicateurs 1, 2, 6 et 7, chacun avec sa référence |
| Pourquoi | Question 2 : indicateurs 3, 4 et 5 |
| Détail | La liste des feux et des communes, à laquelle on accède depuis les deux autres pages |

## Suite

1. Valider cette liste avec le groupe, puis avec le formateur. **Validée par le groupe (PR #123) ; validation du formateur en attente.**
2. Consigner la liste et la règle de période dans le journal (D021). **Fait (PR #138).**
3. Ouvrir un ticket par fiche indicateur manquante (indicateurs 1, 3, 4, 5 et 6), au format du kit (#106). Les indicateurs 2 (H9) et 7 (H8) ont déjà une fiche, à mettre au format du kit. **Fait : les 7 fiches sont dans `docs/indicateurs/`** (indicateur 1 : `fiche-kpi-h4.md` ; 2 : `fiche-kpi-g11.md` ; 3 : `fiche-kpi-h2.md` ; 4 : `fiche-kpi-h5.md` ; 5 : `fiche-kpi-h1.md` ; 6 : `fiche-kpi-h3.md` ; 7 : `fiche-kpi-g10.md`).
