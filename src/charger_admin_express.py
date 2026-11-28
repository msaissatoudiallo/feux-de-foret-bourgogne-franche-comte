"""Couche bronze : téléchargement d'Admin Express (ticket #116).

Télécharge depuis le service WFS de l'IGN (https://data.geopf.fr/wfs) les
contours des communes et des départements d'Admin Express COG, et les dépose
tels quels (GeoJSON) dans data/raw/admin_express/ :

- communes_AAAA_DD.geojson : les communes de l'édition la plus récente, un
  fichier par département, pour les 96 départements de France métropolitaine
  (D022, D023) ;
- communes_2017_DD.geojson : les communes de l'édition 2017, pour la table de
  passage des communes fusionnées (D023) ;
- departements_AAAA.geojson : les contours des 96 départements, pour rattacher
  les mailles de Copernicus et les stations météo aux départements.

AAAA est l'année de l'édition la plus récente, trouvée seule dans le catalogue
du service (2026 au 28/11/2026). L'année est écrite dans le nom du fichier :
quand l'IGN publiera une nouvelle édition, les fichiers ne seront pas mélangés.

- Version précise d'Admin Express (COG), pas la version simplifiée (CARTO) :
  la surface des communes et leur part de forêt (H1, H8) sont calculées sur ces
  contours.
- Le fichier reçu est contrôlé : GeoJSON lisible, nombre de communes égal au
  nombre annoncé par l'IGN, toutes du bon département, codes INSEE de 5
  caractères sans doublon. Sinon, rien n'est écrit.
- Idempotent : un fichier déjà présent n'est pas retéléchargé. L'option --force
  le remplace. Relancer le script ne crée donc aucun doublon.

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_admin_express.py                    # les 96 départements
    python src/charger_admin_express.py --departement 21   # essai sur la Côte-d'Or
    python src/charger_admin_express.py --force            # tout retélécharger
"""

import argparse
import json
import re
import time
from pathlib import Path

import requests

WFS = "https://data.geopf.fr/wfs/ows"
DOSSIER = Path(__file__).resolve().parent.parent / "data" / "raw" / "admin_express"
ENTETES = {"User-Agent": "Mozilla/5.0 (projet etudiant feux de foret BFC)"}
EDITION_FUSIONS = 2017  # première édition d'Admin Express COG, pour la table de passage

# Les noms des colonnes changent selon l'édition (fiche Admin Express) :
# insee_com et insee_dep jusqu'en 2020, code_insee et code_insee_du_departement ensuite.
COLONNES = {
    "ancienne": {"commune": "insee_com", "departement": "insee_dep"},
    "recente": {"commune": "code_insee", "departement": "code_insee_du_departement"},
}
COLONNE_CODE_DEPARTEMENT = {"ancienne": "insee_dep", "recente": "code_insee"}  # couche departement


def colonnes(edition: int) -> str:
    """'ancienne' (2017 à 2020) ou 'recente' (2021 et après)."""
    return "ancienne" if edition <= 2020 else "recente"


def edition_la_plus_recente() -> int:
    """Lit le catalogue du service : année de la dernière édition d'Admin Express COG."""
    reponse = requests.get(
        WFS, params={"SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetCapabilities"},
        headers=ENTETES, timeout=120,
    )
    reponse.raise_for_status()
    annees = {int(a) for a in re.findall(r"<Name>ADMINEXPRESS-COG\.(\d{4}):commune</Name>", reponse.text)}
    if not annees:
        raise RuntimeError("Aucune édition d'Admin Express COG dans le catalogue du service WFS de l'IGN.")
    return max(annees)


def demander(couche: str, filtre: str | None = None) -> bytes:
    """Demande une couche au service WFS, en GeoJSON, avec un filtre éventuel."""
    params = {
        "SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature",
        "TYPENAMES": couche, "OUTPUTFORMAT": "application/json",
    }
    if filtre:
        params["CQL_FILTER"] = filtre
    reponse = requests.get(WFS, params=params, headers=ENTETES, timeout=300)
    reponse.raise_for_status()
    return reponse.content


def lire_geojson(contenu: bytes) -> dict:
    """Refuse une réponse illisible ou incomplète (moins d'objets que le nombre annoncé)."""
    try:
        donnees = json.loads(contenu)
    except ValueError as erreur:
        raise RuntimeError(f"réponse illisible ({erreur})") from erreur
    if donnees.get("type") != "FeatureCollection":
        raise RuntimeError("la réponse n'est pas une carte GeoJSON")
    objets = donnees["features"]
    annonces = donnees.get("numberMatched")
    if annonces is not None and len(objets) != int(annonces):
        raise RuntimeError(f"{len(objets)} objets reçus, {annonces} annoncés par l'IGN")
    if not objets:
        raise RuntimeError("aucun objet reçu")
    return donnees


