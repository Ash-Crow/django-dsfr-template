# Django x DSFR

## Introduction

Ce repo est un kit de démarrage pour vos projets en Django. Il intègre :

- le [Design System de l’État](https://www.systeme-de-design.gouv.fr/) (DSFR) avec [django-dsfr](https://pypi.org/project/django-dsfr/)
- des Content Security Policies avec [django-csp](https://pypi.org/project/django-csp/)
- les paramètres pour se connecter à une base de données PostgreSQL
- [pre-commit](https://pre-commit.com/), pour formater votre code à chaque commit
- une ébauche de CI pour vos tests automatiques
- une ébauche de [justfile](https://just.systems/) pour gérer les commandes fréquentes
- [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances
- les modules django-extensions et django-debug-toolbar pour faciliter le développement
- Les ajustements nécessaires pour déployer Django sur [Scalingo](https://doc.scalingo.com/languages/python/django/start):
  - [gunicorn](https://gunicorn.org/)
  - un fichier Procfile
  - [Cling](https://pypi.org/project/dj-static/) pour servir les fichiers statiques

## Use

```bash
make runserver
```

## Installation

### Edit .env

Copier les variables d’environnement :
```
cp .env.example .env
```
puis modifier en le contenu pour correspondre à votre configuration.

### Installer l’environnement et les dépendances

```
uv sync --no-dev
```

Pour une installation de dev en local, installer aussi les dépendances devs
```
uv sync
```

### Configurer la base de données

Installer PostgreSQL en fonction de votre OS : https://www.postgresql.org/download/
puis créer une base de données et configurer les paramètres correspondants dans DATABASE_URL de votre fichier .env.

### Remplir la base de données et collecter les fichiers statiques
```bash
just update
```

Cette commande peut être passée à chaque mise à jour.

### Installation de pre-commit

[Pre-commit](https://pre-commit.com/) permet de linter et formater votre code avant chaque commit. Il exécute les commandes définies dans le fichier `.pre-commit-config.yaml`

Pour l’installer :

```bash
pre-commit install
```

Vous pouvez effectuer un premier passage sur tous les fichiers du repo avec :

```bash
just quality
```

### Internationalisation
Le dépôt est prêt pour l’[internationalisation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/).
Taper `just makemessages` pour générer les chaînes à traduire, et effectuer la traduction avec un outil tel que [Poedit](https://poedit.net/).

### Exécuter les tests manuellement

```bash
just test
```

### Accéder au shell Django avancé
```bash
just shell
```
