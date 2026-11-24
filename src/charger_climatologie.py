"""Couche bronze : téléchargement des Données climatologiques quotidiennes (ticket #117).

Télécharge depuis data.gouv.fr (fichiers hébergés par Météo-France) les mesures
quotidiennes des stations d'un département (la Côte-d'Or par défaut) et leurs
descriptifs, et les dépose tels quels dans data/raw/climatologie/ :

- 4 fichiers de mesures (.csv.gz) : période ancienne (1950 à N-2) et récente
  (N-1 et N), pour chaque groupe de paramètres (« RR-T-Vent » et « autres
  paramètres »). Le fichier « avant 1949 » n'est pas pris (hors période).
- 3 descriptifs : les champs de chaque groupe (.csv) et le descriptif général (.pdf).

Les fichiers ne sont jamais décompressés ni modifiés. Leur liste est lue dans
le catalogue de data.gouv.fr : quand Météo-France change les périodes (par
exemple previous-1950-2025 en 2027), le script prend les nouveaux noms seul.

- Le fichier reçu est contrôlé : taille annoncée par le serveur, gzip lisible
  jusqu'au bout, colonnes attendues, stations du bon département. Sinon, rien
  n'est écrit.
- Idempotent : un fichier déjà présent n'est pas retéléchargé. L'option --force
  les remplace (utile pour la période récente, mise à jour chaque jour).

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_climatologie.py                    # Côte-d'Or
    python src/charger_climatologie.py --departement 89   # un autre département
    python src/charger_climatologie.py --force            # tout retélécharger
"""

import argparse
import gzip
import re
import time
from pathlib import Path

import requests

API = "https://www.data.gouv.fr/api/1/datasets/donnees-climatologiques-de-base-quotidiennes/"
DOSSIER = Path(__file__).resolve().parent.parent / "data" / "raw" / "climatologie"
DEBUT_COLONNES = "NUM_POSTE;NOM_USUEL;LAT;LON;ALTI;AAAAMMJJ;"  # 6 premières colonnes de chaque fichier de mesures
ENTETES = {"User-Agent": "Mozilla/5.0 (projet etudiant feux de foret BFC)"}


def lister_fichiers(departement: str) -> list[str]:
    """Lit le catalogue de data.gouv.fr : liens des mesures du département et des descriptifs."""
    reponse = requests.get(API, headers=ENTETES, timeout=120)
    reponse.raise_for_status()
    # Titre des mesures : QUOT_departement_21_periode_1950-2024_RR-T-Vent
    mesures = re.compile(rf"QUOT_departement_{departement}_periode_(?!avant-1949)\S+_(RR-T-Vent|autres-parametres)$")
    liens = []
    for ressource in reponse.json()["resources"]:
        titre, url = ressource["title"], ressource["url"]
        if mesures.match(titre) or titre.startswith("Q_descriptif_champs_") or titre == "CLIMATOLOGIE_Donnees_quotidiennes_descriptif.pdf":
            liens.append(url)
    nb_mesures = sum(url.endswith(".csv.gz") for url in liens)
    if nb_mesures != 4 or len(liens) != 7:
        raise RuntimeError(
            f"Catalogue inattendu pour le département {departement} : {nb_mesures} fichiers de mesures "
            f"et {len(liens) - nb_mesures} descriptifs trouvés (4 et 3 attendus). Rien n'est écrit."
        )
    return sorted(liens)


def telecharger(url: str, destination: Path) -> None:
    """Télécharge le fichier morceau par morceau et vérifie qu'il est arrivé en entier."""
    with requests.get(url, headers=ENTETES, stream=True, timeout=300) as reponse:
        reponse.raise_for_status()
        taille_annoncee = int(reponse.headers.get("Content-Length", -1))
        with destination.open("wb") as fichier:
            for morceau in reponse.iter_content(chunk_size=1024 * 1024):
                fichier.write(morceau)
    taille = destination.stat().st_size
    if taille_annoncee >= 0 and taille != taille_annoncee:
        raise RuntimeError(f"{destination.name} : {taille} octets reçus, {taille_annoncee} annoncés.")


