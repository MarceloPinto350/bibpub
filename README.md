# Projeto de Aplicação WEB para Biblioteca Pública
Repositório do projeto de Biblioteca Pública, sendo parte integrante do trabalho final da disciplina de PPGTI1004-DESENVOLVIMENTO WEB 2, do PPGTI, IMD, ministrada pelo prof. Jean Mario Moreira de Lima.

## Componenete do grupo
1. Alikson Oliveira
2. Marcelo Pinto
3. Vitor Lindbergh


## Estrutura de pastas do projeto

### config_server
Contem as configurações da máquina usada como servidor (Docker)

### config_dev
Contem as configurações da máquina utilizada como cliente de desenvolvimento

### codigo
Contem o código fonte da aplicação propriamente dita


## Entidades

### OBRA
* titulo: character (200), NOT NULL
* ano_publicacao: integer, NOT NULL,  validação: 0 < valores >= ano_corrente
* edicao: integer, NOT NULL
* isbn: number, composto de 13 dígitos, NULL
* issn: number, composto de 8 dígitos, NULL
* categoria: FK -> CATEGORIA, NOT NULL
* autor: FK - AUTOR, NOT NULL
* editora: FK - EDITORA, NOT NULL

### AUTOR
* nome: character (200), NOT NULL
* dt_nascimento: date, NULL, validação: data-corrente - dt_nascimento >= 3 anos
* biografia: character (1000), NULL

### CATEGORIA
* descricao: character (100), NOT NULL

### EDITORA
* nome: character (200), NOT NULL
* e_mail: character (100), validação: email válido
* pais: opção: Lista de países a selecionar

### PESSOA
* nome: character (200), NOT NULL
* cpf: number (11), NOT NULL
* sexo: opções:
* e_mail: character (100), validação: e-mail válido
* cep: number, tamanho 8
* endereço: character (200), NOT NULL
* cidade: character (200), NOT NULL
* estado: character (2), NOT NULL, valores da lista, oriundos da tabela ESTADOS
* situacao_pessoa: character (1), sendo possível um dos valores: “A”-Ativa | “S’-Suspensa | “P”-Pendência de devolução

### PAPEL
* nome: character (50), NOT NULL
* descricao: character (200), NULL

### USUARIO
* id_pessoa: FK -> PESSOA
* id_papel: FK -> PAPEL
* dt_inicio: date, NOT NULL
* dt_fim: date, NULL

### EMPRESTIMO	
* id_pessoa: FK -> PESSOA, NOT NULL
* id_obra: FK -> OBRA, NOT NULL
* id_usuario: FK -> USUARIO, NOT NULL
* dt_emprestimo: date, NOT NULL
* prazo_emprestimo: integer NOT NULL, validação: 5 < valor < 60
* dt_devolucao:	date, NULL
