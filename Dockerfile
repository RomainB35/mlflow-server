# Utilisez l'image officielle Python
FROM python:3.9-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installation dépendances de test
COPY requirements-test.txt .
RUN pip install --no-cache-dir -r requirements-test.txt

# Installer MLflow et les dépendances
RUN pip install --no-cache-dir mlflow psycopg2-binary boto3

# Exposer le port MLflow
EXPOSE 8080

# Commande par défaut pour lancer le serveur MLflow
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080"]


FROM python:3.9-slim

# Installation des dépendances
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


