"""Couche bronze : téléchargement de l'IFM de Copernicus EWDS (ticket #114).

Télécharge depuis le Early Warning Data Store de Copernicus
(https://ewds.climate.copernicus.eu) l'Indice Forêt Météo (variable « Fire
weather index », réanalyse consolidée, jeu cems-fire-historical-v1, grille
0,25°, NetCDF) et dépose un fichier par zone et par année, tel quel, dans
data/raw/copernicus/ :

- zone « region » : Bourgogne-Franche-Comté, de 1996 à 2026, toute l'année
  (indicateur 2 : 30 étés ; indicateurs 3, 4 et 6 : feux de printemps). 1996 est
  pris en plus pour pouvoir compter 30 étés complets sur 1996-2025 (D025) ;
- zone « france » : France métropolitaine, de 2015 à 2025, toute l'année
  (indicateur 3 : comparaison Côte-d'Or, région, France).

Les deux zones se recouvrent sur 2015-2025 : en silver, il ne faut pas les
empiler (doublons de mailles).

- La clé personnelle du compte Copernicus est lue dans le fichier .env, à la
  racine du dépôt (COPERNICUS_EWDS_CLE=...). Ce fichier est hors de Git.
- Les jours disponibles sont lus dans le catalogue : la réanalyse consolidée
  a quelques mois de retard (2026 incomplète). Le script ne demande que ces jours.
- Le fichier reçu est contrôlé : NetCDF lisible, variable fwinx présente, un
  pas de temps par jour demandé, valeurs positives. Sinon, rien n'est écrit.
- Idempotent : une année déjà téléchargée n'est pas redemandée. L'option
  --force la remplace (utile pour compléter 2026 plus tard).

Utilisation (environnement activé, depuis la racine du dépôt) :
    python src/charger_copernicus.py                          # les deux zones
    python src/charger_copernicus.py --zone region --debut 2024 --fin 2024
    python src/charger_copernicus.py --zone region --debut 2026 --force
"""

import argparse
import datetime as dt
import os
from pathlib import Path

import cdsapi
import requests
import xarray as xr

RACINE = Path(__file__).resolve().parent.parent
DOSSIER = RACINE / "data" / "raw" / "copernicus"
FICHIER_ENV = RACINE / ".env"

API = "https://ewds.climate.copernicus.eu/api"
JEU = "cems-fire-historical-v1"
VARIABLE = "fire_weather_index"  # s'appelle fwinx dans le fichier NetCDF
TYPE = "consolidated_dataset"    # réanalyse consolidée (pas la version intermédiaire)

# Zone demandée : [nord, ouest, sud, est], en degrés, avec une marge d'une maille.
ZONES = {
    "region": {"emprise": [48.5, 2.75, 46.0, 7.25], "debut": 1996, "fin": 2026},  # Bourgogne-Franche-Comté
    "france": {"emprise": [51.25, -5.25, 41.25, 9.75], "debut": 2015, "fin": 2025},  # métropole et Corse
}


def lire_cle() -> str:
    """Lit la clé Copernicus dans .env (ou dans la variable d'environnement du même nom)."""
    if FICHIER_ENV.exists():
        for ligne in FICHIER_ENV.read_text(encoding="utf-8").splitlines():
            nom, _, valeur = ligne.partition("=")
            if nom.strip() == "COPERNICUS_EWDS_CLE" and valeur.strip():
                return valeur.strip().strip('"').strip("'")
    if os.environ.get("COPERNICUS_EWDS_CLE"):
        return os.environ["COPERNICUS_EWDS_CLE"]
    raise SystemExit(
        "Clé Copernicus introuvable. Copier .env.exemple en .env et y écrire votre clé "
        "(page « Your profile » sur ewds.climate.copernicus.eu). Voir le README."
    )


def jours_disponibles() -> set[dt.date]:
    """Lit dans le catalogue les jours qui existent en réanalyse consolidée, NetCDF, 0,25°."""
    collection = requests.get(f"{API}/catalogue/v1/collections/{JEU}", timeout=60)
    collection.raise_for_status()
    lien = next(l["href"] for l in collection.json()["links"] if l["rel"] == "constraints")
    contraintes = requests.get(lien, timeout=120)
    contraintes.raise_for_status()
    jours = set()
    for bloc in contraintes.json():
        if not (
            VARIABLE in bloc.get("variable", [])
            and "reanalysis" in bloc.get("product_type", [])
            and TYPE in bloc.get("dataset_type", [])
            and "netcdf" in bloc.get("data_format", [])
            and "0.25/0.25" in bloc.get("grid", [])
        ):
            continue
        for annee in bloc["year"]:
            for mois in bloc["month"]:
                for jour in bloc["day"]:
                    try:
                        jours.add(dt.date(int(annee), int(mois), int(jour)))
                    except ValueError:  # 31 février, etc.
                        pass
    return jours


