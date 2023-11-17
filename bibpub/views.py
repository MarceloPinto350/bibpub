from django.shortcuts import render
from django.http import HttpResponse

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


