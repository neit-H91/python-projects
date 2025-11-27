# Python Projects Collection

This repository serves as a centralized collection of small, standalone Python projects. Each project is organized in its own directory and demonstrates various programming concepts, data processing techniques, and practical applications using Python.

## Projects Overview

### 1. IMDb Data Pipeline (`imdb/`)
An ETL (Extract, Transform, Load) pipeline for processing and analyzing IMDb movie data.

**Features:**
- Data extraction and validation from CSV sources
- Data transformation including decade grouping and rating calculations
- Creation of analysis-ready datasets (movies, genres, actors)
- Comprehensive logging throughout the pipeline

**Key Technologies:** Pandas, NumPy, Python Logging

### 2. Password Generator (`password-generator/`)
A secure password generation tool with built-in validation.

**Features:**
- Generates strong, random passwords
- Validates passwords for security requirements
- Generates passwords iteratively until all criteria are met

### 3. Effectifs Terminale Pipeline (`effectifs-terminal/`)
A PySpark-based data pipeline for processing French high school enrollment data into a star schema for analytics.

**Features:**
- Downloads and processes enrollment data from French Ministry of Education API
- Creates star schema with dimension and fact tables (Parquet format)
- Handles large datasets with distributed processing via Apache Spark
- Configurable for different school years and processing parameters

**Key Technologies:** PySpark, Pandas, Apache Parquet

### 4. Veterinary Clinic Management System (`vetapp/`)
A Django-based web application for managing veterinary clinic operations.

**Features:**
- Animal and owner management with detailed records
- Appointment scheduling and tracking
- Medicine inventory and prescription management
- Weight tracking for animals over time
- Dashboard views for clinic operations

**Key Technologies:** Django, SQLite, HTML/CSS

## Structure
```
├── imdb/                 # IMDb data processing pipeline
├── password-generator/   # Secure password generation tool
├── effectifs-terminal/   # French education data pipeline
├── vetapp/               # Veterinary clinic management system
└── README.md            # This file
