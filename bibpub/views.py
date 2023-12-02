
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView

# imports para uso dos modelos e templates criados
from django.template import loader
from django.http import Http404

from bibpub.models import Editora
from .models import Obra, Unidade, Pessoa, Reserva
from .forms import PessoaForm, ReservaForm
from .forms import CadastroPessoaForm
from django.contrib import messages
from .decorators import groups_required


@login_required()
def index(request):
    ultimas_obras_list = Obra.objects.order_by ("-datacadastro")[:5]
    quantidade_obras = Obra.objects.count()
    quantidade_editoras = Editora.objects.count()
    quantidade_pessoas = Pessoa.objects.count()
    template = loader.get_template("index.html")
    context = {
        "ultimas_obras_list":ultimas_obras_list,
        "quantidade_obras": quantidade_obras,
        "quantidade_editoras": quantidade_editoras,
        "quantidade_pessoas": quantidade_pessoas,
    }
    return HttpResponse (template.render(context,request))

def custom_login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('index')
    return LoginView.as_view(template_name='bibpub/template/login.html')(request, **kwargs)

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


############################################################################################################
# Reservas
############################################################################################################
@login_required()
def criar_reserva(request):
    criar_reserva = Reserva.objects.filter(pessoa=request.user.pessoa)
    #criar_reserva = Reserva.objects.filter(situacaoreserva='ATIVA')
    #criar_reserva = Reserva.objects.all()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            if not request.user.groups.filter(name__in=['ADMIN', 'OPERADOR']).exists():                
                reserva.pessoa = request.user.pessoa
            reserva.situacaoreserva = 'PENDENTE'
            reserva.save()
            messages.success(request, 'Reserva realizada com sucesso.')
            return redirect('index')
        else:
            messages.warning(request, 'Não foi possível realizar a reserva.')
            return redirect('index')   
    else:
        form = ReservaForm()
        
    template = loader.get_template("criar_reserva.html")
    context = {
        "form":criar_reserva,
    }
    return HttpResponse (template.render(context,request))
    

@login_required()
def view_reservas(request):
    reservas = Reserva.objects.all()
    template = loader.get_template("reservas.html")
    context = {
        "reservas":reservas,
    }
    return HttpResponse (template.render(context,request))

@login_required()
def view_reservas_pessoa(request, pessoa_id=None):
    if pessoa_id == None:
        pessoa_id = request.user.id
    pessoa = Pessoa.objects.get(id=pessoa_id)    
    reservas_pessoa  = Reserva.objects.filter(pessoa=pessoa)
    # validar se o usuário é a pessoa que está sendo consultada ou o usuário é administrador ou operador para mostrar a lista de reservas
    if ((request.user.is_superuser or request.user.groups.filter(name__in=['Operador','Coordenador']).exists()) and pessoa_id != request.user.id) or pessoa_id != request.user.id:
        messages.warning(request, 'O usuário só pode consultar as suas próprias reservas.')
        return redirect('index')
    if True:    
        template = loader.get_template("reservas_pessoa.html")
        context = {
            "reservas_pessoa":reservas_pessoa,
        }
        return HttpResponse (template.render(context,request))
    else:
        messages.warning(request, 'O usuário só pode consultar as suas próprias reservas.')
        return redirect('index')


def obras_reserva(request,reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    obras_reserva = Obra.objects.filter(reserva=reserva)
    template = loader.get_template("obras_reserva.html")
    context = {
        "obras_reserva":obras_reserva,
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

@groups_required(['ADMIN', 'OPERADOR'])
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
