#!/bin/bash

echo ""
echo "PASSO 1: Instalando pacotes básicos..."
# Atualiza os pacotes apt
sudo apt update && sudo apt upgrade -y

# Instala os pacotes básicos de rede
sudo apt install net-tools iputils-ping apt-transport-https ca-certificates curl software-properties-common -y

# Instalar o SSH e SSL
sudo apt install openssh-server openssl -y

# Instalar o openjdk-17
sudo apt install openjdk-17-jdk -y

echo ""
echo "PASSO 2: Instalando Docker..."
# Instala o docker
# Adicionando a chave GPG do repositório do docker 
if sudo apt-key list | grep -i docker>/dev/null 2>%1; then
  echo "Chave do Docker já inclusa no Apt..."
else
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
fi

# Configura o APT para acesso às fontes do docker (Ubuntu 22.04-Jammy)
if sudo apt-cache showpkg docker | grep -i docker-ce>/dev/null 2>%1; then
  echo "Pacote Docker já incluso no repositóprio do Apt..."
else
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable"
fi

# instala o docker propriamente dito
if command -v docker >/dev/null 2>&1; then
  # O docker está instalado
  echo "Docker já está instalado..."
else
  sudo apt install docker-ce -y
fi

# instala o docker-coompose, conforme o caso
if command -v docker-compose >/dev/null 2>&1; then
  # O docker-compose está instalado
  echo "Docker-compose está instalado."
else
  sudo apt install docker-compose -y
fi

# Cria as pastas /opt/pasta1 e /opt/pasta2 se elas não existirem
#if [ ! -d /opt/pasta1 ]; then
#  mkdir /opt/pasta1
#fi

echo ""
echo "PASSO 3: Criando o banco de dados..."
# Criar o volume local no docker  para ser usado pelo Postgres
if [ ! -d /var/lib/docker/volumes/postgres_data ]; then
  sudo docker volume create postgres_data
fi

# Criar o container do Postgresql
sudo docker run -d \
  --name bibpub-postegres \
  -e POSTGRES_DB=bibpbdb \
  -e POSTGRES_USER=bibpb \
  -e POSTGRES_PASSWORD="@dm1n" \
  -e LANG=pt_BR.UTF8 \
  -e PGDATA=/var/lib/postgresql/data \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:alpine
