# Plano de testes - Sistema de Biblioteca

## Histórico de revisões

Versão | Descrição | Data | Responsável(is)
:-------:|-------------------------------------|:-------------:|--------------------
1.0 | Elaboração inicial do documento | 05/12/2023 | Marcelo e Alikson
1.1 | Ajustes nos requisitos principais | 08/12/2023 | Marcelo

## Situação atual do processo de testes no órgão
1. Foi realizado levantamento acerca da situação atual do órgão quanto ao aspecto de implementação e realização testes automatizados e testes em geral, sendo destacadas as  seguintes questões no panorama:
2. Nenhum dos sistemas desenvolvidos possui plano de testes;
3. Planejamento de testes só são realizados para alguns sistemas nacionais e envolvem usuários

## Introdução
Os objetivos deste plano de testes são garantir que o sistema de biblioteca para empréstimos de livros desenvolvido pela equipe de desenvolvimento do órgão satisfaça todos os requisitos funcionais e não funcionais especificados.

Da mesma forma, visa dar garantia mínima que as principais funcionalidades definidas sejam testadas durante do ciclo de vida do processo de desenvolvimento, de forma que as mudanças ocorridas no software não afetem o funcionamento das principais funcionalidades aqui definidas.

## Requisitos a testar
No escopo do presente plano de testes, são abrangidos os seguintes requisitos:
* Cadastro de usuários
* Cadastro de livros
* Empréstimo de livros
* Devolução de livros
* Reserva de livros
* Consulta de livros

## Priorização de requisitos

### Testes Específicos
Aqui estão listadas as principais funcionalidades que deverão ser priorizadas nos testes que devem ser realizados:

* Cadastro de usuários:
   * Testar se é possível cadastrar um usuário com dados válidos;
   * Testar se é possível cadastrar um usuário com dados inválidos;
   * Testar se é possível cadastrar um usuário com dados duplicados.

* Cadastro de livros:
   * Testar se é possível cadastrar um livro com dados válidos;
   * Testar se é possível cadastrar um livro com dados inválidos;
   * Testar se é possível cadastrar um livro com dados duplicados.

* Empréstimo de livros:
   * Testar se é possível emprestar um livro para um usuário válido;
   * Testar se é possível emprestar um livro para um usuário inválido;
   * Testar se é possível emprestar um livro que já está emprestado;
   * Testar se é possível emprestar um livro que não existe.

* Devolução de livros:
   * Testar se é possível devolver um livro que está emprestado;
   * Testar se é possível devolver um livro que não está emprestado;
   * Testar se é possível devolver um livro que não existe.

* Reserva de livros:
   * Testar se é possível reservar um livro para um usuário válido;
   * Testar se é possível reservar um livro para um usuário inválido;
   * Testar se é possível reservar um livro que já está reservado;
   * Testar se é possível reservar um livro que não existe.

* Consulta de livros:
   * Testar se é possível consultar um livro pelo título;
   * Testar se é possível consultar um livro pelo autor;
   * Testar se é possível consultar um livro pelo gênero;
   * Testar se é possível consultar um livro pela data de publicação.

## Estratégias de teste
Os testes serão realizados de forma manual e automatizada.

### Critérios de Aceitação
Um teste será considerado aprovado se o sistema atender aos seguintes critérios:
1. O teste deve ser executado sem erros;
2. O teste deve produzir os resultados esperados.

## Recursos
Para a realização dos testes, serão necessários os seguintes recursos:

### Humanos
Os testes serão realizados por uma equipe de 6 pessoas, composta por 4 desenvolvedores, 1 analista da área de negócio e 1 testador da equipe de sustentação de sistemas. 

### Ambientes de teste
Para que seja viabilizada a realização dos testes, serão necessários os seguintes ambientes:
* Microcomputadores com qualquer sistema operacional, com navegaor web instalado e acesso à internet/rede local;
* Acesso ao ambiente de desenvolvimento integrado (IDE);
* Banco de dados PostgreSQL;

### Ferramentas de teste
Considerando que o software será desenvolvido em Pyton, será necessário acesso às bibliotecas de desenvolvimento de testes para a Ferramentas de automação de testes

## Cronograma
Os testes serão realizados em duas fases:

  **Fase 1**: Testes de unidade e integração (2 semanas)
  **Fase 2**: Testes de aceitação (1 semana)

### Fase 1: Testes de unidade e integração
Os testes de unidade serão realizados pelos desenvolvedores, com o objetivo de verificar se cada unidade de código funciona corretamente. Deverão adotar a estratégia de incluir o desenvolvimento dos casos de teste juntamente com a fase de desenvolvimento, visando minimizar eventuais retrabalhos na codificação.
Os testes de integração serão realizados pela equipe de testes/sustentação, com o objetivo de verificar a integração entre as unidades de código.

### Fase 2: Testes de aceitação
Os testes de aceitação serão realizados pelo usuário final ou de negócio, com o objetivo de verificar se o sistema atende aos requisitos especificados.



