# 🚀 Guide d'installation et d'utilisation de Docker pour le projet MLflow

Ce document vous guide étape par étape pour :

- Installer Docker sur Ubuntu
- Lancer votre image Docker `mlflow-server`
- Vérifier que tout fonctionne correctement

---

## 🐳 1. Installer Docker sur Ubuntu

### 🔧 Mettre à jour les paquets

```bash
sudo apt update && sudo apt upgrade -y
```

### 🛡️ Installer les dépendances nécessaires

```bash
sudo apt install -y ca-certificates curl gnupg
```

### 🔑 Ajouter la clé GPG officielle de Docker

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

### 📦 Ajouter le dépôt Docker à vos sources APT

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 🔄 Mettre à jour les sources et installer Docker

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

## ✅ 2. Tester Docker

### 🧪 Vérifier que Docker fonctionne correctement

```bash
sudo docker run hello-world
```

---

## 👤 3. Utiliser Docker sans sudo (optionnel mais recommandé)

### ➕ Ajouter votre utilisateur au groupe `docker`

```bash
sudo usermod -aG docker $USER
```

### 🔁 Appliquer les changements (nécessite de se reconnecter)

```bash
newgrp docker
```

### 🔁 Vérifier à nouveau que Docker fonctionne sans sudo

```bash
docker run hello-world
```

---

## 🛠️ 4. Construire et lancer le conteneur `mlflow-server`

### 🏗️ Construire l'image Docker

Assurez-vous d’avoir un `Dockerfile` à la racine de votre projet.

```bash
docker build -t mlflow-server .
```

### 🚀 Lancer le conteneur

```bash
docker run -d -p 8080:8080 --name mlflow-container mlflow-server
```

Le serveur MLflow sera accessible sur [http://localhost:8080](http://localhost:8080)

---

## ⏹️ 5. Gérer le conteneur

### ⛔ Arrêter le conteneur

```bash
docker stop mlflow-container
```

### ▶️ Relancer le conteneur

```bash
docker start mlflow-container
```

---

## 🧼 Bonus : Supprimer le conteneur ou l'image (si nécessaire)

### ❌ Supprimer un conteneur

```bash
docker rm mlflow-container
```

### ❌ Supprimer une image

```bash
docker rmi mlflow-server
```

---

## 📦 Dépannage

- Si vous voyez une erreur `permission denied`, assurez-vous d’avoir bien appliqué `newgrp docker` ou reconnectez-vous à votre session.
- Vérifiez que le port 8080 est libre (pas utilisé par un autre service).
- Utilisez `docker ps -a` pour lister tous les conteneurs, même arrêtés.

---

💡 N’hésitez pas à adapter ce fichier selon vos besoins spécifiques ou à l’ajouter à la racine de votre projet sous le nom `README.md`.

