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

**Run:**
```bash
cd imdb
pip install -r requirements.txt
python pipeline.py
```

### 2. Password Generator (`password-generator/`)
A secure password generation tool with built-in validation.

**Features:**
- Generates strong, random passwords
- Validates passwords for security requirements
- Generates passwords iteratively until all criteria are met

**Run:**
```bash
cd password-generator
python main.py
```

## Getting Started

### Prerequisites
- Python 3.8+ (each project may specify a version in `.python-version`)
- pip for package management
- pyenv recommended for version management

### Adding New Projects
1. Create a new directory for your project
2. Include a clear README.md with setup and usage instructions
3. Add any required dependencies and configuration files
4. Update this main README to include your new project

## Structure
```
├── imdb/                 # IMDb data processing pipeline
├── password-generator/   # Secure password generation tool
└── README.md            # This file
