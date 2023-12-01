from django import forms
from .models import Pessoa, Reserva

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'nascimento', 'cpf', 'sexo', 
                'genero', 'email', 'cep', 'endereco',
                'cidade', 'uf','origem', 'situacaocadastro']

# reservas
#class ReservaForm(forms.ModelForm):
#    class Meta:
#        model = Reserva
#        fields = ['pessoa', 'obra', 'situacaoreserva']
#        #exclude = ['datareserva']
#        all_reservas = Reserva.objects.all()
        

class CadastroPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'nascimento', 'cpf', 'sexo', 'genero', 'email', 'cep', 'endereco', 'cidade', 'uf', 'origem']
