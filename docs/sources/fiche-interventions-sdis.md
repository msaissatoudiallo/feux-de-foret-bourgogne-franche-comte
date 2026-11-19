# Fiche d'identité – Interventions réalisées par les services d'incendie et de secours

- **Explorée par :** Aissatou Diallo
- **Date d'exploration :** 2026-11-17
- **Page de la source :** https://www.data.gouv.fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours
- **Nom dans la liste du défi :** « Interventions SDIS » (groupe « Historique de feux »)
- **Fichiers ouverts :** `interventions2024.csv`, `interventions2013` (fichier `interventions.csv`), `interventions2008.csv`

## Fiche

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Intérieur. Les données sont collectées chaque année par la Direction générale de la sécurité civile et de la gestion des crises (DGSCGC) auprès des services d'incendie et de secours : les SDIS, la Brigade de sapeurs-pompiers de Paris (BSPP) et le Bataillon de marins-pompiers de Marseille (BMPM). Le système informatique utilisé pour la collecte : non vérifié (non indiqué sur la fiche). |
| Mode d'accès et format | Téléchargement direct sur data.gouv.fr. Un fichier CSV par année (17 fichiers). Séparateur `;`, encodage ISO-8859-1 (Latin-1). |
| Grain (une ligne = ?) | **Un service d'incendie et de secours (un département) sur une année.** Chaque colonne donne le nombre d'interventions d'un type (feux d'habitations, feux de végétations, malaises, accidents…). Ce n'est pas une liste d'interventions. |
| Emprise géographique | France entière, outre-mer compris (codes 971 à 976 présents dans le fichier 2024). Niveau le plus fin : le département. Paris et la petite couronne sont regroupés sous la BSPP ; Marseille apparaît sous le BMPM. |
| Période réellement couverte par les données | Années 2008 à 2024 d'après la liste des fichiers. Vérifié dans les fichiers 2008, 2013 et 2024. Les autres années : non vérifiées (fichiers non ouverts). |
| Date de dernière mise à jour affichée sur la fiche | 2 juillet 2026 |
| Fréquence de mise à jour | Annuelle (indiquée sur la fiche) |
| Volumétrie | Environ 30 Ko par fichier. Fichier 2024 : 99 lignes de données × 71 colonnes. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | **Année** et **Numéro de département** (ex. `21` pour la Côte-d'Or). Attention : le nom de la région change selon les années (« Bourgogne » en 2008 et 2013, « Bourgogne-Franche-Comté » en 2024), il ne peut donc pas servir de clé. Les lignes BSPP et BMPM n'ont pas un numéro de département classique. |
| Données personnelles | Aucune : les données sont des totaux annuels par département. |
| Licence | Licence Ouverte / Open Licence d'Etalab (identifiant `fr-lo` sur data.gouv.fr, version 1.0). Réutilisation libre, à condition de citer la source. |
| Questions de mon analyse auxquelles elle pourrait répondre | **Q1 : non** (pas de commune). **Q2 : non** (un seul total par an, pas de mois). **Q3 : non** (pas de surface brûlée, pas d'indice). **Q4 : en partie** : elle permet de comparer, d'un département à l'autre, le nombre annuel de feux de végétations, mais sans lien avec la Météo des forêts. |

## Ce que j'ai découvert

- **« Feux de végétations » n'est pas « feux de forêt ».** La colonne compte tous les feux de végétation (forêts, mais aussi champs, broussailles…). C'est un terme à ajouter au glossaire. Exemple : 161 feux de végétations en Côte-d'Or en 2024.
- **La structure change selon les années.** Les fichiers 2008 et 2024 détaillent les feux en environ 70 colonnes (dont « Feux de végétations »). Les fichiers 2011 et 2013 n'ont que 16 colonnes, avec un seul total « Incendies » : on ne peut pas y isoler les feux de végétations. Une série continue de 2008 à 2024 n'est donc pas possible.
- **Problème de qualité :** dans le fichier 2024, les nombres de 1 000 et plus contiennent un « ? » à la place du séparateur de milliers (ex. `1?812` pour 1 812). Il faudra nettoyer ces valeurs avant tout calcul.
- **Conclusion :** source fiable et ouverte, mais trop agrégée (un total par an et par département) pour répondre à nos questions sur les zones, les mois, la taille des feux et l'indice. Elle peut seulement donner un ordre de grandeur pour comparer les départements (Q4).
