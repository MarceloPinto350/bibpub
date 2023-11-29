from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'nascimento', 'cpf', 'sexo', 
                'genero', 'email', 'cep', 'endereco',
                'cidade', 'uf','origem', 'situacaocadastro']
