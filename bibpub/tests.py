# imports do python
from django.test import TestCase
from django.utils import timezone

from datetime import date, timedelta

from .models import Autor, Emprestimo, Editora, Pessoa


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
      """Prazo do empréstimo é de no máximo 365 dias, devendo retornar False para prazo superior a este limite"""
      prazo = 200
      emprestimo = Emprestimo(prazo=prazo)
      self.assertIs(emprestimo.prazo < 90, False)      
      