def mois_complets(annee: int, disponibles: set[dt.date]) -> list[dt.date]:
    """Jours de l'année, en ne gardant que les mois entièrement disponibles.

    Le formulaire croise les mois et les jours demandés : un mois à moitié publié
    ferait demander des jours qui n'existent pas encore.
    """
    jours = []
    for mois in range(1, 13):
        du_mois = [dt.date(annee, mois, 1) + dt.timedelta(i) for i in range(31)]
        du_mois = [j for j in du_mois if j.month == mois]
        if all(j in disponibles for j in du_mois):
            jours += du_mois
    return jours


def demande(annee: int, jours: list[dt.date], emprise: list[float]) -> dict:
    """Demande au format du formulaire EWDS pour une année."""
    return {
        "product_type": "reanalysis",
        "variable": [VARIABLE],
        "dataset_type": TYPE,
        "system_version": ["4_1"],
        "year": [str(annee)],
        "month": sorted({f"{j.month:02d}" for j in jours}),
        "day": sorted({f"{j.day:02d}" for j in jours}),
        "grid": "0.25/0.25",
        "area": emprise,
        "data_format": "netcdf",
    }


def verifier_netcdf(chemin: Path, jours: list[dt.date]) -> str:
    """Refuse un fichier illisible, incomplet ou aux valeurs impossibles ; renvoie un résumé."""
    try:
        with xr.open_dataset(chemin) as donnees:
            if "fwinx" not in donnees:
                raise RuntimeError(f"variable fwinx absente (variables : {list(donnees.data_vars)})")
            ifm = donnees["fwinx"]
            temps = "valid_time" if "valid_time" in ifm.dims else "time"
            dates = {dt.date.fromisoformat(str(t)[:10]) for t in ifm[temps].values}
            if dates != set(jours):
                manquants = sorted(set(jours) - dates)[:3]
                raise RuntimeError(f"{len(dates)} jours reçus, {len(jours)} demandés (manquants : {manquants}…)")
            minimum, maximum = float(ifm.min()), float(ifm.max())
            if minimum < 0:
                raise RuntimeError(f"IFM négatif ({minimum})")
            mailles = ifm.sizes["latitude"] * ifm.sizes["longitude"]
    except (OSError, ValueError, KeyError, RuntimeError) as erreur:
        raise RuntimeError(f"{chemin.name} refusé ({erreur}). Rien n'est écrit.") from erreur
    return f"{len(dates)} jours, {mailles} mailles, IFM de {minimum:.1f} à {maximum:.1f}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Télécharge l'IFM de Copernicus EWDS dans data/raw/copernicus/.")
    parser.add_argument("--zone", choices=[*ZONES, "toutes"], default="toutes", help="zone à télécharger (défaut : toutes)")
    parser.add_argument("--debut", type=int, help="première année (défaut : celle de la zone)")
    parser.add_argument("--fin", type=int, help="dernière année (défaut : celle de la zone)")
    parser.add_argument("--force", action="store_true", help="redemande les années déjà présentes")
    args = parser.parse_args()

    client = cdsapi.Client(url=API, key=lire_cle(), quiet=True, progress=False)
    disponibles = jours_disponibles()
    DOSSIER.mkdir(parents=True, exist_ok=True)

    zones = ZONES if args.zone == "toutes" else {args.zone: ZONES[args.zone]}
    for nom, zone in zones.items():
        debut = max(args.debut or zone["debut"], zone["debut"])
        fin = min(args.fin or zone["fin"], zone["fin"])
        for annee in range(debut, fin + 1):
            fichier = DOSSIER / f"ifm_{nom}_{annee}.nc"
            if fichier.exists() and not args.force:
                print(f"{fichier.name} : déjà présent, ignoré")
                continue
            jours = mois_complets(annee, disponibles)
            if not jours:
                print(f"{annee} : pas encore disponible en réanalyse consolidée, ignoré")
                continue

            # Écrit d'abord un fichier temporaire, contrôlé, puis le renomme : un
            # téléchargement interrompu ou abîmé ne remplace jamais le bon fichier.
            temporaire = fichier.with_name(fichier.name + ".tmp")
            print(f"{fichier.name} : demande envoyée (file d'attente de Copernicus, souvent plusieurs minutes)…")
            try:
                client.retrieve(JEU, demande(annee, jours, zone["emprise"]), str(temporaire))
                resume = verifier_netcdf(temporaire, jours)
            except Exception:
                temporaire.unlink(missing_ok=True)
                raise
            temporaire.replace(fichier)
            incomplet = "" if len(jours) >= 365 else f" (année incomplète : jusqu'au {jours[-1]})"
            print(f"{fichier.name} : {resume}{incomplet}")

    print(f"Terminé : fichiers dans {DOSSIER}")


if __name__ == "__main__":
    main()