def verifier_mesures(chemin: Path, departement: str) -> str:
    """Refuse un fichier de mesures abîmé ou d'un autre département ; renvoie un résumé."""
    lignes, stations, dates = 0, set(), set()
    try:
        with gzip.open(chemin, "rt", encoding="utf-8") as fichier:
            entete = fichier.readline()
            if not entete.startswith(DEBUT_COLONNES):
                raise RuntimeError("colonnes inattendues")
            for ligne in fichier:  # lit tout le fichier : un gzip tronqué lève une erreur
                num_poste, _, _, _, _, date = ligne.split(";", 6)[:6]
                if not num_poste.startswith(departement):
                    raise RuntimeError(f"station {num_poste} hors du département {departement}")
                lignes += 1
                stations.add(num_poste)
                dates.add(date)
    except (OSError, EOFError, UnicodeDecodeError, ValueError, RuntimeError) as erreur:
        raise RuntimeError(f"{chemin.name} refusé ({erreur}). Rien n'est écrit.") from erreur
    if lignes == 0:
        raise RuntimeError(f"{chemin.name} refusé (aucune mesure). Rien n'est écrit.")
    return f"{lignes} lignes, {len(stations)} stations, du {min(dates)} au {max(dates)}"


def verifier_descriptif(chemin: Path, nom: str) -> str:
    """Refuse un descriptif vide ou qui n'est pas celui attendu (nom = nom final du fichier)."""
    contenu = chemin.read_bytes()
    if nom.endswith(".pdf"):
        valide = contenu.startswith(b"%PDF")
    else:
        valide = "NUM_POSTE" in contenu.decode("utf-8", errors="replace")
    if not valide:
        raise RuntimeError(f"{nom} refusé (contenu inattendu). Rien n'est écrit.")
    return f"{len(contenu) / 1e3:.0f} ko"


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge les Données climatologiques dans data/raw/climatologie/.")
    parser.add_argument("--departement", default="21", help="code du département (défaut : 21, Côte-d'Or)")
    parser.add_argument("--force", action="store_true", help="retélécharge les fichiers déjà présents")
    args = parser.parse_args()

    liens = lister_fichiers(args.departement)
    DOSSIER.mkdir(parents=True, exist_ok=True)
    for url in liens:
        fichier = DOSSIER / url.rsplit("/", 1)[-1]
        if fichier.exists() and not args.force:
            print(f"{fichier.name} : déjà présent, ignoré")
            continue

        # Écrit d'abord un fichier temporaire, contrôlé, puis le renomme : un
        # téléchargement interrompu ou abîmé ne remplace jamais le bon fichier.
        temporaire = fichier.with_name(fichier.name + ".tmp")
        try:
            telecharger(url, temporaire)
            if fichier.name.endswith(".csv.gz"):
                resume = verifier_mesures(temporaire, args.departement)
            else:
                resume = verifier_descriptif(temporaire, fichier.name)
        except Exception:
            temporaire.unlink(missing_ok=True)
            raise
        temporaire.replace(fichier)
        print(f"{fichier.name} : {resume}")
        time.sleep(1)  # une requête par seconde au plus, pour ménager le serveur

    # Quand Météo-France change les périodes, les anciens fichiers restent dans le
    # dossier : on les signale (ils feraient des doublons de dates), sans les supprimer.
    attendus = {url.rsplit("/", 1)[-1] for url in liens}
    anciens = sorted(f.name for f in DOSSIER.glob(f"Q_{args.departement}_*.csv.gz") if f.name not in attendus)
    for nom in anciens:
        print(f"Attention : {nom} n'est plus au catalogue (ancienne période). À supprimer à la main.")
    print(f"Terminé : {len(liens)} fichiers dans {DOSSIER}")


if __name__ == "__main__":
    main()
