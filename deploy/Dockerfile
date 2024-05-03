FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /biblioteca
WORKDIR /biblioteca

# Instalando as dependências do SO
RUN apt-get update && apt-get upgrade -y && apt-get install -y linux-headers && \
  apt install -y net-tools apt-transport-https ca-certificates curl && \
  apt install -y openssh-server openssl postgresql-client 

# Instalando asconfigurações para o Python
RUN pip install -U pip setuptools 

# Copiando o código da aplicação para o container
ADD . .

# Copiando o arquivo de dependências para o container
COPY requirements.txt /biblioteca/

# Executando a aplicação quando o container inicia
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Expondo o Django service na máquina
EXPOSE 8000
