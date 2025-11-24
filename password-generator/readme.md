# Générateur de Mot de Passe

## Description

Ce projet est un générateur de mot de passe simple en Python. Il génère des mots de passe aléatoires d'une longueur de 8 caractères, composés de caractères imprimables (ASCII 33-126), et valide qu'ils contiennent au moins :
- 2 chiffres
- 2 lettres minuscules
- 2 lettres majuscules
- 2 caractères de ponctuation

Le programme continue de générer des mots de passe jusqu'à ce qu'il trouve un qui satisfait toutes ces conditions de validation.

L'objectif de ce projet était de pratiquer le TDD, les expréssions régulières et découvrir la bibliothèque Pytest.

## Prérequis

- Python 3.x

## Installation

Clonez ce dépôt ou téléchargez les fichiers dans un répertoire local.

## Utilisation

Exécutez le script principal :

```bash
python main.py
```

Le programme générera et affichera un mot de passe valide.

## Tests

Des tests unitaires sont disponibles pour les composants générateur et validateur :

```bash
python test_generator.py
python test_validator.py
```

## Structure du Projet

- `generator.py` : Fonction pour générer un mot de passe aléatoire.
- `validator.py` : Fonctions de validation pour différents critères (chiffres, majuscules, minuscules, ponctuation).
- `main.py` : Script principal qui génère et valide un mot de passe.
- `test_generator.py` : Tests pour le générateur.
- `test_validator.py` : Tests pour le validateur.

## Licence

