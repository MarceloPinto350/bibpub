from django.db import models

# outros imports usados
from datetime import datetime
from django.urls import reverse 

class Categoria(models.Model):
    descricao = models.TextField('Descrição', unique=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = "tb_categoria"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        permissions = [
            ("can_view_categoria", "Can view categorias"),
            ("can_change_categoria", "Can change categorias"),
            ("can_add_categoria", "Can add categorias"),
            ("can_delete_categoria", "Can delete categorias"),
        ]

# Criação do modelo Pessoa
class Pessoa (models.Model):
    OPC_SEXO = [
        ("M","Masculino"),
        ("F","Feminino"),
        ("I","Intersexo"),
        ("N","Não informado"),
    ]
    OPC_GENERO = [
        (1,"Cisgênero"),
        (2,"Transgênero"),
        (3,"Transexual"),
        (4,"Travesti"),
        (5,"Gênero fluido"),
        (6,"Agênero"),
        (7,"Outra"),
        (8,"Não informado"),
    ]
    
    Estados = models.TextChoices("Estados","AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RO RR SC SP SE TO")
    OrigemCadastro = models.TextChoices("Origem cadastro" ,"INTERNET APLICAÇÃO")
    SituacaoCadastro = models.TextChoices("Situação cadastro","ATIVO PENDENTE SUSPENSO BLOQUEADO")
    #id = models.BigAutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=200, null=False,db_index=True)
    nascimento = models.DateField("Data nascimento")
    cpf = models.CharField("CPF", max_length=14, null=False, unique=True)
    #criar validador para CPF
    sexo = models.CharField("Sexo", max_length=1, null=False, choices=OPC_SEXO,default="N")
    genero = models.IntegerField("Identidade de Gênero", null=False, choices=OPC_GENERO,default=1)
    eMail = models.CharField("E-Mail", max_length=254, null=False)
    # Verificar o uso do validador de e-mails
    #eMail = models.CharField("E-Mail", max_length=254, null=False, 
    #        validator=[
    #            EmailValidator(message="Informe um e-mail válido!", 
    #            code=None,
    #            allowlist=None)
    #        ])
    cep = models.CharField("CEP", max_length=9)
    # criar validador para CEP
    #cep = models.ForeignKey (ZipCode,on_delete=models.SET_NULL, blank=True, null=True,)
    endereco = models.CharField("Endereço", max_length=200, null=False)
    cidade = models.CharField("Cidade", max_length=200, null=False)
    uf = models.CharField("Unidade da federação", max_length=2, null=False, choices=Estados.choices)
    cadastro = models.DateTimeField ("Data do cadastro",auto_now_add=True)
    origem = models.CharField("Origem do cadastro da pessoa", max_length=10, null=False, default="PENDENTE", choices=OrigemCadastro.choices)
    situacaocadastro = models.CharField("Situação do cadastro da pessoa", max_length=10, null=False, default="INTERNET", choices=SituacaoCadastro.choices)
    
    # retornar o valor padrão para a classe
    def __str__(self):
        return self.nome

    # define o nome padrão da tabela a ser criada no BD
    class Meta:
        db_table = "tb_pessoa"
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        permissions = [
            ("can_view_pessoa", "Can view pessoas"),
            ("can_change_pessoa", "Can change pessoas"),
            ("can_add_pessoa", "Can add pessoas"),
            ("can_delete_pessoa", "Can delete pessoas"),
        ]


# Definição do modelo de Autor
class Autor(models.Model):
    nome = models.CharField("Nome do autor", max_length=200, null=False, unique=True)
    nascimento = models.DateField("Data de nascimento", null=True)
    biografia = models.TextField("Biografia do autor", max_length=1000, null=False)
 
    def __str__(self):
        return self.nome 

    # define as configuraçẽos da classe Meta (dados de BD)
    class Meta:
        db_table = "tb_autor"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        permissions = [
            ("can_view_autor", "Can view autores"),
            ("can_change_autor", "Can change autores"),
            ("can_add_autor", "Can add autores"),
            ("can_delete_autor", "Can delete autores"),
        ]


# Definição do modelo de Autor
class Editora(models.Model):
    nome = models.CharField("Nome da editora", max_length=200, null=False, unique=True)
    email = models.CharField("E-Mail de contato da editora", max_length=254, null=False)
    # criar validação para os e-mails
    pais = models.CharField("País da editora", max_length=100, null=False)
    # validar conformme tabela de países a ser criada

    def __str__(self):
        return self.nome 
    
    # define as configurações da classe Meta (dados de BD)
    class Meta:
        db_table = "tb_editora"
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        permissions = [
            ("can_view_editora", "Can view editoras"),
            ("can_change_editora", "Can change editoras"),
            ("can_add_editora", "Can add editoras"),
            ("can_delete_editora", "Can delete editoras"),
        ]

# Definição do modelo de Obra
class Obra(models.Model):
    TipoObra = models.TextChoices("Tipo de obra" ,"LIVRO PERIÓDICO JORNAL REVISTA")
    titulo = models.CharField("Título da obra", max_length=200, null=False, unique=True, db_index=True)
    anopublicacao = models.PositiveSmallIntegerField("Ano de publicação da obra", null=False)
    # criar validação para o maior valor ser o ano corrente e o menor 100
    edicao  = models.PositiveSmallIntegerField("Número da edição da obra", default=1, null=False)
    isbn  = models.CharField('Número do ISBN da obra', max_length=20, null=True, blank=True)   # se for livro
    issn  = models.CharField('Número do ISSN da obra', max_length=20, null=True, blank=True)   # se for periódico
    quantidade = models.PositiveSmallIntegerField('Quantidade de unidades', default=1, null=False)
    tipo  = models.CharField("Tipo de obra", max_length=10, null=False, choices=TipoObra.choices)
    datacadastro = models.DateTimeField("Data de registro da obra",auto_now_add=True,null=False,db_index=True)
    dataatualizacao = models.DateTimeField("Data de modificação no registro da obra",auto_now_add=True,null=False)
    categoria = models.ForeignKey (Categoria, verbose_name=("Categoria"), on_delete=models.CASCADE,null=False)
    autor =  models.ForeignKey (Autor, verbose_name=("Autor"), on_delete=models.CASCADE,null=False)
    editora = models.ForeignKey (Editora, verbose_name=("Editora"), on_delete=models.CASCADE,null=False)
    
    def __str__(self):
        return self.titulo    
    
    def get_absolute_url(self):
        return reverse ("obra",args=[str(self.id)]) 
    
    def mostra_categoria(self):
        return ', '.join(categoria.descricao for categoria in self.categoria.all()[:1])
    mostra_categoria.short_description = "Categoria"
        
    # define as configurações da classe Meta (dados de BD)
    class Meta:
        db_table = "tb_obra"
        ordering = ["titulo","-datacadastro"] # traz por padrão os registros ordenados pelo título e data de registro decrescente
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        permissions = [
            ("can_view_obra", "Can view obras"),
            ("can_change_obra", "Can change obras"),
            ("can_add_obra", "Can add obras"),
            ("can_delete_obra", "Can delete obras"),
        ]

# Definição do modelo de Unidade (de obra)
class Unidade (models.Model):
    TipoDisponibilidade = models.TextChoices("Tipo disponibilidade","INTERNO INDISPONÍVEL EMPRÉSTIMO")
    obra = models.ForeignKey(Obra, verbose_name=("Obra"), on_delete=models.CASCADE)
    disponibilidade = models.CharField(max_length = 15, null=False, choices=TipoDisponibilidade.choices)
    datainclusao = models.DateTimeField("Data de inclusão da unidade da obra",auto_now_add=True,null=False)
     
    def __str__(self):
        return f"{self.obra.titulo} - {self.disponibilidade}"
    
    def get_absolute_url(self):
        return reverse ("unidade",args=[str(self.id)]) 
    
    def mostra_obra(self):
        return ', '.join(obra.titulo for obra in self.obra.all()[:1])
    mostra_obra.short_description = "Obra"
        
    # define as configurações da classe Meta (dados de BD)
    class Meta:
        db_table = "tb_unidade"
        ordering = ["disponibilidade","-datainclusao"] # traz por padrão os registros ordenados pelo disponibilidade e data de inclusão decrescente
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        permissions = [
            ("can_view_unidade", "Can view unidades"),
            ("can_change_unidade", "Can change unidades"),
            ("can_add_unidade", "Can add unidades"),
            ("can_delete_unidade", "Can delete unidades"),
        ]


# Definição do modelo de Emprestimo
class Emprestimo(models.Model):
    pessoa = models.ForeignKey (Pessoa, verbose_name=("Pessoa"), on_delete=models.CASCADE,)
    obras = models.ManyToManyField (Obra)
    #usuario = models.ForeignKey (User,on_delete=models.CASCADE,)
    #usuario = models.ForeignKey ("Usuário que relaizou o empréstimo",models.CharField,null=False)
    dataemprest = models.DateTimeField ("Data do empréstimos",auto_now_add=True, null=False)
    prazo = models.PositiveSmallIntegerField("Prazo do empréstimo em dias", default=10)
    # criar regra de validação para os prazos entre min=10, max=90
    data_devol = models.DateTimeField("Data da efetiva devolução", null=True)
    
    # define as configurações da classe Meta (dados de BD)
    class Meta:
        db_table = "tb_emprestimo"
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        permissions = [
            ("can_view_emprestimo", "Can view emprestimos"),
            ("can_change_emprestimo", "Can change emprestimos"),
            ("can_add_emprestimo", "Can add emprestimos"),
            ("can_delete_emprestimo", "Can delete emprestimos"),
        ]


# Definição do modelo de Reserva
class Reserva(models.Model):
    SituacaoReserva = models.TextChoices("Situação reserva","ATIVA CANCELADA EXPIRADA")
    pessoa = models.ForeignKey(Pessoa, verbose_name=("Pessoa"), on_delete=models.CASCADE,)
    obra = models.ManyToManyField(Obra, verbose_name=("Obra"))
    situacaoreserva = models.CharField(max_length = 10, default="ATIVA", null=False)
    datareserva = models.DateTimeField ("Data da reserva",auto_now_add=True, null=False)
    
    # retornar o valor padrão para a classe
    def __str__(self):
        return f"{self.pessoa.nome} - {self.obra.titulo}: {self.datareserva} - {self.situacaoreserva}"
 
    # define o nome padrão da tabela a ser criada no BD
    class Meta:
        db_table = "tb_reserva"
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        permissions = [
            ("can_view_reserva", "Can view reservas"),
            ("can_change_reserva", "Can change reservas"),
            ("can_add_reserva", "Can add reservas"),
            ("can_delete_reserva", "Can delete reservas"),
        ]

# Definição do modelo de papel
#class Papel(models.Model):
#    nome = models.CharField("Papel", max_length=50, null=False, unique=True)
#    descricao = models.CharField("Descrição", max_length=200, null=False)
#    
#    # retornar o valor padrão para a classe
#    def __str__(self):
#        return f"{self.nome} - {self.descricao}"
# 
#    # define o nome padrão da tabela a ser criada no BD
#    class Meta:
#        db_table = "tb_papel"


# Definição do modelo de usuario
#class Usuario(models.Model):
#    pessoa = models.ForeignKey (Pessoa,on_delete=models.CASCADE,)
#    papel = models.ForeignKey (Papel,on_delete=models.CASCADE,)
#    inicio = models.DateTimeField ("Início do período de validadade do papel",auto_now_add=True)
#    fim = models.DateTimeField ("Final do período", null=True)
#
#    # retornar o valor padrão para a classe
#    def __str__(self):
#        return f"{self.pessoa}/{self.papel}-{self.inicio}"
#
#    # define o nome padrão da tabela a ser criada no BD
#    class Meta:
#        db_table = "tb_usuario"
