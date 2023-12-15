from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NascimentoValidator:
   message = "Enter a valid birth date."
   menorIdade = 0
        
   def __init__(self, message=None, menorIdade=None):
      if message is not None:
         self.message = message
      if menorIdade is not None:
         self.menorIdade = menorIdade
    
   def __call__(self, value):
      # erros gerais de data
      #if not value or isinstance(value,date) :
      #   raise ValidationError(self.message, params={"value": value})
      
      # Não existe data de nascimento futura
      if value > date.today():
         raise ValidationError("Não existe data de nascimento futura.", params={"value": value})
      
      # O valor da idade mínimo aceita é de 0 anos, caso não seja informada outra data
      if value > date.today()-timedelta(days=self.menorIdade*365):
         raise ValidationError("A idade mínima permitida é de 5 anos.", params={"value": value})
      
        

