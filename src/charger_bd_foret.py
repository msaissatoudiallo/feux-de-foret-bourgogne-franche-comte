"""Couche bronze : téléchargement de la BD Forêt V2 (ticket #115).

Télécharge depuis le service de l'IGN (data.geopf.fr) l'archive .7z de la
BD Forêt V2 d'un département (la Côte-d'Or par défaut) et la dépose telle
quelle dans data/raw/bd_foret/, sous le nom donné par l'IGN, par exemple
BDFORET_2-0__SHP_LAMB93_D021_2017-10-04.7z (la date est celle de l'édition).

- L'archive n'est jamais décompressée ni modifiée : elle garde la carte
  (FORMATION_VEGETALE.shp et ses fichiers), les métadonnées et le LISEZ-MOI.
- Le lien et la taille attendue sont lus dans le catalogue de l'IGN : le
  script trouve seul l'édition V2 du département.
- Le fichier reçu est contrôlé : taille annoncée par l'IGN, archive .7z
  lisible et intacte, carte présente. Sinon, rien n'est écrit.
- Idempotent : une archive déjà téléchargée n'est pas retéléchargée. L'option
  --force la remplace. Relancer le script ne crée donc aucun doublon.

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_bd_foret.py                    # Côte-d'Or
    python src/charger_bd_foret.py --departement 89   # un autre département
    python src/charger_bd_foret.py --force            # retélécharger
"""

import argparse
import struct
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import py7zr
import requests

CATALOGUE = "https://data.geopf.fr/telechargement/resource/BDFORET"
EDITION_V2 = "BDFORET_2-0__SHP_LAMB93_"  # la V1 (2,25 ha) est aussi au catalogue : on ne la prend pas
DOSSIER = Path(__file__).resolve().parent.parent / "data" / "raw" / "bd_foret"
CARTE = "FORMATION_VEGETALE"  # nom de la couche des zones de forêt dans l'archive
ENTETES = {"User-Agent": "Mozilla/5.0 (projet etudiant feux de foret BFC)"}
ATOM = {"atom": "http://www.w3.org/2005/Atom", "gpf_dl": "https://data.geopf.fr/annexes/ressources/xsd/gpf_dl.xsd"}


def trouver_archive(departement: str) -> tuple[str, int]:
    """Lit le catalogue de l'IGN : lien de l'archive V2 du département et sa taille."""
    zone = f"D{departement.zfill(3)}"  # '21' -> 'D021'
    reponse = requests.get(CATALOGUE, params={"zone": zone}, headers=ENTETES, timeout=60)
    reponse.raise_for_status()
    editions = [
        entree.find("atom:title", ATOM).text
        for entree in ET.fromstring(reponse.content).findall("atom:entry", ATOM)
    ]
    editions_v2 = sorted(e for e in editions if e.startswith(EDITION_V2 + zone))
    if not editions_v2:
        raise RuntimeError(f"Pas de BD Forêt V2 au catalogue de l'IGN pour {zone}.")
    edition = editions_v2[-1]  # la plus récente, si l'IGN en publie plusieurs

    # La page de l'édition donne le lien de l'archive et sa taille en octets.
    reponse = requests.get(f"{CATALOGUE}/{edition}", headers=ENTETES, timeout=60)
    reponse.raise_for_status()
    for lien in ET.fromstring(reponse.content).iter(f"{{{ATOM['atom']}}}link"):
        if lien.get("href", "").endswith(".7z"):
            return lien.get("href"), int(lien.get(f"{{{ATOM['gpf_dl']}}}length"))
    raise RuntimeError(f"Pas d'archive .7z pour l'édition {edition}.")


def telecharger(url: str, destination: Path) -> None:
    """Télécharge l'archive morceau par morceau (environ 30 Mo)."""
    with requests.get(url, headers=ENTETES, stream=True, timeout=300) as reponse:
        reponse.raise_for_status()
        with destination.open("wb") as fichier:
            for morceau in reponse.iter_content(chunk_size=1024 * 1024):
                fichier.write(morceau)


def verifier_archive(chemin: Path, taille_attendue: int) -> int:
    """Refuse une archive incomplète ou abîmée ; renvoie le nombre de zones de forêt."""
    taille = chemin.stat().st_size
    if taille != taille_attendue:
        raise RuntimeError(f"Taille reçue {taille} octets, {taille_attendue} annoncés par l'IGN.")
    if not py7zr.is_7zfile(chemin):
        raise RuntimeError("Le fichier reçu n'est pas une archive .7z.")
    try:
        with py7zr.SevenZipFile(chemin) as archive:
            noms = archive.getnames()
            abime = archive.testzip()  # contrôle de chaque fichier (CRC)
    except Exception as erreur:  # py7zr lève une erreur si les données sont illisibles
        raise RuntimeError(f"Archive abîmée ({erreur}).") from erreur
    if abime is not None:
        raise RuntimeError(f"Archive abîmée ({abime}).")
    morceaux = {ext: [n for n in noms if n.endswith(f"/{CARTE}.{ext}")] for ext in ("shp", "shx", "dbf", "prj")}
    manquants = [ext for ext, trouves in morceaux.items() if not trouves]
    if manquants:
        raise RuntimeError(f"Carte {CARTE} incomplète dans l'archive : {', '.join(manquants)} absent.")
    return compter_zones(chemin, morceaux["dbf"][0])


def compter_zones(chemin: Path, nom_dbf: str) -> int:
    """Nombre de zones de forêt, lu dans l'en-tête du .dbf (pour le contrôle à l'écran)."""
    with tempfile.TemporaryDirectory() as dossier, py7zr.SevenZipFile(chemin) as archive:
        archive.extract(path=dossier, targets=[nom_dbf])
        entete = (Path(dossier) / nom_dbf).read_bytes()[:8]
    return struct.unpack("<I", entete[4:8])[0]  # octets 4 à 7 : nombre de lignes


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge la BD Forêt V2 dans data/raw/bd_foret/.")
    parser.add_argument("--departement", default="21", help="code du département (défaut : 21, Côte-d'Or)")
    parser.add_argument("--force", action="store_true", help="retélécharge l'archive déjà présente")
    args = parser.parse_args()

    url, taille = trouver_archive(args.departement)
    fichier = DOSSIER / url.rsplit("/", 1)[-1]
    if fichier.exists() and not args.force:
        print(f"Déjà présent ({fichier.name}), ignoré")
        return

    DOSSIER.mkdir(parents=True, exist_ok=True)
    # Écrit d'abord un fichier temporaire, contrôlé, puis le renomme : un
    # téléchargement interrompu ou abîmé ne remplace jamais le bon fichier.
    temporaire = fichier.with_name(fichier.name + ".tmp")
    try:
        telecharger(url, temporaire)
        zones = verifier_archive(temporaire, taille)
    except Exception:
        temporaire.unlink(missing_ok=True)
        raise
    temporaire.replace(fichier)
    print(f"{fichier.name} : {taille / 1e6:.0f} Mo, {zones} zones de forêt -> {DOSSIER}")


if __name__ == "__main__":
    main()
