#import datetime
from datetime import datetime
from .models import Obra, Categoria, Autor, Pais, Editora, Pessoa, Unidade, Reserva, Emprestimo, Pessoa, Obra
# imports do python
from django.test import TestCase
from django.utils import timezone

from datetime import date, timedelta

class AutorModelTests(TestCase):
   
   def test_data_nascimento_futura(self):
      """Data de nascimento do autor retorna False para data de nascimento futura"""
      nascimento = date.today() + timedelta(days=30)
      autor = Autor(nascimento=nascimento)
      self.assertIs(autor.data_nascimento_valida(), False)
      
   def test_data_nascimento_recente(self):
      """Data de nascimento do autor retorna False para data de nascimento < que 5 anos"""
      nascimento = date.today() - timedelta(days=5*200)
      autor = Autor(nascimento=nascimento)
      self.assertIs(autor.data_nascimento_valida(), False)


class EditoraModelTests(TestCase):
   
   def test_email_valido(self):
      """Email da editora retorna False para email fora do padrão"""
      email = "meuemail@"
      editora = Editora(email=email)
      self.assertIs(editora.email_valido(), False)


class PessoaModelTests(TestCase):
    def test_data_nascimento_futura(self):
        """Data de nascimento da pessoa retorna False para data de nascimento futura"""
        nascimento = date.today() + timedelta(days=30)
        pessoa = Pessoa(nascimento=nascimento)
        self.assertIs(pessoa.data_nascimento_valida(), False)

    def test_email_valido(self):
        """Email da pessoa retorna False para email fora do padrão"""
        email = "meuemail@"
        pessoa = Pessoa(email=email)
        self.assertIs(pessoa.email_valido(), False)

    def test_cpf_valido(self):
        """CPF da pessoa retorna False para CPF fora do padrão"""
        cpf = "111.111.111-00"
        pessoa = Pessoa(cpf=cpf)
        self.assertIs(pessoa.cpf_valido(), True)


class EmprestimoModelTests(TestCase):
    def test_prazo_inferior(self):
        """Prazo do empréstimo é de no mínimo 30 dias, devendo retornar False para prazo inferior a este limite"""
        prazo = 20
        emprestimo = Emprestimo(prazo=prazo)
        self.assertIs(emprestimo.prazo > 30, False)

    def test_prazo_superior(self):
        """Prazo do empréstimo é de no máximo 90 dias, devendo retornar False para prazo superior a este limite"""
        prazo = 200
        emprestimo = Emprestimo(prazo=prazo)
        self.assertIs(emprestimo.prazo < 90, False)
        
class CadastroPessoaTestCase(TestCase):
    def test_cadastro_pessoa_valida(self):
        response = self.client.post('/cadastrar_pessoa/', {
          'nome': 'Maria',
          'nascimento': '1990-01-01',
          'cpf': '123.456.789-09',
          'sexo': 'F',
          'genero': 8,
          'email': 'maria@imd.com',
          'cep': '12345678',
          'endereco': 'Rua Mossoro, 23',
          'cidade': 'Natal',
          'uf': 'RN',
          'origem': 'INTERNET',
        })
        self.assertEqual(response.status_code, 302)

        # Verifica se a pessoa foi cadastrada no banco de dados
        pessoa_cadastrada = Pessoa.objects.get(cpf='123.456.789-09')
        self.assertEqual(pessoa_cadastrada.situacaocadastro, 'PENDENTE')

    def test_cadastro_pessoa_invalida(self):
        # Tenta cadastrar uma pessoa com dados inválidos
        response = self.client.post('/cadastrar_pessoa/', {
             'nome': '',
             'nascimento': '',
             'cpf': '123.456.789-09',
             'sexo': 'M',
             'genero': 8,
             'email': 'usuario@gmail.com',
             'cep': '12345678',
             'endereco': 'Rua mossoro, 1234',
             'cidade': 'Natal',
             'uf': 'RN',
             'origem': 'INTERNET',
        })
        # Verifica se "erro" está presente no conteúdo da resposta
        self.assertIn('erro', response.content.decode('utf-8').lower())

        # Verifica se a pessoa não foi cadastrada no banco
        pessoa_cadastrada = Pessoa.objects.filter(cpf='12345678909').first()
        self.assertIsNone(pessoa_cadastrada)

