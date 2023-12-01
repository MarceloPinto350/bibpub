FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /biblioteca
WORKDIR /biblioteca

# Instalando as dependências do SO
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y linux-headers && \
apt install -y net-tools apt-transport-https ca-certificates curl && \
apt install -y openssh-server openssl postgresql-client 

# Instalando asconfigurações para o Python
RUN pip install -U pip setuptools 

# Copiando o arquivo de dependências para o container
COPY requirements.txt /biblioteca/

# Instalando as dependências do Python
RUN pip install -r /biblioteca/requirements.txt
RUN pip install -r /biblioteca/requirements-opt.txt

# Copiando o código da aplicação para o container
ADD . /biblioteca/

# Espendo o Django service na máquina
EXPOSE 8000