# Image Python légère
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Port exposé
EXPOSE 5000

# Variable d'environnement Flask
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Commande de lancement
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
