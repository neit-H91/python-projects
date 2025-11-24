# Configuration for the effectifs terminal pipeline

# Data directory
DATA_DIR = "data"

# Raw data path pattern
RAW_DATA_PATTERN = f"{DATA_DIR}/effectifs_*.csv"

# Processed data path
PROCESSED_DATA_DIR = f"{DATA_DIR}/processed"

# Years to process
YEARS = [2020, 2021, 2022, 2023, 2024]

# Spark configuration
SPARK_APP_NAME = "effectifsRentreeStarSchema"
SPARK_SHUFFLE_PARTITIONS = "4"

# Unwanted columns for extracting specialties
UNWANTED_COLS = [
    'Rentrée scolaire',
    'Code région académique',
    'Région académique',
    'Code académie',
    'Académie',
    'Code département',
    'Département',
    'Code commune',
    'Commune',
    'UAI',
    'Dénomination principale',
    'Patronyme',
    'Secteur',
    'Effectif total',
    'Effectif total garçons',
    'Effectif total filles',
    'AUTRES COMBINAISONS - filles',
    'AUTRES COMBINAISONS - garcons',
    'code_region_insee'
]
