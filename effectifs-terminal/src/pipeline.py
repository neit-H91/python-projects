#!/usr/bin/env python3
"""
Main pipeline for processing French education enrollment data (effectifs terminale)
into a star schema using PySpark.
"""

import os
import sys
import requests
from pathlib import Path

# Add parent directory to path for config import
sys.path.append(str(Path(__file__).parent.parent))

from config import config
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id


def download_data(years, data_dir):
    """Download CSV data from the French education API."""
    # Based on user's working code
    urls = [
        f"https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-effectifs-specialites-doublettes-terminale-generale/exports/csv?lang=fr&refine=rentree_scolaire%3A%22{y}%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
        for y in years
    ]

    for year, url in zip(years, urls):
        try:
            response = requests.get(url)
            response.raise_for_status() # Lève une exception pour les codes d'état d'erreur (4xx ou 5xx)

            filename = os.path.join(data_dir, f"effectifs_{year}.csv")

            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Téléchargé et sauvegardé sur folder : {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du téléchargement pour l'année {year}: {e}")
        except IOError as e:
            print(f"Erreur lors de l'écriture du fichier pour l'année {year}: {e}")


def create_spark_session():
    """Create and configure Spark session."""
    return (
        SparkSession.builder
        .appName(config.SPARK_APP_NAME)
        .config("spark.sql.shuffle.partitions", config.SPARK_SHUFFLE_PARTITIONS)
        .getOrCreate()
    )


def load_data_raw(spark):
    """Load raw CSV data into Spark DataFrame."""
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .option("encoding", "utf-8")
        .load(config.RAW_DATA_PATTERN)
    )


def create_speciality_dimension(data_csv):
    """Create the speciality dimension table."""
    # Get specialty columns
    spe_cols = [
        col for col in data_csv.columns
        if col not in config.UNWANTED_COLS
    ]

    # Create list of dicts for speciality dim
    speciality_data = []
    for col in spe_cols:
        parts = col.split(' - ', 1)
        if len(parts) >= 2:
            speciality_data.append({"id": parts[0], "name": parts[1]})

    speciality_temp_df = data_csv.sparkSession.createDataFrame(speciality_data)
    speciality_dim = speciality_temp_df.distinct().withColumnRenamed("id", "speciality_id")

    print("Speciality dimension created")
    speciality_dim.show(speciality_dim.count(), truncate=False)

    return speciality_dim


def create_geographic_dimensions(data_csv):
    """Create geographic and administrative dimension tables."""

    # Academic region dimension (Code région académique as PK)
    dim_regionaca = (
        data_csv.select(
            "Code région académique",
            "Région académique",
            "code_region_insee"
        )
        .distinct()
        .withColumnRenamed("Code région académique", "code_region_academie")
        .withColumnRenamed("Région académique", "region_academie_name")
    )

    print("Academic Region dimension:")
    dim_regionaca.show(truncate=False)

    # Académie (academic authority) dimension (Code académie as PK)
    dim_academie = (
        data_csv.select("Code académie", "Académie").distinct()
        .withColumnRenamed("Code académie", "code_academie")
        .withColumnRenamed("Académie", "academie_name")
    )

    print("Académie dimension:")
    dim_academie.show(truncate=False)

    # Department dimension (Code département as PK)
    dim_departement = (
        data_csv.select("Code département", "Département").distinct()
        .withColumnRenamed("Code département", "code_departement")
        .withColumnRenamed("Département", "departement_name")
    )

    print("Department dimension:")
    dim_departement.show(truncate=False)

    # Commune dimension (Code commune as PK, with FK to department)
    dim_commune = (
        data_csv.select("Code commune", "Commune", "Code département").distinct()
        .withColumnRenamed("Code commune", "code_commune")
        .withColumnRenamed("Commune", "commune_name")
        .withColumnRenamed("Code département", "code_departement")
    )

    print("Commune dimension:")
    dim_commune.show(truncate=False)

    return dim_regionaca, dim_academie, dim_departement, dim_commune


def create_lycee_dimension(data_csv):
    """Create établissement (school/lycée) dimension table with UAI as PK."""
    dim_lycee = (
        data_csv.select(
            "UAI",
            "Dénomination principale",
            "Secteur",
            "Code région académique",
            "Code académie",
            "Code département",
            "Code commune"
        ).distinct()
        .withColumnRenamed("UAI", "uai")
        .withColumnRenamed("Dénomination principale", "denomination_principale")
        .withColumnRenamed("Secteur", "secteur")
        .withColumnRenamed("Code région académique", "code_region_academie")
        .withColumnRenamed("Code académie", "code_academie")
        .withColumnRenamed("Code département", "code_departement")
        .withColumnRenamed("Code commune", "code_commune")
    )

    print("Lycée (School) dimension:")
    dim_lycee.show(10, truncate=False)

    return dim_lycee


def create_time_dimension(data_csv):
    """Create time (school year) dimension."""
    dim_rentree = (
        data_csv.select("Rentrée scolaire").distinct()
        .withColumn("rentree_id", monotonically_increasing_id())
        .select("rentree_id", "Rentrée scolaire")
        .withColumnRenamed("Rentrée scolaire", "rentree_year")
    )

    print("Time (School year) dimension:")
    dim_rentree.show(truncate=False)

    return dim_rentree


