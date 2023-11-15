# Configuração da máquina servidora - Auxiliar
Esta configuração foi desenvolvida para criar um ambiente Docker para rodar o banco de dados e demais serviços para uso pela aplicação.

## Pré requisitos:
O ambiente para rodar os serviços foi configurado em uma máquina virtual do Oracle Virtualbox, com sistema operacional Ubuntu 22.04, com os seguintes recursos e configurações:
* Memória: 6Gb
* CPU: 3
* Rede: Bridge

## Como proceder a configuração:
Acessar a máquina virtual, acessar o prompt de comando, compiar o arquivo **inicializaConfig.sh** para uma pasta local e proceder a execução dos seguintes comandos:
* $ chmod +x inicializaConfig.sh
* $ ./inicializaConfig.sh
