# Pour installer docker

sudo apt update && sudo apt upgrade -y

sudo apt install -y ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update


sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world

# Pour lancer le conteneur

#Ajoutez votre utilisateur au groupe docker :

sudo usermod -aG docker $USER

# Appliquez les changements :

newgrp docker

# Vérifiez que ça fonctionne :

docker run hello-world


docker build -t mlflow-server .

docker run -d -p 8080:8080 --name mlflow-container mlflow-server

docker stop mlflow-container

docker start mlflow-container
