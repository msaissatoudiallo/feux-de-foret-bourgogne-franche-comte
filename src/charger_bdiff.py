"""Couche bronze : téléchargement de la BDIFF (ticket #39).

Télécharge depuis le portail https://bdiff.agriculture.gouv.fr les incendies de
forêt de la France entière, une année à la fois, et dépose chaque export tel
quel dans data/raw/bdiff/bdiff_AAAA.zip.

- Le zip n'est jamais modifié : il contient Incendies.csv, les définitions et
  les mentions légales du producteur (licence, D005).
- Une année par fichier, car le portail refuse l'export de la France entière
  sur 2006-2025 en une seule fois (52 811 incendies).
- Idempotent : une année déjà téléchargée n'est pas retéléchargée. L'option
  --force la remplace. Relancer le script ne crée donc aucun doublon.

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_bdiff.py                      # 2006 à 2025
    python src/charger_bdiff.py --debut 2024 --fin 2025
    python src/charger_bdiff.py --force              # tout retélécharger
"""

import argparse
import io
import time
import zipfile
from pathlib import Path

import requests
import truststore

# Le portail de la BDIFF envoie une chaîne de certificats incomplète : le
# navigateur la complète, mais pas Python. truststore fait vérifier les
# certificats par le système (macOS, Windows), comme le navigateur. La
# vérification reste active : on ne la désactive jamais.
truststore.inject_into_ssl()

PORTAIL = "https://bdiff.agriculture.gouv.fr"
DOSSIER = Path(__file__).resolve().parent.parent / "data" / "raw" / "bdiff"
PREMIERE_ANNEE = 2006  # la BDIFF centralise les données depuis 2006
DERNIERE_ANNEE = 2025  # dernière campagne publiée (2026 en cours de saisie)
ENTETES = {"User-Agent": "Mozilla/5.0 (projet etudiant feux de foret BFC)"}


def telecharger_annee(annee: int) -> bytes:
    """Refait la recherche du portail pour une année, puis récupère le zip."""
    with requests.Session() as session:
        session.headers.update(ENTETES)
        # 1. Ouvre le formulaire (crée la session sur le portail).
        session.get(f"{PORTAIL}/incendies", timeout=60).raise_for_status()
        # 2. Lance la recherche : France entière, une seule année.
        filtres = {
            "if[fr]": "1",
            "if[periodeAnnees][anneeDeb]": str(annee),
            "if[periodeAnnees][anneeFin]": str(annee),
            "if[submit]": "",
        }
        session.get(f"{PORTAIL}/incendies", params=filtres, timeout=120).raise_for_status()
        # 3. Exporte le résultat de la recherche (bouton « CSV » du portail).
        reponse = session.get(f"{PORTAIL}/incendies/zip", timeout=300, allow_redirects=False)
        reponse.raise_for_status()
        contenu = reponse.content

    verifier_zip(contenu, annee)
    return contenu


def verifier_zip(contenu: bytes, annee: int) -> None:
    """Refuse un fichier qui n'est pas un export complet de la BDIFF."""
    if not zipfile.is_zipfile(io.BytesIO(contenu)):
        raise RuntimeError(
            f"{annee} : le portail n'a pas renvoyé de zip "
            "(export refusé ou recherche vide). Rien n'est écrit."
        )
    with zipfile.ZipFile(io.BytesIO(contenu)) as archive:
        if "Incendies.csv" not in archive.namelist():
            raise RuntimeError(f"{annee} : Incendies.csv absent du zip. Rien n'est écrit.")
        if archive.testzip() is not None:
            raise RuntimeError(f"{annee} : zip abîmé. Rien n'est écrit.")


def compter_incendies(contenu: bytes) -> int:
    """Nombre de lignes de données dans Incendies.csv (pour le contrôle à l'écran)."""
    with zipfile.ZipFile(io.BytesIO(contenu)) as archive:
        lignes = archive.read("Incendies.csv").decode("utf-8-sig").splitlines()
    entete = next(i for i, ligne in enumerate(lignes) if ligne.startswith("Année;"))
    return sum(1 for ligne in lignes[entete + 1:] if ligne.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge la BDIFF dans data/raw/bdiff/.")
    parser.add_argument("--debut", type=int, default=PREMIERE_ANNEE, help="première année (défaut : 2006)")
    parser.add_argument("--fin", type=int, default=DERNIERE_ANNEE, help="dernière année (défaut : 2025)")
    parser.add_argument("--force", action="store_true", help="retélécharge les années déjà présentes")
    args = parser.parse_args()

    DOSSIER.mkdir(parents=True, exist_ok=True)
    total = 0
    for annee in range(args.debut, args.fin + 1):
        fichier = DOSSIER / f"bdiff_{annee}.zip"
        if fichier.exists() and not args.force:
            print(f"{annee} : déjà présent ({fichier.name}), ignoré")
            continue

        contenu = telecharger_annee(annee)
        # Écrit d'abord un fichier temporaire, puis le renomme : un téléchargement
        # interrompu ne laisse jamais un zip incomplet à la place du bon.
        temporaire = fichier.with_suffix(".zip.tmp")
        temporaire.write_bytes(contenu)
        temporaire.replace(fichier)

        nombre = compter_incendies(contenu)
        total += nombre
        print(f"{annee} : {nombre} incendies -> {fichier.name}")
        time.sleep(1)  # une requête par seconde au plus, pour ménager le portail

    print(f"Terminé. {total} incendies téléchargés dans {DOSSIER}")


if __name__ == "__main__":
    main()
