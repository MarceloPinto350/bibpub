# Pré requisitos para executar o ambiente de desenvolvimento
Este ambiente de desenvolvimento foi testado e executado em uma máquina vitual e um máquina física com sistema operacional Ubuntu 22.04 LTS, instalada e configurada conforme arquivo configDev.sh, em anexo.

## Criando o projeto a partir do zero
Inicialmente crie e vá para a pasta onde será criada e armazenada a pasta do projeto, por exemplo, a pasta ~/git/projetos
* $ cd ~/git/projetos

Em seguida execute o comando para criar a estrutura do projeto para o Django.
* $ django-admin startproject bibpub

Para iniciar e testar a aplicação está executando rode o comando abaixo:
* python manage.py runserver 0.0.0.0:8000

Para testar, abra o navegador na máquina e acesse a url localhost:8000


## Para utilizar o projeto a partir do Github
Inicialmente crie uma máquina virtual Linux Ubuntu 22.04, ou, caso sua máquina seja Linux compatível com Ubuntu 22.04 e/ou Debian, abra o gerenciador de arquivos e crie uma pasta no home do usuário chamada git.

* Abra o VS Code e adicione a pasta do projeto: **Menu Arquivo** -> **Abrir pasta**
* Abra um terminal para o VS Code: **Terminal** -> **Novo Termional** 
* Clique no terminal e adicione a variável de desenvolvimento, conforme segue:
   $ python3 -m venv venv  # configura as configurações de ambiente com o venv
   $ source venv/bin/activate # para ativar o venv - observe que irá ficar com o texto (venv) no início do prompt
   $ python -m pip install --upgrade pip  # atualizar o pip
   $ python -m pip install -r requirements.txt  # instala as dependências do projeto




Em seguida crie um par de chaves para utilizar no Github, usando o seguinte comando: 
* $ ssh-keygen -t rsa -b 4096 -C <email>

Para verificar se o agende do ssh está rodando, use o seguinte comando: 
* $ eval "$(ssh-agent -s)"

Para adicionar a chave privada ao agente, para evitar que todas as vezes que vocês tentar sincronizar com o Github seja exigida a senha do certificado, execute o seguinte comando: 
* $ ssh-add ~/.ssh/id_rsa

Em seguinda acesse o github e adcione a chave pública no seu perfil do Github, conforme passos a seguir:
1. Faça a cópia do texto da chave pública (ex.: cat ~/.ssh/id_rsa.pub);
2. Acesse a interface web do Github;
3. Clique no ícone da sua imagem, no canto superior direito da tela e selecione o menu "Settings"/"Configurações";
4. Seelcine a opção "SSH and GPG keys" à esquerda da tela;
5. Clique no botão "New SSH key";
6. Informe um nome para a chave "Title" e cole o conteúdo lido no passo 1 para o campo "Key", mantendo selecionado "Key type" = "Authentication Key";
7. Clique no botão "Add SSH key" para conlcuir


