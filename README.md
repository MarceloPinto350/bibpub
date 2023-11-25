# Descrição do projeto 
Este projeto de aplicação para empréstimos de livros para bibliotecas públicas, é parte integrante do trabalho final da disciplina de PPGTI1004-DESENVOLVIMENTO WEB 2, do Programd de pós graduação em Tecnologia da Informação da Universidade Federal do Rio Grando do Norte (UFRN/IMD), ministrada pelo prof. Jean Mario Moreira de Lima.

## Componenetes do grupo
1. Alikson Oliveira
2. Marcelo Pinto
3. Vitor Lindbergh

## Requisitos Funcionais
   PAPEIS: ADMIN, USER, OPERADOR
1. A aplicação deve permitir que as pessoas realizem seu próprio cadastro pela internet;
2. Ao realizar o cadastro do usuário ficará disponível para os operadores do ou adminsitradores do sistema avaliarem e aprovarem o cadastro: PENDENTE, ATIVO, SUSPENSO, BLOQUEADO
3. A aplicação deve permitir a consulta às obras cadastradas, pelo título, autor, através da internet a qualquer usuário habilitado;
4. A aplicação deve permitir a reserva, de até 3 obras, para empréstimos a partir da internet, apenas às pessoas cadastradas e ativas, a reserva é válida por 7 dias após a 1ª disponibiizadae de um exemplar;
5. A aplicação deve permitir o empréstimo, de até 5 obras simultaneamente, às pessoas cadastradas e com cadastro ativo, pelo período de 30 a 90 dias, a escolha da pessoa, não podendo ter obras a empréstdas em atraso;
6. A aplicação deverá permitir a renovação de empréstimos, por igual período, caso não haja reserva para a obra, a partir dos últimos 10 dias de empréstimo atual;
7. As obras podem ter situação da disponibilidade alterada pelo operador ou adminsitrador: INDISPONÍVEL, USO INTERNO, DISPONÍVEL PARA EMPRÉSTIMO
8. A aplicação deverá listar em sua página principal: a quantidade de obras cadastradas, total de empréstimos no ano corrente, as 5 obras mais emprestadas e os últimos cinco títulos cadastrados;
9. A aplicação deverá consignar penalidades às pessoas, confrome as seguintes regras:
    * Devolver fora do prazo do empréstimo, a pessoa ficará com a situação suspensa por 10 dias e não poderá pegar novas obras emprestadas; 
    * Com atraso na devolução superior a 30 dias, a pessoa ficará bloqueada, não podendo acessar o sistema até a devolução da obra em atraso; (TODO: AUTOMATIZAR)
10. O sistema deverá permitir o usuário visualizar seu histórico de empréstimos;
11. A aplicação deve aceitar a confirmação/validação de cadastro das pessoas, pelo link e chave enviada por e-mail; (TODO:)
12. A pesquisa de obra poderá permitir filtrar por categoria e tipo de disponibilidade; (TODO:)


## Estrutura de pastas do projeto

### config_server
Contem as configurações da máquina usada como servidor (Docker)

### config_dev
Contem as configurações da máquina utilizada como cliente de desenvolvimento

### bibpub
Contem o código fonte da aplicação propriamente dita


## Entidades

### OBRA
* titulo: character (200), NOT NULL
* anopublicacao: integer, NOT NULL,  validação: 0 < valores >= ano_corrente
* edicao: integer, NOT NULL
* isbn: varchar(20), composto de 13 dígitos, NULL
* issn: varchar(20), composto de 8 dígitos, NULL
* tipo: varchar (10), NOT NULL
* categoria_id: FK -> CATEGORIA, NOT NULL
* autor_id: FK - AUTOR, NOT NULL
* editora_id: FK - EDITORA, NOT NULL
* datacadastro: datetime, NOT NULL

### AUTOR
* nome: character (200), NOT NULL
* nascimento: date, NULL, validação: data-corrente - dt_nascimento >= 3 anos
* biografia: character (1000), NULL

### CATEGORIA
* descricao: character (100), NOT NULL

### EDITORA
* nome: character (200), NOT NULL
* e_mail: character (254), validação: email válido
* pais: varchar(100)opção: Lista de países a selecionar

### PESSOA
* nome: character (200), NOT NULL
* nascimento date, NULL
* cpf: number (11), NOT NULL
* sexo: varchar(1), NOT NUL
* genero: int4, NOT NULL
* email: character (100), validação: e-mail válido
* cep: number, tamanho 8
* endereço: character (200), NOT NULL
* cidade: character (200), NOT NUL
* uf: character (2), NOT NULL, valores da lista, oriundos da tabela ESTADOS
* cadastro: datetime
* origem: varchar (10), NOT NULL ("origem do cadastro")
* situacaocadastro: character (1), sendo possível um dos valores: “A”-Ativa | “S’-Suspensa | “P”-Pendência de devolução

### PAPEL (USAR DO DJANGO)
* nome: character (50), NOT NULL
* descricao: character (200), NULL

### USUARIO (USAR DO DJANGO)
* id_pessoa: FK -> PESSOA
* id_papel: FK -> PAPEL
* dt_inicio: date, NOT NULL
* dt_fim: date, NULL

### EMPRESTIMO	
* pesso_id: FK -> PESSOA, NOT NULL
* data_emprest: date, NOT NULL
* prazo: integer NOT NULL, validação: 5 < valor < 60
* data_devol:	date, NULL

### EMPRESTIMO_OBRAS
* emprestimo_id, FK -> EMPRESTIMO, NOT NULL
* obra_id, FK -> OBRA, NOT NULL
