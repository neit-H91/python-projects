# Effectifs Terminale Pipeline

A PySpark-based data pipeline for processing French high school (terminale générale) enrollment data into a star schema for analytics.

## Overview

This project transforms raw enrollment data from the French Ministry of Education's open data platform into a structured star schema suitable for business intelligence and analytical queries. The pipeline downloads CSV files from the API, processes them using Apache Spark, and creates dimension and fact tables stored in Parquet format.

## Project Structure

```
effectifs-terminal/
├── src/
│   ├── __init__.py
│   └── pipeline.py          # Main pipeline script
├── config/
│   └── config.py            # Configuration settings
├── data/
│   └── processed/           # Output Parquet tables (created after run)
│       ├── dim_speciality/
│       ├── dim_departement/
│       ├── dim_regionaca/
│       ├── dim_secteur/
│       ├── dim_rentree/
│       ├── dim_genre/
│       ├── fact_speciality_enrollment/
│       └── fact_total_enrollment/
├── tests/
│   # Test files (to be implemented)
├── requirements.txt
└── README.md
```

## Features

- **Data Download**: Automatically downloads CSV data for specified school years from the French education API
- **Spark Processing**: Uses PySpark for efficient distributed data processing
- **Star Schema Creation**:
  - Dimension tables: Speciality, Department, Academic Region, Sector, Time (School Year)
  - Fact table: Enrollment totals per school with dimension references
- **Error Handling**: Robust error handling for download failures
- **Configurable**: Easily adjustable parameters via config file

## Prerequisites

- Python 3.8+
- Apache Spark 3.x (PySpark 3.5.0 recommended)
- Internet connection for data download (or pre-downloaded CSV files)

## Installation

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Configure the pipeline in `config/config.py` (optional - defaults are provided)
2. Run the pipeline:
   ```bash
   python src/pipeline.py
   ```

The pipeline will:
- Download data if not already present in `data/` directory
- Process CSV files using PySpark
- Create and save dimension and fact tables in `data/processed/`

## Configuration

Edit `config/config.py` to customize:

- `YEARS`: List of school years to process
- `DATA_DIR`: Directory for raw CSV files
- `PROCESSED_DATA_DIR`: Output directory for processed Parquet files
- Spark configuration parameters

## Data Source

Data is sourced from: https://data.education.gouv.fr/explore/dataset/fr-en-effectifs-specialites-doublettes-terminale-generale/

Contains enrollment figures by specialty, gender, and school for French général terminals (high school seniors in general track).

## Tables Created

### Dimension Tables
- **dim_speciality**: Academic specialties (e.g., Mathematics, Physics-Chemistry)
- **dim_regionaca**: Academic regions (with INSEE codes)
- **dim_academie**: Academic authorities (NEW - académies)
- **dim_departement**: French departments
- **dim_commune**: Municipalities (communes) - linked to departments
- **dim_secteur**: School sector (public/private)
- **dim_lycee**: Schools (lycées) - contains all geographical FKs directly
- **dim_rentree**: School years (rentrée scolaire)
- **dim_genre**: Gender dimension (boys/girls)

### Fact Tables
- **fact_speciality_enrollment**: Enrollment by gender, school year, speciality, school (UAI)
- **fact_total_enrollment**: Total enrollment by gender, school year, school (UAI)

### Data Warehouse Hierarchy
The warehouse uses this lookup structure:
- **fact_total** → UAI → **dim_lycee** → secteur, region, acadé mie, département
- **fact_total** → département (from dim_lycee) → **dim_commune** → communes

## Output Format

All tables are saved in Apache Parquet format for efficient querying with tools like Apache Spark, Presto, or Dremio.

## Error Handling

- Continues processing even if individual year downloads fail
- Logs errors for failed operations
- Validates data structure before processing

## Testing

Currently includes basic structure for testing. Add unit tests in the `tests/` directory.

## Notes

- Large datasets possible; ensure sufficient disk space
- Spark session configured for local processing; adjust for cluster deployment
- Fact table is simplified; consider adding proper joins for full star schema with foreign keys

## License
