#!/bin/bash

# Atualiza os pacotes apt
sudo apt update && sudo apt upgrade -y

# Instala os pacotes básicos de rede
sudo apt-get install net-tools iputils-ping apt-transport-https ca-certificates curl software-properties-common -y

# Instalar o SSH e SSL
sudo apt install openssh-server openssl -y

# Instalar o openjdk-17
sudo apt-get install openjdk-17-jdk -y

# Instala o docker
# Adicionando a chave GPG do repositório do docker 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Configura o APT para acesso às fontes do docker (Ubuntu 22.04-Jammy)
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable"
# instala o docker propriamente dito
sudo apt update && sudo apt install docker-ce -y

# Cria as pastas /opt/pasta1 e /opt/pasta2 se elas não existirem
#if [ ! -d /opt/pasta1 ]; then
#  mkdir /opt/pasta1
#fi

# Criar o volume local no docker  para ser usado pelo Postgres
sudo docker volume create postgres_data

# Criar o container do Postgresql
sudo docker run -d \
  --name bibpub-postegres \
  -e POSTGRES_DB=bibpbdb \
  -e POSTGRES_USER=bibpb \
  -e POSTGRES_PASSWORD=’@dm1n’ \
  -e LANG=pt_BR.UTF8 \
  -e PGDATA=/var/lib/postgres/data \
  -p 5432:5432
  --mount ‘type=volume,source=postgres_data,destination=/var/lib/postgres/data,”volume-opt=rw”’ \
  postgres:alpine
