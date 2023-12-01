
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView

# imports para uso dos modelos e templates criados
from django.template import loader
from django.http import Http404
from .models import Obra, Unidade, Pessoa, Reserva
from .forms import PessoaForm   #, ReservaForm
from .forms import CadastroPessoaForm
from django.contrib import messages
from .decorators import groups_required


@login_required()
def index(request):
    ultimas_obras_list = Obra.objects.order_by ("-datacadastro")[:5]
    quantidade_obras = Unidade.objects.count()
    
    template = loader.get_template("index.html")
    context = {
        "ultimas_obras_list":ultimas_obras_list,
        "quantidade_obras": quantidade_obras,
    }
    return HttpResponse (template.render(context,request))

def custom_login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('index')
    return LoginView.as_view(template_name='bibpub/template/login.html')(request, **kwargs)

def obra(request,obra_id):
    try:
        obra = Obra.objects.get(obra_id)
    except Obra.DoesNotExist:
        raise Http404("Obra não está cadastrada.")
    return render(request,"obra.html",{"obra":obra})

# CRUD Pessoa
def create_pessoa_view(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_view')
    return render(request, 'pessoa_form.html', {'form': form})

def list_pessoa_view(request):
    items = Pessoa.objects.all()
    return render(request, 'pessoa_list.html', {'items': items})

def detail_pessoa_view(request, pessoa_id):
    item = get_object_or_404(Pessoa, id=pessoa_id)
    fields = [(field.name, field.value_to_string(item)) for field in item._meta.fields]
    return render(request, 'pessoa_detail.html', {'item': item})

def update_pessoa_view(request, pessoa_id):
    item = get_object_or_404(Pessoa, id=pessoa_id)
    form = PessoaForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list_view')
    return render(request, 'pessoa_form.html', {'form': form, 'item': item})

def delete_pessoa_view(request, pessoa_id):
    item = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == 'POST':
        item.delete()
        return redirect('pessoa_list_view')
    return render(request, 'pessoa_delete_confirm.html', {'item': item})

# Reservas
def view_reserva(request, reserva_id):
    reservas_ativas = Reserva.objects.filter(situacaoreserva='ATIVA')
    #reservas_expiradas = Reserva.objects.filter(situacaoreserva='EXPIRADA')
    template = loader.get_template("reserva_view.html")
    context = {
        "reservas_ativas":reservas_ativas,
    }
    return HttpResponse (template.render(context,request))


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = CadastroPessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.situacaocadastro = 'PENDENTE'
            pessoa.save()

            messages.success(request, 'Cadastro realizado com sucesso. Aguarde a análise.')
            return redirect('login')

    else:
        form = CadastroPessoaForm()

    return render(request, 'cadastrar_pessoa.html', {'form': form})

@groups_required(['Coordenador', 'Operador'])
def avaliar_cadastros(request):
    cadastros_pendentes = Pessoa.objects.filter(situacaocadastro='PENDENTE')
    if request.method == 'POST':
        for pessoa_id, status in request.POST.items():
            if pessoa_id.isdigit() and status in ['APROVAR', 'RECUSAR']:
                pessoa = Pessoa.objects.get(pk=int(pessoa_id))
                if status == 'APROVAR':
                    pessoa.situacaocadastro = 'ATIVO'
                else:
                    pessoa.situacaocadastro = 'BLOQUEADO'
                pessoa.save()
        messages.success(request, 'Análise realizada com sucesso.')
        return redirect('index')

    return render(request, 'avaliar_cadastros.html', {'cadastros_pendentes': cadastros_pendentes})
