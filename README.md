# Mini Catalogue de Jeux Vidéo 🎮

## Description
Application web Flask permettant de parcourir un catalogue de jeux vidéo. 
Les données sont stockées dans un fichier JSON et le site est conteneurisé avec Docker.

**Thème choisi : Jeux Vidéo**

## Structure du projet
```
Projet/
├── app/
│   ├── __init__.py           # Initialisation de l'application Flask
│   ├── routes.py             # Définition des routes
│   ├── data/
│   │   └── items.json        # Données du catalogue (pseudo BDD)
│   ├── templates/
│   │   ├── base.html         # Template de base (header, nav, footer)
│   │   ├── index.html        # Page d'accueil
│   │   ├── items_list.html   # Liste des jeux
│   │   ├── item_detail.html  # Détail d'un jeu
│   │   ├── about.html        # Page À propos
│   │   └── 404.html          # Page d'erreur 404
│   └── static/
│       └── style.css         # Feuille de styles
├── requirements.txt          # Dépendances Python
├── Dockerfile                # Configuration Docker
├── docker-compose.yml        # Configuration Docker Compose
└── README.md                 # Ce fichier
```

## Les 4 pages du site

| Route | Template | Description |
|-------|----------|-------------|
| `/` | index.html | Page d'accueil avec présentation du site |
| `/items` | items_list.html | Liste de tous les jeux du catalogue |
| `/items/<id>` | item_detail.html | Détail d'un jeu spécifique |
| `/about` | about.html | Page À propos avec infos sur le projet |

## Lancement avec Docker

### 1. Construire l'image Docker
```bash
docker build -t mini-catalogue .
```

### 2. Lancer le conteneur
```bash
docker run -p 5000:5000 mini-catalogue
```

### Alternative avec Docker Compose
```bash
docker compose up --build
```

Le site est ensuite accessible sur : **http://localhost:5000**

## Lancement en local (sans Docker)

### 1. Créer un environnement virtuel
```bash
python -m venv venv
```

### 2. Activer l'environnement virtuel
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
# Option 1 : avec flask run
set FLASK_APP=app/routes.py
flask run

# Option 2 : avec Python directement
python -c "from app import app; app.run(host='0.0.0.0', port=5000, debug=True)"
```

## Technologies utilisées
- **Python 3.11**
- **Flask 3.0** - Framework web
- **Jinja2** - Moteur de templates
- **HTML/CSS** - Interface utilisateur
- **Docker** - Conteneurisation
- **JSON** - Stockage des données

## Équipe
- **Sofiane CHERIETTE** - Étudiant L3

## TP TP – Mini site Flask
© 2026
