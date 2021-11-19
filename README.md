# TDD-introduction

## Initialiser le projet

### Créer un environnement virtuel

```shell
~$ python -m venv .venv/
~$ .venv/Scripts/activate
```

### Installer les dépendances

```shell
~$ pip install -r requirements.txt
```

### Quitter l'environnement virtuel

```shell
~$ deactivate
```

## Commandes principales

### Lancer le projet

`$ python app/main.py`

### Lancer les tests

`$ python -m unittest`

### Vérifier la qualité du code

`$ pylint ./app`
