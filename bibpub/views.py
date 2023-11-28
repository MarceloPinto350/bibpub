from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

# imports para uso dos modelos e templates criados
from django.template import loader
from django.http import Http404
from .models import Obra

def index(request):
    ultimas_obras_list = Obra.objects.order_by ("-datacadastro")[:5] 
    template = loader.get_template("index.html")
    context = {
        "ultimas_obras_list":ultimas_obras_list,
    }
    return HttpResponse (template.render(context,request))

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