def create_genre_dimension(data_csv):
    """Create genre (gender) dimension."""
    genre_data = [{"genre_id": 0, "genre_name": "total"},
                  {"genre_id": 1, "genre_name": "garçons"},
                  {"genre_id": 2, "genre_name": "filles"}]

    dim_genre = data_csv.sparkSession.createDataFrame(genre_data)

    print("Genre (Gender) dimension:")
    dim_genre.show()

    return dim_genre


def create_speciality_facts(data_csv):
    """Create facts table for speciality-level enrollments."""
    # Get specialty columns
    spe_cols = [
        col for col in data_csv.columns
        if col not in config.UNWANTED_COLS
    ]

    # Unpivot specialty columns into facts
    facts_data = []

    # Collect required base columns
    data_list = data_csv.select("UAI", "Rentrée scolaire").collect()

    for row in data_list[:10]:  # Limit for demo, remove [:10] for full processing
        uai = row["UAI"]
        rentree = row["Rentrée scolaire"]

        for col in spe_cols:
            if col in data_csv.columns:
                value = data_csv.filter(f"UAI = '{uai}' AND `Rentrée scolaire` = '{rentree}'").select(col).first()[0]
                if value and value > 0:
                    parts = col.split(' - ')
                    if len(parts) >= 3:
                        speciality_id = parts[0]
                        genre = parts[2]  # filles or garçons
                        genre_id = 1 if genre == "garçons" else 2

                        facts_data.append({
                            "uai": uai,
                            "rentree": rentree,
                            "speciality_id": speciality_id,
                            "genre_id": genre_id,
                            "effectif": int(value)
                        })

    fact_spe_df = data_csv.sparkSession.createDataFrame(facts_data)
    print("Speciality facts table:")
    fact_spe_df.show(20, truncate=False)

    return fact_spe_df


def create_total_facts(data_csv):
    """Create facts table for total enrollments per school-year-gender."""
    # Create fact table: total - genre - year - code_uai (lycee)
    # Using UAI as business key directly, can lookup hierarchy from lycee dim
    fact_total_data = []

    data_list = data_csv.select("UAI", "Rentrée scolaire", "Effectif total", "Effectif total garçons", "Effectif total filles").collect()

    for row in data_list:
        uai = row["UAI"]
        rentree = row["Rentrée scolaire"]

        # Overall total (genre_id = 0)
        fact_total_data.append({
            "uai": uai,
            "rentree": rentree,
            "genre_id": 0,  # 0 for total
            "effectif_total": int(row["Effectif total"]) if row["Effectif total"] else 0
        })

        # Boys total
        fact_total_data.append({
            "uai": uai,
            "rentree": rentree,
            "genre_id": 1,
            "effectif_total": int(row["Effectif total garçons"]) if row["Effectif total garçons"] else 0
        })

        # Girls total
        fact_total_data.append({
            "uai": uai,
            "rentree": rentree,
            "genre_id": 2,
            "effectif_total": int(row["Effectif total filles"]) if row["Effectif total filles"] else 0
        })

    fact_total_df = data_csv.sparkSession.createDataFrame(fact_total_data)
    print("Total facts table (using UAI as school FK):")
    fact_total_df.show(10, truncate=False)

    return fact_total_df


def save_dims_to_parquet(speciality_dim, dim_regionaca, dim_academie, dim_departement,
                         dim_commune, dim_lycee, dim_rentree, dim_genre,
                         fact_spe, fact_total):
    """Save dimension and fact tables to Parquet format."""
    os.makedirs(config.PROCESSED_DATA_DIR, exist_ok=True)

    speciality_dim.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_speciality"
    )
    dim_regionaca.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_regionaca"
    )
    dim_academie.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_academie"
    )
    dim_departement.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_departement"
    )
    dim_commune.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_commune"
    )
    dim_lycee.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_lycee"
    )
    dim_rentree.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_rentree"
    )
    dim_genre.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/dim_genre"
    )
    fact_spe.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/fact_speciality_enrollment"
    )
    fact_total.write.mode("overwrite").parquet(
        f"{config.PROCESSED_DATA_DIR}/fact_total_enrollment"
    )

    print("All tables saved to Parquet format in data/processed/")


def main():
    """Main pipeline execution."""
    print("Starting Effectifs Terminale Pipeline...")

    # Check if data directory exists and download if needed
    if not os.path.exists(config.DATA_DIR) or not list(Path(config.DATA_DIR).glob("effectifs_*.csv")):
        print(f"No data found in {config.DATA_DIR}, downloading...")
        download_data(config.YEARS, config.DATA_DIR)
    else:
        print("Data already exists, skipping download.")

    # Create Spark session
    spark = create_spark_session()

    # Load data
    data_csv = load_data_raw(spark)
    print(f"Loaded data with {data_csv.count()} rows and {len(data_csv.columns)} columns")

    # Create dimensions
    speciality_dim = create_speciality_dimension(data_csv)
    dim_regionaca, dim_academie, dim_departement, dim_commune = create_geographic_dimensions(data_csv)
    dim_lycee = create_lycee_dimension(data_csv)
    dim_rentree = create_time_dimension(data_csv)
    dim_genre = create_genre_dimension(data_csv)

    # Create fact tables
    fact_spe = create_speciality_facts(data_csv)
    fact_total = create_total_facts(data_csv)

    # Save all tables
    save_dims_to_parquet(
        speciality_dim, dim_regionaca, dim_academie, dim_departement,
        dim_commune, dim_lycee, dim_rentree, dim_genre,
        fact_spe, fact_total
    )

    print("Pipeline completed successfully!")

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    main()
