from django import forms
from .models import Pessoa, Reserva, Obra   

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'nascimento', 'cpf', 'sexo', 
                'genero', 'email', 'cep', 'endereco',
                'cidade', 'uf','origem', 'situacaocadastro']

# reservas
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        #fields = ['pessoa', 'situacaoreserva', 'datareserva', 'obra']
        fields = ['pessoa', 'situacaoreserva', 'datareserva']
        #widgets = {
        #    'obra': forms.SelectMultiple(attrs={'size': 3}),
        #}
        #todas_reservas = Reserva.objects.all()
        


class CadastroPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'nascimento', 'cpf', 'sexo', 'genero', 'email', 
                  'cep', 'endereco', 'cidade', 'uf', 'origem']
