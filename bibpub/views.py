from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

# imports para uso dos modelos e templates criados
from django.template import loader
from django.http import Http404
from .models import Obra


@login_required()
def index(request):
    ultimas_obras_list = Obra.objects.order_by ("-datacadastro")[:5]
    quantidade_obras = Obra.objects.count()
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


