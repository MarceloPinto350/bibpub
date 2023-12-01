#!/usr/bin/env bash

cd bibpub/
# Executar o comando abaixo para criar o banco de dados
#python manage.py migrate

# Executar o comando abaixo para criar o super usuário      
#python manage.py collectstatic --noinput

# Executar o comando abaixo para rodar o serviço
python manage.py runserver 0.0.0.0:8000