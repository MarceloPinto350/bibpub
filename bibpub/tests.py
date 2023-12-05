import datatime 

from django.test import TestCase
from django.utils import timezone

from .models import Autor, Emprestimo, Editora, Obra

class AutorModelTests(TestCase):
   
   def test_data_nascimento_futura(self):
      """Data de nascimento do autor retorna False para data de nascimento futura"""
      nascimento = timezone.now() + datetime.timedelta(days=30)
      autor = Autor(nascimento=nascimento)
      self.assertIs(autor.data_nascimento_valida(), False)
      
   def test_data_nascimento_recente(self):
      """Data de nascimento do autor retorna False para data de nascimento < que 5 anos"""
      nascimento = timezone.now() - datetime.timedelta(years=5)
      autor = Autor(nascimento=nascimento)
      self.assertIs(autor.data_nascimento_valida(), False)


class EditoraModelTests(TestCase):
   
   def test_email_vallido(self):
      """Email da editora retorna False para email fora do padrão"""
      email = "meuemail@com"
      self.assertIs(editora.email_valido(), False)
      
