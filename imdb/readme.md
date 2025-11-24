# Projet Pipeline ETL pour les Données IMDb

Ce projet implémente un pipeline ETL (Extract, Transform, Load) complet pour le traitement et l'analyse des données de films IMDb. Il transforme des données brutes en ensembles de données propres et analysés, prêts pour l'exploitation et les requêtes.

## Architecture du Pipeline

### 1. Extraction et Validation (Scripts/extract.py)
- **Chargement des données** : Import des fichiers CSV bruts depuis `Data/raw/`
- **Nettoyage initial** : Conversion des colonnes gross et runtime (suppression des formats texte)
- **Validation des données** :
  - Vérification du schéma (colonnes attendues)
  - Validation des types de données
  - Contrôle des plages de valeurs (années, notes, scores)
  - Vérification de l'unicité (Titre et année de sortie du film)
  - Contrôle des valeurs positives/négatives
  - Détection des valeurs nulles

### 2. Transformation (Scripts/transform.py)
- **Ajout de colonnes dérivées** :
  - Colonne `Decade` : Groupe les films par décennie
  - Colonne `Rating` : Moyenne pondérée des notes IMDb et Metacritic
- **Création de nouveaux DataFrames** :
  - Explosion des genres pour l'analyse par genre
  - Fusion des colonnes d'acteurs pour l'analyse par acteur

### 3. Chargement (pipeline.py)
- Sauvegarde des données nettoyées dans `Data/cleaned/`
- Génération de plusieurs vues :
  - `cleaned_imdb.csv` : Données principales transformées
  - `cleaned_imdb_genres.csv` : Films explosés par genre
  - `cleaned_imdb_actors.csv` : Données sur les acteurs

### 4. Logging (Scripts/log.py)
- Journalisation complète de toutes les étapes du pipeline
- Logs enregistrés dans `Logs/pipeline_{dd_mm_yyyy}.log` (avec la date actuelle au format dd_mm_yyyy)
- Niveaux d'erreur pour identifier les problèmes de données

## Structure du Projet

```
/imdb/
├── Data/
│   ├── raw/
│   │   └── imdb_top_1000.csv
│   └── cleaned/  # Généré par le pipeline
├── Logs/         # Logs du pipeline
├── Scripts/
│   ├── extract.py    # Extraction et validation
│   ├── transform.py  # Transformations
│   └── log.py        # Fonctions de logging
├── pipeline.py       # Script principal d'exécution
├── requirements.txt  # Dépendances Python
├── .python-version   # Version pyenv
└── project.md        # Ce fichier
```

## Installation et Utilisation

1. **Environnement** : Le projet utilise pyenv pour gérer les versions Python
2. **Installation des dépendances** :
   ```
   pip install -r requirements.txt
   ```
3. **Exécution du pipeline** :
   ```
   python pipeline.py
   ```

## Données Traitées

- **Source** : `imdb_top_1000.csv` (1000 films du top IMDb)
- **Colonnes principales** : Titre, Année, Genre, Notes, Directeur, Acteurs, Recettes, etc.
- **Sorties** : Données nettoyées et analyses prêtes pour dashboard ou requêtes

## Technologies Utilisées

- **Python** avec pyenv pour la gestion des versions
- **Pandas** et **NumPy** pour le traitement des données
- **Logging** Python pour le suivi des opérations
