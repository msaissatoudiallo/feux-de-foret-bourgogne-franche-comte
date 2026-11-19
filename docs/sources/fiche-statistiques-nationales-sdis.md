# Fiche d'identité – Statistiques nationales des SDIS

- **Explorée par :** Aissatou Diallo
- **Date d'exploration :** 2026-11-17
- **Page de la source (dans la liste du défi) :** https://www.ressourcesdupompier.com/etudes-statistiques/
- **Nom dans la liste du défi :** « Statistiques nationales des SDIS » (groupe « Statistiques annuelles des services départementaux d'incendie et de secours »)
- **Fichier ouvert :** plaquette « Les statistiques des services d'incendie et de secours – édition 2023 » (PDF de 84 pages, hébergé sur le site du ministère de l'Intérieur : https://www.interieur.gouv.fr/sites/minint/files/medias/documents/2025-09/StatsSDIS23BD%283%29.pdf)

## Fiche

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Producteur : Direction générale de la sécurité civile et de la gestion des crises (DGSCGC), ministère de l'Intérieur. Les chiffres sont déclarés chaque année par les 99 services d'incendie et de secours sur le site www.infosdis.fr (indiqué dans l'avant-propos de la plaquette). Le site ressourcesdupompier.com n'est pas le producteur : il rassemble des liens vers les plaquettes, hébergées sur plusieurs sites (ministère de l'Intérieur, ENSOSP, sites tiers). |
| Mode d'accès et format | Téléchargement de documents **PDF** (une plaquette par édition). Aucun fichier CSV ni Excel sur la page. Les tableaux devraient être extraits du PDF pour être exploités. |
| Grain (une ligne = ?) | Mélangé. La plupart des pages donnent des indicateurs **nationaux** ou **par catégorie de SDIS** (A, B, C). Les annexes contiennent des tableaux où **une ligne = un service d'incendie et de secours (un département) sur une année** (interventions, effectifs, dépenses, population). |
| Emprise géographique | France entière, département par département dans les annexes. |
| Période réellement couverte par les données | Plaquette ouverte : **édition 2023, qui décrit l'année 2022** (« Les chiffres 2022 restituent les informations recueillies… »). L'édition d'une plaquette ne correspond donc pas à l'année des données. La page liste les éditions 2014 à 2025 : non vérifiées (non ouvertes). |
| Date de dernière mise à jour affichée sur la fiche | Non vérifiée : la page n'affiche pas de date de mise à jour. La dernière édition listée est datée « déc. 2025 ». |
| Fréquence de mise à jour | Annuelle (une édition par an d'après la liste des documents). |
| Volumétrie | Édition 2023 : un PDF de 84 pages, environ 8 Mo. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | **Numéro de département** (attention : la Corse est notée `2a` et `2b` en minuscules dans les annexes) et **année des données**. |
| Données personnelles | Aucune vue dans la plaquette : uniquement des totaux et des moyennes. |
| Licence | **Non vérifiée** : aucune licence ni condition de réutilisation n'est indiquée sur la page ressourcesdupompier.com, ni trouvée dans la plaquette (recherche des mots « licence », « copyright », « reproduction »). |
| Questions de mon analyse auxquelles elle pourrait répondre | **Q1 : non** (pas de commune). **Q2 : non** (pas de mois). **Q3 : non** (pas de surface par feu, pas d'indice). **Q4 : en partie** : elle permet de comparer les départements entre eux, mais sans lien avec la Météo des forêts. |

## Ce que j'ai découvert

- **C'est la même enquête que la source « Interventions SDIS ».** Le total d'interventions de la Côte-d'Or en 2022 est le même dans la plaquette et dans le fichier CSV de data.gouv.fr : **28 330**. Pour les nombres d'interventions, le CSV de data.gouv.fr est préférable (format exploitable, licence connue).
- **Elle apporte en plus des informations sur les moyens**, absentes du CSV : effectifs de sapeurs-pompiers professionnels et volontaires, dépenses de fonctionnement et d'investissement de chaque SDIS. Exemple pour la Côte-d'Or en 2022 : 308 sapeurs-pompiers professionnels, 1 690 volontaires, 34 M€ de dépenses de fonctionnement et 10 M€ d'investissement. Cela peut servir à comparer les **moyens humains et financiers** du SDIS 21 avec ceux des autres départements (premier point de la commande).
- **Peu de chiffres sur les feux de forêt par département** dans la plaquette : les indicateurs sur les feux de forêt sont surtout nationaux (ex. 87 % des feux de forêt éteints avant d'avoir détruit 5 hectares, sur un échantillon de 68 SDIS sur 94).
- **Points de qualité :**
  - quand un SDIS n'a pas répondu, les totaux nationaux utilisent la moyenne de sa catégorie (avant-propos) ;
  - les chiffres d'une année peuvent être corrigés dans l'édition suivante ;
  - sur la page ressourcesdupompier.com, certains liens semblent ne pas correspondre à l'année affichée (ex. l'édition « 2019 » pointe vers un fichier nommé « chiffres-2018 »).
- **Conclusion :** source utile seulement pour comparer les moyens des SDIS entre départements. Elle ne répond pas à nos questions sur les feux. Format PDF et licence non indiquée : à utiliser avec prudence.
