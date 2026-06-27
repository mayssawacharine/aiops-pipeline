# 1. On utilise une image Python légère (la même version que ton lab)
FROM python:3.10-slim

# 2. On définit le dossier de travail dans le conteneur
WORKDIR /app

# 3. On copie tout notre code dans le conteneur
COPY . /app

# 4. La commande à lancer quand le conteneur démarre
CMD ["python3", "app.py"]
