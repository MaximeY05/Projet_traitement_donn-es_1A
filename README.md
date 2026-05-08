# Projet_traitement_donn-es_1A
Ce projet permet d'extraire, de transformer et d'analyser des données sportives (Basketball, Football, Tennis, Badminton, etc.) à partir de fichiers CSV. Il utilise une architecture basée sur des Adapters pour normaliser les données et des Services pour générer des analyses.

## Prérequis et installation
### Version de Python
Ce projet a été développé et testé avec Python 3.13.12

### Installation environnement
1. Cloner le dépot
Éxécutez ces commandes dans un Terminal :
    git clone [<url-du-depot>](https://github.com/MaximeY05/Projet_traitement_donn-es_1A.git)
    cd Projet_traitement_donn-es_1A

2. Créer un environnement virtuel
Éxécutez cette commande dans un Terminal :
    python3 -m venv venv

3. Activer l'environnement virtuel
Éxécutez cette commande dans un Terminal :
    Linux/macOS : source venv/bin/activate
    Windows : venv\Scripts\activate

4. Installer les dépendances
Éxécutez cette commande dans un Terminal :
    pip install -r requirements.txt

## Utilisation
Pour lancer l'application, exécutez cette commande :
    python3 main.py

## Documentation
Le code respecte le style de docstrings NumPy. Chaque classe et méthode est documentée pour expliquer sa fonction.

## Linting
Le projet utilise Pylint 4.0.5 pour garantir la qualité du code et le respect des conventions PEP 8. La commande pour vérifier le code est :
    pylint pkg/

## Tests
Les tests unitaires sont écrits avec pytest 9.0.3, pour lancer les tests :
    python3 -m pytest pkg/tests/

## Dépendances
Voici une liste des dépendances de notre code :
    Python 3.13.12 fournit les dépendances suivantes :
        datetime
        typing
        abc
        dataclasses
    pandas==2.3.3
    pytest==9.0.3
    pylint==4.0.5
