# Utiliser l'image officielle Python comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source de l'application
COPY . .

# Définir les variables d'environnement Flask
ENV FLASK_APP=app/routes.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Exposer le port sur lequel Flask s'exécute
EXPOSE 5000

# Commande pour lancer l'application
CMD ["flask", "run"]
