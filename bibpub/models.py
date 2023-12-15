# immports do Django
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import EmailValidator, RegexValidator
from django.urls import reverse 

# outros imports usados
from datetime import date, timedelta, datetime
import re
from bibpub.utils import num_cpf_valido
from bibpub.validators import NascimentoValidator


# definições globais
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
SITUACAO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('ATIVO', 'Ativo'),
        ('SUSPENSO', 'Suspenso'),
        ('BLOQUEADO', 'Bloqueado'),
    ]
 
ESTADOS = [
        ("AC","Acre"),
        ("AL","Alagoas"),
        ("AP","Amapá"),
        ("AM","Amazonas"),
        ("BA","Bahia"),
        ("CE","Ceará"),
        ("DF","Distrito Federal"),
        ("ES","Espírito Santo"),
        ("GO","Goiás"),
        ("MA","Maranhão"),
        ("MT","Mato Grosso"),
        ("MS","Mato Grosso do Sul"),
        ("MG","Minas Gerais"),
        ("PA","Pará"),
        ("PB","Paraíba"),
        ("PR","Paraná"),
        ("PE","Pernambuco"),
        ("PI","Piauí"),
        ("RJ","Rio de Janeiro"),
        ("RN","Rio Grande do Norte"),
        ("RS","Rio Grande do Sul"),
        ("RO","Rondônia"),
        ("RR","Roraima"),
        ("SC","Santa Catarina"),
        ("SP","São Paulo"),
        ("SE","Sergipe"),
        ("TO","Tocantins"), 
    ]
     
 
#GRUPOS
grupo_coordenador, created = Group.objects.get_or_create(name='ADMIN')
grupo_operador, created = Group.objects.get_or_create(name='OPERADOR')
grupo_usuario, created = Group.objects.get_or_create(name='USUARIO')

# Classes
class Categoria(models.Model):
    descricao = models.CharField('Descrição', unique=True)

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
class Pessoa(models.Model):
    #Estados = models.TextChoices("Estados","AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PE PR PI RJ RN RO RR RS SC SP SE TO")
    OrigemCadastro = models.TextChoices("Origem cadastro" ,"INTERNET APLICAÇÃO")
    situacaocadastro = models.CharField(
        max_length=10,
        choices=SITUACAO_CHOICES,
        default='PENDENTE',
        verbose_name="Situação do cadastro",
    )
    nome = models.CharField("Nome", max_length=200, null=False,db_index=True)
    nascimento = models.DateField("Data nascimento")
    cpf = models.CharField("CPF", max_length=14, null=False, unique=True)
    sexo = models.CharField("Sexo", max_length=1, null=False, choices=OPC_SEXO,default="N")
    genero = models.IntegerField("Gênero", null=False, choices=OPC_GENERO,default=8)
    #email = models.CharField("E-Mail", max_length=254, null=False)
    # Verificar o uso do validador de e-mails
    email = models.CharField("E-Mail", max_length=254, null=False,validators=   [
                EmailValidator(message="Informe um e-mail válido!",
                code=None,
                allowlist=None)
            ])
    cep = models.CharField("CEP", max_length=9)
    # criar validador para CEP
    #cep = models.ForeignKey (ZipCode,on_delete=models.SET_NULL, blank=True, null=True,)
    endereco = models.CharField("Endereço", max_length=200, null=False)
    cidade = models.CharField("Cidade", max_length=200, null=False)
    uf = models.CharField("UF", max_length=2, null=False, choices=ESTADOS)
    cadastro = models.DateTimeField ("Data do cadastro",auto_now_add=True)
    origem = models.CharField("Origem do cadastro", max_length=10, null=False, default="INTERNET", choices=OrigemCadastro.choices)

    # retornar o valor padrão para a classe
    def __str__(self):
        return self.nome

    def cpf_valido(self):
        """Valida o CPF da pessoa"""
        regex = re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$")
        # TODO: validar o número do CPF
        #numValido = num_cpf_valido(num_cpf=self.cpf)
        #return re.match(regex,self.cpf) and num_cpf_valido(num_cpf=self.cpf)
        #validando só o formato
        return False if re.match(regex,self.cpf) == None else True
        
    def data_nascimento_valida(self):
        """Data de nascimento da pessoa retorna False para data de nascimento de hoje ou futura"""
        return self.nascimento < date.today()
    
    def email_valido(self):
        """Valida o e-mail da pessoa"""
        regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
        return True if re.match(regex, self.email) else False
    
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

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if self.situacaocadastro == 'ATIVO':
            user = User.objects.create(username=self.cpf)
            user.is_staff = True
            user.set_password('123')
            user.save()

            grupo_usuario, _ = Group.objects.get_or_create(name='Usuário')
            user.groups.add(grupo_usuario)


# Definição do modelo de Autor
class Autor(models.Model):
    nome = models.CharField("Nome do autor", max_length=200, null=False, unique=True)
    #nascimento = models.DateField("Data de nascimento", null=True)
    nascimento = models.DateField("Data de nascimento", null=True, validators = [
                    NascimentoValidator (message="Informe uma data de nascimento válida!",menorIdade=5)])
    biografia = models.TextField("Biografia do autor", max_length=1000, null=False)
 
    def __str__(self):
        return self.nome 

    def data_nascimento_valida(self):
        """Data de nascimento do autor retorna False caso a data seja futura ou menor que 5 anos"""
        return self.nascimento <= date.today()-timedelta(days=5*365) 
    
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


