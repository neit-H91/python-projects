# 🔐 Générateur et Validateur de Mots de Passe

Ce projet propose un **générateur de mots de passe aléatoires** ainsi qu’un **système de validation avancé** basé sur des expressions régulières.  
Un mot de passe est généré en continu jusqu’à ce qu’il respecte **toutes les règles de sécurité définies**.

---

## 📁 Structure du projet

├── generator.py
├── validator.py
├── main.py
├── test_generator.py
└── test_validator.py


---

## 🚀 Fonctionnalités

### 1. Génération de mots de passe
Le module `generator.py` crée un mot de passe de **8 caractères**, chacun étant un caractère ASCII imprimable (codes 33 à 126).  
Le mot de passe est donc totalement aléatoire, sans règle prédéfinie autre que sa longueur et son type de caractères.

### 2. Validation stricte du mot de passe
Le module `validator.py` valide les mots de passe en imposant la présence **exacte** des éléments suivants :

| Type de caractère | Quantité attendue |
|-------------------|-------------------|
| Chiffres (0–9) | **exactement 2** |
| Lettres minuscules (a–z) | **exactement 2** |
| Lettres majuscules (A–Z) | **exactement 2** |
| Ponctuation ASCII | **exactement 2** |

Les expressions régulières définies permettent de vérifier précisément ces quantités.

Le mot de passe doit donc contenir **8 caractères** au total, répartis comme suit :  
**2 chiffres + 2 minuscules + 2 majuscules + 2 ponctuations**.

### 3. Génération jusqu'à validation
Le fichier `main.py` génère successivement des mots de passe jusqu’à en produire un qui respecte *toutes* les contraintes.

Une fois obtenu, il est affiché à l’utilisateur.

---

## 🧪 Tests unitaires

Le projet comprend une série de tests (`pytest`) afin de garantir :

### ✔️ Pour le générateur :
- Longueur toujours égale à 8
- Caractères dans la plage ASCII autorisée
- Comportement déterministe lors du mock de `random.randint`

### ✔️ Pour les validateurs :
- Exactitude des règles (acceptation uniquement de 2 caractères du type attendu)
- Gestion correcte des cas limites

Ces tests assurent la fiabilité et la robustesse du système.

---

## ▶️ Utilisation

### Exécution simple :

```bash
python main.py

# Exemple de sortie :
votre nouveau mot de passe est :  "7kzX4'X
```
### 🎯 Objectif du projet

Ce projet peut servir :

d’exercice sur les expressions régulières avancées

de démonstration de tests unitaires

d'exemple de séparation logique entre génération, validation et exécution

d’introduction à la gestion de flux génératifs (via iter() et next())

Bien qu’il ne soit pas destiné à un usage de sécurité en production, il illustre clairement un pipeline complet de génération/validation.