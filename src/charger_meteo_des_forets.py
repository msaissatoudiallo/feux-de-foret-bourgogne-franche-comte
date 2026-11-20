"""Couche bronze : téléchargement de la Météo des forêts (ticket #40).

Télécharge les archives de la Météo des forêts publiées par Météo-France
(jeu « Archives de la Météo des forêts » sur data.gouv.fr) et dépose chaque
fichier tel quel dans data/raw/meteo_des_forets/mdf_AAAA.csv.gz.

- Le fichier n'est jamais modifié : il est enregistré compressé, comme il est
  publié. Le séparateur (« , » en 2024 et 2025, « ; » en 2026), les numéros de
  département sans zéro (2024, 2025) et l'heure en UTC sont traités plus tard,
  dans la couche silver (fiche docs/sources/fiche-meteo-des-forets.md).
- Un fichier par année : les archives commencent le 3 juin 2024.
- Idempotent : une année déjà téléchargée n'est pas retéléchargée. L'option
  --force la remplace. Relancer le script ne crée donc aucun doublon.
  Le fichier de l'année en cours est complété par Météo-France pendant la
  saison des feux : pour avoir la dernière version, le relancer avec --force.

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_meteo_des_forets.py                      # 2024 à 2026
    python src/charger_meteo_des_forets.py --debut 2026 --fin 2026
    python src/charger_meteo_des_forets.py --force              # tout retélécharger
"""

import argparse
import gzip
import time
from pathlib import Path

import requests

# Adresse des fichiers, celle des liens « mdf.AAAA » de la page data.gouv.fr
# https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets
ADRESSE = "https://meteofrance.s3.sbg.io.cloud.ovh.net/data/BULLETIN/MDF/mdf_{annee}.csv.gz"
DOSSIER = Path(__file__).resolve().parent.parent / "data" / "raw" / "meteo_des_forets"
PREMIERE_ANNEE = 2024  # les archives commencent le 3 juin 2024
DERNIERE_ANNEE = 2026
COLONNES = ("date", "num_dep", "niveau_j1", "niveau_j2")  # présentes toutes les années


def telecharger_annee(annee: int) -> bytes:
    """Récupère le fichier compressé d'une année."""
    reponse = requests.get(ADRESSE.format(annee=annee), timeout=120)
    if reponse.status_code == 404:
        raise RuntimeError(f"{annee} : fichier absent chez Météo-France. Rien n'est écrit.")
    reponse.raise_for_status()
    return reponse.content


def verifier_fichier(contenu: bytes, annee: int) -> tuple[int, str]:
    """Refuse un fichier qui n'est pas une archive de la Météo des forêts.

    Renvoie le nombre de lignes de données et le séparateur trouvé, pour le
    contrôle à l'écran.
    """
    try:
        texte = gzip.decompress(contenu).decode("utf-8-sig")
    except (OSError, UnicodeDecodeError) as erreur:
        raise RuntimeError(f"{annee} : fichier illisible ({erreur}). Rien n'est écrit.") from erreur

    lignes = [ligne for ligne in texte.splitlines() if ligne.strip()]
    if not lignes:
        raise RuntimeError(f"{annee} : fichier vide. Rien n'est écrit.")
    entete = lignes[0]
    separateur = ";" if entete.count(";") > entete.count(",") else ","
    colonnes = [colonne.strip() for colonne in entete.split(separateur)]
    manquantes = [colonne for colonne in COLONNES if colonne not in colonnes]
    if manquantes:
        raise RuntimeError(f"{annee} : colonnes absentes {manquantes}. Rien n'est écrit.")
    return len(lignes) - 1, separateur


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge la Météo des forêts dans data/raw/meteo_des_forets/.")
    parser.add_argument("--debut", type=int, default=PREMIERE_ANNEE, help="première année (défaut : 2024)")
    parser.add_argument("--fin", type=int, default=DERNIERE_ANNEE, help="dernière année (défaut : 2026)")
    parser.add_argument("--force", action="store_true", help="retélécharge les années déjà présentes")
    args = parser.parse_args()

    DOSSIER.mkdir(parents=True, exist_ok=True)
    total = 0
    for annee in range(args.debut, args.fin + 1):
        fichier = DOSSIER / f"mdf_{annee}.csv.gz"
        if fichier.exists() and not args.force:
            print(f"{annee} : déjà présent ({fichier.name}), ignoré")
            continue

        contenu = telecharger_annee(annee)
        nombre, separateur = verifier_fichier(contenu, annee)
        # Écrit d'abord un fichier temporaire, puis le renomme : un téléchargement
        # interrompu ne laisse jamais un fichier incomplet à la place du bon.
        temporaire = fichier.with_name(fichier.name + ".tmp")
        temporaire.write_bytes(contenu)
        temporaire.replace(fichier)

        total += nombre
        print(f"{annee} : {nombre} lignes, séparateur « {separateur} » -> {fichier.name}")
        time.sleep(1)  # une requête par seconde au plus

    print(f"Terminé. {total} lignes téléchargées dans {DOSSIER}")


if __name__ == "__main__":
    main()
