#!/bin/bash

# Atualizar os pacotes da máquina
echo "PASSO 1: Atualizando pacotes instalados..."
sudo apt update && sudo apt upgrade -y

# instalar configurações básicas de rede e segurança
echo "PASSO 2: Instalando pacotes básicos..."
sudo apt install -y net-tools iputils-ping ca-certificates openssh-server openssl

# instalar o openjdk 17
echo "PASSO 3: Instalando OpenJDK..."
sudo apt install openjdk-17-jdk

# instalar o VS Code
echo "PASSO 4: Instalando VS Code..."
if command -v code >/dev/null 2>&1; then
	echo "VS Code instalado..."
else
	sudo snap install --classic code 
fi

# configurando o python
python --version >/dev/null 2>&1
if [ $? -eq 0 ]; then
	echo "O Python está instalado."
	echo "Versão:  $(python --version)"
	echo "PASSO 5: Instalando o PIP para o Python..."
	sudo apt install python3-pip -y
	sudo apt install pytho3.10-venv -y
	##echo "PASSO 6: Instalando o Django para o Python... (requeriments.txt)"
	##sudo python -m pip install Django
	#echo "PASSO 7: Instalando o driver do Postgres para o Python... (requeriments.txt)"
	# conforme o caso, instalar os drives correspondentes ao BD a ser utilizado
	#sudo python -m pip install "psycopg[binary]"
else
	echo "O Python não está instalado."
	#echo "Instalando..."
	#sudo apt install python3
	# instalando o PIP
	#sudo apt install python3-pip
	#instalando o Django
        #sudo python -m pip install Django
fi

# Instalar o dbeaver para gerenciamento do banco de dados
echo "PASSO 8: Instalando o DBeaver para gerenciar banco de dados..."
sudo snap install dbeaver-ce

# Instalar o cliente do GIT
echo "PASSO 9: Instalando o GIT para acesso aos repositórios das aplicações..."
sudo apt install git -y

echo "Configurando email do usuário git... Exemplo: git config --global user.email 'pintomarc@gmail.com'"
git config --global user.name "Marcelo Pinto"
git config --global user.email "pintomarc@gmail.com"

echo "Criando para pasta do GIT para os projetos no local onde se encontra este script..."
if [ ! -d git ]; then
	mkdir git
fi


echo "PASSO 10: Importando o projeto do Github..."

echo "Certifique-se de possuir o certificado SSH importando no Github para permitir acesso..."
ls -al ~/.ssh/

# Para gerar o certificado use o comando: ssh-keygen -t rsa -b 4096 -C <email>
# Para verificar se o agende do ssh está rodando: eval "$(ssh-agent -s)"
# Para adicionar a chave privatda ao agente: ssh-add ~/.ssh/id_rsa
# Adicionar a chave pública no Github através da interface web do Github

cd ~/git
git clone https://github.com/MarceloPinto350/bibpub-imd.git

# final da configuração
echo "Versão:  $(python --version)"
echo "Versão PIP:  $(pip --version)"
echo "Versão Django:  $(python -m django --version)"
eval "$(ssh-agent -s)"
