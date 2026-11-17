# Analyse de la commande - Melvyn

## Ma compréhension en bref

La direction du SDIS 21 doit décider, pour l'été 2027, où placer ses moyens et à partir de quel niveau de la Météo des forêts renforcer le dispositif.

- L'indice mesure un **danger** (la végétation et la météo permettent à un feu de partir et de se propager), pas un départ de feu. Ce qui allume le feu est le plus souvent humain (travaux agricoles, imprudences).
- Cela explique les deux plaintes des chefs de centre : un indice élevé sans feu (personne n'a rien allumé) et des feux avec un indice bas (un feu allumé dans un champ sec, par exemple).
- Le choix du seuil est un compromis : un seuil bas rate peu de feux mais coûte cher, un seuil haut coûte moins mais rate des feux. Le budget fixe la limite.

## 1. Les questions

1. **Pour décider sur quels créneaux renforcer patrouilles et guet**, la direction a besoin de savoir à quelles heures de la journée et quels jours de la semaine (semaine ou week-end) partent les feux en Côte-d'Or.
   - Si les feux se concentrent sur quelques créneaux (par exemple l'après-midi ou le week-end), elle renforce seulement sur ces créneaux, ce qui coûte moins cher.
   - S'ils partent à toute heure, elle garde un renforcement sur la journée entière.
2. **Pour décider où prépositionner des moyens**, la direction a besoin de savoir si les feux qui deviennent gros sont ceux où les secours arrivent le plus tard.
   - Si oui, elle place des moyens à l'avance près des zones éloignées des casernes.
   - Si non, la taille du feu dépend surtout de la météo, et elle mise sur le seuil de déclenchement.
3. **Pour décider où concentrer la prévention et la surveillance**, la direction a besoin de savoir où un feu ferait le plus de dégâts (forêts proches des habitations, des routes ou de zones sensibles).
   - Si ces zones sont peu nombreuses, elle y concentre ses moyens en priorité.
   - Si elles sont partout, elle répartit ses moyens selon la fréquence des feux.
4. **Pour décider combien de jours de renforcement prévoir au budget 2027**, la direction a besoin de savoir si le nombre de jours de danger élevé augmente d'un été à l'autre en Côte-d'Or.
   - Si oui, elle prévoit plus de jours que les années passées.
   - Si non, elle se base sur la moyenne des étés passés.

## 2. Les termes inconnus

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| SDIS | Service départemental d'incendie et de secours (les pompiers du département) | Son découpage en centres et en zones |
| Météo des forêts | Indice quotidien de danger de feu publié par Météo-France | Nombre de niveaux, date de création, échelle géographique |
| IFM | Indice forêt météo, le calcul sur lequel repose la Météo des forêts | Comment il est calculé, s'il existe un historique avant la Météo des forêts |
| Départ de feu | Un feu qui se déclare, quelle que soit sa taille | Une surface minimale pour être compté |
| Feu de forêt / feu de végétation | Feu en forêt / feu plus large (champs, broussailles, landes) | Ce que la direction inclut dans sa demande |
| Dispositif renforcé | Moyens ajoutés les jours à risque (patrouilles, guet) | Son contenu exact et son coût par jour |
| Guet | Surveillance depuis des points hauts pour repérer les fumées | Où et combien de postes |
| Moyens | Personnes, véhicules et budget | Ce qui est réellement déplaçable |
| Délai d'intervention | Le temps entre l'alerte et l'arrivée des secours sur le feu | Si ce délai est enregistré, et à partir de quel moment il est compté |
| Enjeux | Ce qu'un feu menace : habitations, routes, zones sensibles | Ce que le SDIS considère comme un enjeu prioritaire |

## 3. Les besoins

La décision à éclairer, en une phrase : où et à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé en Côte-d'Or, dans la limite du budget.

Ce qui manque dans la commande pour y répondre :
- le budget disponible, ou le nombre de jours de renforcement qu'il permet ;
- le seuil actuel utilisé par le SDIS ;
- la période qui compte comme « l'été » (dates de début et de fin de la saison) ;
- la définition d'un feu retenue par la direction (forêt seulement ou toute végétation) ;
- l'emplacement des casernes et des postes de guet.

## 4. Les données

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Liste des feux avec la date et l'heure de l'alerte | Un feu | Au moins 10 saisons | Saison 2026 incluse | Côte-d'Or |
| 2 | Liste des feux avec l'heure de l'alerte, l'heure d'arrivée des secours et la surface brûlée ; emplacement des casernes | Un feu | Au moins 10 saisons | Saison 2026 incluse | Côte-d'Or |
| 3 | Occupation du sol (forêts, habitations, routes) et liste des feux avec leur lieu | Une parcelle ou une commune | Le millésime le plus récent | Le plus récent disponible | Côte-d'Or, par commune |
| 4 | Niveau quotidien de la Météo des forêts, ou historique de l'indice IFM | Un jour × une zone de prévision | Le plus d'étés possible | Saison 2026 incluse | Côte-d'Or, et la région pour comparer la tendance |