class ObraTestCase(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(descricao='Categoria Teste')
        autor = Autor.objects.create(nome='Autor Teste')
        pais = Pais.objects.create(codigo='BR', nome='Brasil', datainicial=datetime.now())
        editora = Editora.objects.create(nome='Editora Teste', pais=pais)

        self.obra = Obra.objects.create(
            titulo='Obra Teste',
            anopublicacao=2022,
            descricao='Descrição da obra teste',
            isbn='1234567890',
            tipo=Obra.TipoObra.LIVRO,
            categoria=categoria,
            autor=autor,
            editora=editora
        )

    def test_consulta_obra(self):
        obra_consultada = Obra.objects.get(titulo='Obra Teste')

        self.assertEqual(obra_consultada.titulo, 'Obra Teste')
        self.assertEqual(obra_consultada.anopublicacao, 2022)
        self.assertEqual(obra_consultada.descricao, 'Descrição da obra teste')
        self.assertEqual(obra_consultada.isbn, '1234567890')
        self.assertEqual(obra_consultada.tipo, Obra.TipoObra.LIVRO)
        self.assertEqual(obra_consultada.categoria, self.obra.categoria)
        self.assertEqual(obra_consultada.autor, self.obra.autor)
        self.assertEqual(obra_consultada.editora, self.obra.editora)



class ReservaTestCase(TestCase):
    def setUp(self):
        dados_ficticios = {
            'situacaocadastro': 'PENDENTE',
            'nome': 'Pedro',
            'nascimento': datetime(1990, 1, 1),
            'cpf': '123.456.789-01',
            'sexo': 'M',
            'genero': 1,
            'email': 'pedro@gmail.com',
            'cep': '12345-678',
            'endereco': 'Rua imd, 123',
            'cidade': 'Natal',
            'uf': 'RN',
            'cadastro': datetime.now(),
            'origem': 'INTERNET',
        }
        pessoa = Pessoa.objects.create(**dados_ficticios)
        obra = Obra.objects.create(
            titulo='Obra Teste',
            anopublicacao=2022,
            descricao='Descrição da obra teste',
            isbn='1234567890',
            tipo=Obra.TipoObra.LIVRO,
            categoria=Categoria.objects.create(descricao='Categoria Teste'),
            autor=Autor.objects.create(nome='Autor Teste'),
            editora=Editora.objects.create(nome='Editora Teste',
                                           pais=Pais.objects.create(codigo='BR', nome='Brasil',
                                                                    datainicial=datetime.now()))
        )

    def test_reserva_obra(self):
        # Consulta a pessoa e a obra criadas no método setUp
        pessoa = Pessoa.objects.get(nome='Pedro')
        obra = Obra.objects.get(titulo='Obra Teste')

        # Cria uma reserva para a obra
        reserva = Reserva.objects.create(
            pessoa=pessoa,
            situacaoreserva=Reserva.SituacaoReserva.ATIVA,
            datareserva=datetime.now() + timedelta(days=1)
        )
        reserva.obra.add(obra)

        # Verifica se a reserva foi registrada
        self.assertEqual(reserva.pessoa, pessoa)
        self.assertEqual(reserva.situacaoreserva, Reserva.SituacaoReserva.ATIVA)
        self.assertIn(obra, reserva.obra.all())
        self.assertTrue(datetime.now() < reserva.datareserva)

        # Verifica se a obra foi associada corretamente à reserva
        self.assertIn(reserva, obra.reserva_set.all())


class EmprestimoTestCase(TestCase):
    def setUp(self):
        # Criando objetos necessários para os testes
        dados_ficticios = {
            'situacaocadastro': 'PENDENTE',
            'nome': 'joao',
            'nascimento': datetime(1990, 1, 1),
            'cpf': '123.456.789-01',
            'sexo': 'M',
            'genero': 1,
            'email': 'fulano@example.com',
            'cep': '12345-678',
            'endereco': 'Rua Principal, 123',
            'cidade': 'Cidade Exemplo',
            'uf': 'SP',
            'cadastro': datetime.now(),
            'origem': 'INTERNET',
        }

        pessoa = Pessoa.objects.create(**dados_ficticios)
        obra1 = Obra.objects.create(
            titulo='Livro 1',
            anopublicacao=2022,
            descricao='Descrição da obra 1',
            isbn='1234567890',
            tipo=Obra.TipoObra.LIVRO,
            categoria=Categoria.objects.create(descricao='Categoria 2'),
            autor=Autor.objects.create(nome='Autor 1'),
            editora=Editora.objects.create(nome='Editora 1',
                                           pais=Pais.objects.create(codigo='BR', nome='Brasil',
                                                                    datainicial=datetime.now()))
        )
        obra2 = Obra.objects.create(
            titulo='Livro 2',
            anopublicacao=2022,
            descricao='Descrição da obra 2',
            isbn='1234567890',
            tipo=Obra.TipoObra.LIVRO,
            categoria=Categoria.objects.create(descricao='Categoria 3'),
            autor=Autor.objects.create(nome='Autor 2'),
            editora=Editora.objects.create(nome='Editora 2',
                                           pais=Pais.objects.get(codigo='BR'))
        )

    def test_emprestimo_criado_corretamente(self):
        pessoa = Pessoa.objects.get(nome="joao")
        obras = Obra.objects.all()[:2]
        prazo = 10

        emprestimo = Emprestimo.objects.create(
            pessoa=pessoa,
            prazo=prazo,
        )
        emprestimo.obras.set(obras)

        self.assertEqual(emprestimo.pessoa.nome, "joao")
        self.assertEqual(emprestimo.obras.count(), 2)
        self.assertEqual(emprestimo.prazo, prazo)

    def test_devolucao_livro(self):
        pessoa = Pessoa.objects.get(nome="joao")
        obra = Obra.objects.first()

        emprestimo = Emprestimo.objects.create(
            pessoa=pessoa,
            prazo=10,
        )
        emprestimo.obras.add(obra)

        # Simula a devolução depois de 5 dias
        emprestimo.data_devol = timezone.now() + timezone.timedelta(days=5)
        emprestimo.save()

        self.assertIsNotNone(emprestimo.data_devol)


