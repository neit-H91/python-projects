# Data Warehouse Star Schema - Corrected Hierarchy

## Overview
The warehouse uses a hybrid approach where facts reference UAI directly, and the lycée dimension provides all hierarchical information.

```
fact_total_enrollment
├── uai (DIRECT FK to school)
├── rentree (school year)
├── genre_id (FK to dim_genre)
└── effectif_total (measure)

fact_speciality_enrollment
├── uai (DIRECT FK to school)
├── rentree (school year)
├── speciality_id (FK to dim_speciality)
├── genre_id (FK to dim_genre)
└── effectif (measure)
```

## Dimension Relationships

```
dim_lycee (School Dimension - UAI as PK)
├── uai (PK)
├── denomination_principale
├── secteur
├── code_region_academie (FK to dim_regionaca.code_region_academie)
├── code_academie (FK to dim_academie.code_academie)
├── code_departement (FK to dim_departement.code_departement)
└── code_commune (FK to dim_commune.code_commune)

dim_commune (Municipality - code_commune as PK)
├── code_commune (PK)
├── commune_name
└── code_departement (FK to dim_departement.code_departement)

dim_departement (Department - code_departement as PK)
├── code_departement (PK)
└── departement_name

dim_academie (Academy - code_academie as PK)
├── code_academie (PK)
└── academie_name

dim_regionaca (Region - code_region_academie as PK)
├── code_region_academie (PK)
├── region_academie_name
└── code_region_insee
```

## Query Pattern
To query school-level enrollments with demographics:
```
fact_total_enrollment f
JOIN dim_lycee l ON f.uai = l.uai
JOIN dim_departement d ON l.code_departement = d.code_departement
JOIN dim_commune c ON l.code_commune = c.code_commune AND c.code_departement = d.code_departement
JOIN dim_regionaca r ON l.code_region_academie = r.code_region_academie
JOIN dim_academie a ON l.code_academie = a.code_academie
JOIN dim_genre g ON f.genre_id = g.genre_id
```
