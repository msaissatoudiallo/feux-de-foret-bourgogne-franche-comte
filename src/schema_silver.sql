-- Schéma de l'entrepôt v0 : couche silver (ticket #41)
-- Description complète : docs/schema-entrepot.md
--
-- Les tables sont créées dans l'ordre des dépendances : d'abord les
-- dimensions, puis les faits qui pointent vers elles. Les scripts de
-- chargement remplissent ensuite ces tables depuis data/raw/ (couche bronze).
-- Périmètre : France métropolitaine (96 départements), outre-mer exclu (D022).

-- ---------------------------------------------------------------------------
-- Dimensions
-- ---------------------------------------------------------------------------

-- Un jour, du 1997-01-01 au 2026-12-31 (calculée, sans source externe).
CREATE TABLE dim_date (
    date            DATE PRIMARY KEY,
    annee           SMALLINT NOT NULL,
    mois            TINYINT  NOT NULL CHECK (mois BETWEEN 1 AND 12),
    jour_semaine    TINYINT  NOT NULL CHECK (jour_semaine BETWEEN 1 AND 7), -- 1 = lundi
    est_weekend     BOOLEAN  NOT NULL,
    est_ferie       BOOLEAN  NOT NULL,           -- 11 jours fériés calculés par règle (H7)
    nom_ferie       VARCHAR,                     -- vide si le jour n'est pas férié
    est_ete         BOOLEAN  NOT NULL            -- juin à septembre (H4, H9)
);

-- Un département de France métropolitaine (Admin Express).
CREATE TABLE dim_departement (
    code_departement VARCHAR PRIMARY KEY CHECK (length(code_departement) = 2), -- '01', '21', '2A'
    nom              VARCHAR NOT NULL,
    code_region      VARCHAR NOT NULL,
    est_bfc          BOOLEAN NOT NULL            -- Bourgogne-Franche-Comté (code région 27)
);

-- Une commune de France métropolitaine, édition la plus récente d'Admin Express (D023).
CREATE TABLE dim_commune (
    code_insee        VARCHAR PRIMARY KEY CHECK (length(code_insee) = 5),
    nom               VARCHAR NOT NULL,
    code_departement  VARCHAR NOT NULL REFERENCES dim_departement (code_departement),
    population        INTEGER,
    surface_km2       DOUBLE  NOT NULL,          -- calculée depuis le contour, en Lambert 93
    surface_foret_km2 DOUBLE,                    -- BD Forêt V2 : Côte-d'Or seulement, vide ailleurs
    part_foret        DOUBLE CHECK (part_foret BETWEEN 0 AND 1)
);

-- Un ancien code de commune, disparu après une fusion, et son code actuel.
CREATE TABLE passage_commune (
    code_insee_ancien VARCHAR PRIMARY KEY CHECK (length(code_insee_ancien) = 5),
    code_insee_actuel VARCHAR NOT NULL REFERENCES dim_commune (code_insee)
);

-- Une maille de 0,25° de l'IFM (Copernicus EWDS).
CREATE TABLE dim_maille (
    id_maille        VARCHAR PRIMARY KEY,        -- latitude_longitude du centre, ex. '47.25_5.00'
    latitude         DOUBLE  NOT NULL,
    longitude        DOUBLE  NOT NULL,
    code_departement VARCHAR REFERENCES dim_departement (code_departement) -- département du centre ; vide en mer ou hors de France
);

-- Une station météo de Météo-France (Données climatologiques).
CREATE TABLE dim_station (
    num_poste        VARCHAR PRIMARY KEY CHECK (length(num_poste) = 8),
    nom              VARCHAR NOT NULL,
    latitude         DOUBLE  NOT NULL,
    longitude        DOUBLE  NOT NULL,
    altitude_m       INTEGER,
    code_departement VARCHAR NOT NULL REFERENCES dim_departement (code_departement),
    code_insee       VARCHAR REFERENCES dim_commune (code_insee) -- commune qui contient la station
);