def codes_departements(contenu: bytes, edition: int) -> list[str]:
    """Codes des départements d'une réponse ; refuse une liste qui n'a pas les 96 de métropole."""
    colonne = COLONNE_CODE_DEPARTEMENT[colonnes(edition)]
    codes = sorted(objet["properties"][colonne] for objet in lire_geojson(contenu)["features"])
    if len(codes) != 96 or len(set(codes)) != 96:
        raise RuntimeError(f"{len(set(codes))} départements de métropole reçus, 96 attendus. Rien n'est écrit.")
    return codes


def departements_metropole(edition: int) -> bytes:
    """Contours des départements de métropole, sans les codes 97x (environ 110 Mo)."""
    colonne = COLONNE_CODE_DEPARTEMENT[colonnes(edition)]
    return demander(f"ADMINEXPRESS-COG.{edition}:departement", f"{colonne} NOT LIKE '97%'")


def verifier_communes(contenu: bytes, edition: int, departement: str) -> int:
    """Refuse un fichier incomplet, d'un autre département ou aux codes INSEE anormaux."""
    noms = COLONNES[colonnes(edition)]
    objets = lire_geojson(contenu)["features"]
    codes = [objet["properties"].get(noms["commune"]) or "" for objet in objets]
    autres = {objet["properties"].get(noms["departement"]) for objet in objets} - {departement}
    if autres:
        raise RuntimeError(f"communes d'un autre département reçues ({sorted(map(str, autres))})")
    anormaux = [code for code in codes if len(code) != 5]
    if anormaux:
        raise RuntimeError(f"codes INSEE vides ou mal formés ({anormaux[:3]})")
    if len(set(codes)) != len(codes):
        raise RuntimeError("codes INSEE en double")
    return len(codes)


def enregistrer(fichier: Path, contenu: bytes) -> None:
    """Écrit d'abord un fichier temporaire, puis le renomme : un fichier abîmé ne remplace jamais le bon."""
    temporaire = fichier.with_name(fichier.name + ".tmp")
    temporaire.write_bytes(contenu)
    temporaire.replace(fichier)


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge Admin Express dans data/raw/admin_express/.")
    parser.add_argument("--departement", help="un seul département, pour un essai (ex. 21)")
    parser.add_argument("--force", action="store_true", help="retélécharge les fichiers déjà présents")
    args = parser.parse_args()

    recente = edition_la_plus_recente()
    print(f"Édition la plus récente d'Admin Express COG : {recente}")
    DOSSIER.mkdir(parents=True, exist_ok=True)

    # 1. Les contours des départements, qui donnent aussi la liste des 96 codes de métropole.
    fichier = DOSSIER / f"departements_{recente}.geojson"
    if fichier.exists() and not args.force:
        codes = codes_departements(fichier.read_bytes(), recente)
        print(f"{fichier.name} : déjà présent, ignoré")
    else:
        contenu = departements_metropole(recente)
        try:
            codes = codes_departements(contenu, recente)
        except RuntimeError as erreur:
            raise RuntimeError(f"{fichier.name} refusé ({erreur})") from erreur
        enregistrer(fichier, contenu)
        print(f"{fichier.name} : {len(codes)} départements")

    if args.departement:
        if args.departement not in codes:
            raise SystemExit(f"{args.departement} n'est pas un département de métropole (ex. 01, 21, 2A).")
        codes = [args.departement]

    # 2. Les communes, un fichier par édition et par département.
    totaux = {}
    for edition in (recente, EDITION_FUSIONS):
        colonne = COLONNES[colonnes(edition)]["departement"]
        totaux[edition] = 0
        for code in codes:
            fichier = DOSSIER / f"communes_{edition}_{code}.geojson"
            if fichier.exists() and not args.force:
                totaux[edition] += verifier_communes(fichier.read_bytes(), edition, code)
                print(f"{fichier.name} : déjà présent, ignoré")
                continue
            contenu = demander(f"ADMINEXPRESS-COG.{edition}:commune", f"{colonne}='{code}'")
            try:
                nombre = verifier_communes(contenu, edition, code)
            except RuntimeError as erreur:
                raise RuntimeError(f"{fichier.name} refusé ({erreur}). Rien n'est écrit.") from erreur
            enregistrer(fichier, contenu)
            totaux[edition] += nombre
            print(f"{fichier.name} : {nombre} communes")
            time.sleep(1)  # une demande par seconde au plus, pour ménager le service de l'IGN

    for edition, total in totaux.items():
        print(f"Édition {edition} : {total} communes dans {len(codes)} département(s)")
    print(f"Terminé : fichiers dans {DOSSIER}")


if __name__ == "__main__":
    main()