# Definição do modelo de Pais
class Pais(models.Model):
    codigo = models.CharField("Código do país", max_length=2, null=False, unique=True)
    nome = models.CharField("Nome do país", max_length=150, null=False, unique=True)
    datainicial = models.DateField("Data de início", null=False)
    datafinal = models.DateField("Data de término", null=True)
    
    # retornar o valor padrão para a classe
    def __str__(self):
        #return f"{self.codigo}-{self.nome}"
        return self.nome
 
    # define o nome padrão da tabela a ser criada no BD
    class Meta:
        db_table = "tb_pais"
        verbose_name = "País"
        verbose_name_plural = "Países"
        permissions = [
            ("can_view_pais", "Can view paises"),
            ("can_change_pais", "Can change paises"),
            ("can_add_pais", "Can add paises"),
            ("can_delete_pais", "Can delete paises"),
        ]


# Definição do modelo de Autor
class Editora(models.Model):
    nome = models.CharField("Nome da editora", max_length=200, null=False, unique=True)
    email = models.CharField("E-Mail editora", max_length=254, null=False)
    pais = models.ForeignKey(Pais, verbose_name=("País"), on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nome 
    
    def email_valido(self):
        """Valida o e-mail da editora"""
        regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
        return True if re.match(regex, self.email) else False
    
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
    descricao  = models.TextField("Resumo da obra", max_length=4000, null=True)
    isbn  = models.CharField('Número do ISBN da obra', max_length=20, null=True, blank=True)   # se for livro
    issn  = models.CharField('Número do ISSN da obra', max_length=20, null=True, blank=True)   # se for periódico
    #quantidade = models.PositiveSmallIntegerField('Quantidade de unidades', default=1, null=False)
    tipo  = models.CharField("Tipo de obra", max_length=10, null=False, choices=TipoObra.choices)
    datacadastro = models.DateTimeField("Data de registro da obra",auto_now_add=True,null=False,db_index=True)
    dataatualizacao = models.DateTimeField("Data de modificação no registro da obra",auto_now=True,null=False)
    categoria = models.ForeignKey (Categoria, verbose_name=("Categoria"), on_delete=models.CASCADE,null=False)
    autor =  models.ForeignKey (Autor, verbose_name=("Autor"), on_delete=models.CASCADE,null=False)
    editora = models.ForeignKey (Editora, verbose_name=("Editora"), on_delete=models.CASCADE,null=False)
    
    def __str__(self):
        return self.titulo    
    
    #def get_absolute_url(self):
    #    return reverse ("obra",args=[str(self.id)]) 
    
    def mostra_categoria(self):
        return ', '.join(categoria.descricao for categoria in self.categoria.all()[:1])
    mostra_categoria.short_description = "Categoria"
    
    def mostra_autor(self):
        return ', '.join(autor.nome for autor in self.autor.all()[:1])
    mostra_autor.short_description = "Autor"
    
    def get_unidades_disponiveis(self):
        return Unidade.objects.filter(disponibilidade="EMPRESTIMO",obra_id=self.id).count()
    get_unidades_disponiveis.short_description = "Unidades"
        
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
    TipoDisponibilidade = models.TextChoices("Tipo disponibilidade","INTERNO INDISPONIVEL EMPRESTIMO")
    obra = models.ForeignKey(Obra, verbose_name=("Obra"), on_delete=models.CASCADE)
    disponibilidade = models.CharField("Disponibilidade da unidade da obra", default="EMPRESTIMO", max_length = 15, null=False, choices=TipoDisponibilidade.choices)
    edicao  = models.PositiveSmallIntegerField("Número da edição da obra", default=1, null=False)
    datainclusao = models.DateTimeField("Data de inclusão",auto_now_add=True,null=False)
     
    def __str__(self):
        return self.obra.titulo
        #return self.mostra_obra()
        #return f"{self.obra.titulo} - {self.disponibilidade} - {self.edicao}"
    
    #def get_absolute_url(self):
    #    return reverse ("unidade",args=[str(self.id)]) 
    
    def mostra_obra(self):
        return ', '.join(obra.titulo for obra in self.obra.all()[:1])
    mostra_obra.short_description = "Obra"
    
    def get_quantidade_disponivel(self):
        return Unidade.objects.filter(disponibilidade="EMPRESTIMO").count()
    get_quantidade_disponivel.short_description = "Quantidade unidades disponível para empréstimo"
        
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
    datadevol = models.DateTimeField("Data da efetiva devolução", null=True)
    
    def __str__(self):
        return f"{self.pessoa.nome} - {self.obras.titulo}: {self.dataemprest}"
    
    def mostra_obras(self):
        return ', '.join(obra.titulo for obra in self.obras.all()[:1])
    
    def prazo_valido(self):
        """Valida o prazo do empréstimo"""
        return self.prazo >= 30 and self.prazo <= 90
    
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
    situacaoreserva = models.CharField("Situação da reserva",max_length = 10, default="ATIVA", null=False, choices=SituacaoReserva.choices)
    #datareserva = models.DateTimeField ("Data da reserva",auto_now_add=True, null=False)
    datareserva = models.DateTimeField ("Data da reserva",default=datetime.now(), null=False)
    
    # retornar o valor padrão para a classe
    def __str__(self):
        #return f"{self.pessoa.nome} - {self.obra.titulo}: {self.datareserva} - {self.situacaoreserva}"
        return self.situacaoreserva
    
    # define a url de retorno dos dados da reserva
    #def get_absolute_url(self):
    #    return reverse("reserva_view", args=[str(self.id)])
    
    def mostra_obras(self):
        return ', '.join(obra.titulo for obra in self.obra.all()[:1])
    
    # define o nome padrão da tabela a ser criada no BD
    class Meta:
        db_table = "tb_reserva"
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['pessoa','-datareserva']
        
        permissions = [
            ("can_view_reserva", "Can view reservas"),
            ("can_change_reserva", "Can change reservas"),
            ("can_add_reserva", "Can add reservas"),
            ("can_delete_reserva", "Can delete reservas"),
        ]
