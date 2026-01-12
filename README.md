# Mini Catalogue de Jeux Vidéo 🎮

> Application web Flask permettant de parcourir un catalogue de 30 jeux vidéo avec images.

---

## 🚀 Lancement rapide

### Option 1 : Docker (recommandé) 🐳
```bash
docker compose up --build
```

### Option 2 : Script automatique (Windows)
```bash
.\start.bat
```
ou directement :
```bash
python start.py
```

### Option 3 : Script automatique (Linux/Mac)
```bash
chmod +x start.sh && ./start.sh
```

> Les scripts vérifient automatiquement si Python et les dépendances sont installés, et les installent si nécessaire.

👉 **Accès au site : http://localhost:5000**

---

## 📖 Description

Application web développée dans le cadre d'un TP de L3 sur Flask et Docker.  
Les données sont stockées dans un fichier JSON et le site est conteneurisé avec Docker.

**Thème choisi : Jeux Vidéo**

### Fonctionnalités
- 🎮 Catalogue de 30 jeux vidéo avec images
- 🔍 Affichage détaillé de chaque jeu
- 📱 Design responsive et moderne
- 🐳 Conteneurisation Docker

---

## 🌐 Les 4 pages du site

| Route | Template | Description |
|-------|----------|-------------|
| `/` | index.html | Page d'accueil avec présentation du site |
| `/items` | items_list.html | Liste de tous les jeux du catalogue |
| `/items/<id>` | item_detail.html | Détail d'un jeu spécifique |
| `/about` | about.html | Page À propos avec infos sur le projet |

---

## 📂 Structure du projet

```
Projet/
├── app/
│   ├── __init__.py           # Initialisation de l'application Flask
│   ├── routes.py             # Définition des routes
│   ├── data/
│   │   └── items.json        # Données du catalogue (30 jeux avec images)
│   ├── templates/
│   │   ├── base.html         # Template de base
│   │   ├── index.html        # Page d'accueil
│   │   ├── items_list.html   # Liste des jeux
│   │   ├── item_detail.html  # Détail d'un jeu
│   │   ├── about.html        # Page À propos
│   │   ├── 404.html          # Page d'erreur 404
│   │   └── partials/
│   │       ├── header.html   # En-tête du site
│   │       └── footer.html   # Pied de page
│   └── static/
│       └── css/              # CSS modulaires
│           ├── base.module.css
│           ├── header.module.css
│           ├── footer.module.css
│           ├── index.module.css
│           ├── items_list.module.css
│           ├── item_detail.module.css
│           ├── about.module.css
│           └── 404.module.css
├── requirements.txt          # Dépendances Python
├── Dockerfile                # Image Docker
├── docker-compose.yml        # Configuration Docker Compose
└── README.md                 # Ce fichier
```

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **Python 3.11** | Langage principal |
| **Flask 3.0** | Framework web |
| **Jinja2** | Moteur de templates |
| **HTML/CSS** | Interface utilisateur |
| **Docker** | Conteneurisation |
| **JSON** | Stockage des données |

---

## 👤 Équipe

- **Sofiane CHERIETTE** - Étudiant L3

---

## 📝 TP – Mini site Flask

© 2026
