
#!/bin/bash

# Atualiza os pacotes apt
$ sudo apt update && sudo apt upgrade

# Instala os pacotes básicos de rede
sudo apt-get install net-tools iputils-ping ca-certificate

# Instala o SSH
sudo apt install openssh

# Instala o openjdk-17
sudo apt-get install openjdk-17-jdk

# Instala o docker
sudo apt-get install docker.io

# Cria as pastas /opt/pasta1 e /opt/pasta2 se elas não existirem
if [ ! -d /opt/postgresql ]; then
  mkdir /opt/postgresql
fi