-- ---------------------------------------------------------------------------
-- Faits
-- ---------------------------------------------------------------------------

-- Un feu de forêt (BDIFF).
CREATE TABLE fait_feu (
    id_feu               VARCHAR  PRIMARY KEY,  -- 'AAAA-numéro' : le numéro seul n'est pas unique
    annee                SMALLINT NOT NULL,
    numero               INTEGER  NOT NULL,
    date_alerte          DATE     NOT NULL REFERENCES dim_date (date),
    heure_alerte         TIME     NOT NULL,     -- 00:00 pour 135 feux : heure peut-être non saisie
    code_insee_bdiff     VARCHAR  NOT NULL,     -- code tel qu'écrit dans la BDIFF
    code_insee           VARCHAR  NOT NULL REFERENCES dim_commune (code_insee), -- code actuel (passage_commune)
    code_departement     VARCHAR  NOT NULL REFERENCES dim_departement (code_departement),
    surface_parcourue_m2 BIGINT   NOT NULL CHECK (surface_parcourue_m2 > 0),
    surface_foret_m2     BIGINT,
    precision_surfaces   VARCHAR CHECK (precision_surfaces IN ('Estimées', 'Mesurées')),
    nature               VARCHAR,               -- cause du feu ; vide pour 100 feux sur 120 en Côte-d'Or
    ancien_formulaire    BOOLEAN  NOT NULL,     -- feux de 2022 et avant : définitions des surfaces différentes
    UNIQUE (annee, numero)
);

-- Une maille pour un jour : valeur de l'IFM (Copernicus EWDS, variable fwinx).
CREATE TABLE fait_ifm_jour (
    id_maille VARCHAR NOT NULL REFERENCES dim_maille (id_maille),
    date      DATE    NOT NULL REFERENCES dim_date (date),
    ifm       DOUBLE  NOT NULL CHECK (ifm >= 0),
    PRIMARY KEY (id_maille, date)
);

-- Un département pour le jour visé par le bulletin de la veille (Météo des forêts).
-- date = date du bulletin (convertie de UTC en heure française) + 1 jour,
-- niveau = niveau_j1 de ce bulletin (D008). Le décalage est fait ici, une fois.
CREATE TABLE fait_mdf_jour (
    code_departement VARCHAR NOT NULL REFERENCES dim_departement (code_departement),
    date             DATE    NOT NULL REFERENCES dim_date (date),
    date_bulletin    DATE    NOT NULL,
    niveau           TINYINT NOT NULL CHECK (niveau BETWEEN 1 AND 4),
    PRIMARY KEY (code_departement, date),
    CHECK (date = date_bulletin + 1)
);

-- Une station pour un jour : météo mesurée (Données climatologiques).
-- Valeurs déjà en °C, mm, m/s et % dans les fichiers (pas en dixièmes).
-- La pluie du jour J est mesurée de J 6 h à J+1 6 h (UTC).
CREATE TABLE fait_meteo_jour (
    num_poste VARCHAR NOT NULL REFERENCES dim_station (num_poste),
    date      DATE    NOT NULL REFERENCES dim_date (date),
    rr_mm     DOUBLE CHECK (rr_mm >= 0),         -- pluie
    tx_c      DOUBLE,                            -- température maximale
    tn_c      DOUBLE,                            -- température minimale
    ffm_ms    DOUBLE CHECK (ffm_ms >= 0),        -- vent moyen
    un_pct    DOUBLE CHECK (un_pct BETWEEN 0 AND 100), -- humidité minimale
    q_rr      TINYINT,                           -- codes qualité de Météo-France (0, 1, 9, 2)
    q_tx      TINYINT,
    q_tn      TINYINT,
    q_ffm     TINYINT,
    q_un      TINYINT,
    PRIMARY KEY (num_poste, date)
);
