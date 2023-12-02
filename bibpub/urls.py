"""bibpub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

admin.site.site_header = 'Biblioteca Pública'
admin.site.site_title = 'Biblioteca Pública'
admin.site.index_title = 'Bem-vindo ao Painel Administrativo'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path ("",views.index, name="index"),
    # pessoa
    path("pessoa/", views.list_pessoa_view, name="list_pessoa_view"),
    path("pessoa/criar/", views.create_pessoa_view, name="create_pessoa_view"),
    path("pessoa/<int:pessoa_id>/", views.detail_pessoa_view, name="detail_pessoa_view"),
    path("pessoa/<int:pessoa_id>/update/", views.update_pessoa_view, name="update_pessoa_view"),
    path("pessoa/<int:pessoa_id>/delete/", views.delete_pessoa_view, name="delete_pessoa_view"),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('avaliar_cadastros/', views.avaliar_cadastros, name='avaliar_cadastros'),
    # reserva
    path ("reservas/", views.view_reservas, name="view_reservas"),
    path ('reservas/<int:pessoa_id>/', views.view_reservas_pessoa, name="view_reservas_pessoa"),    
    path ('obras_reserva/<int:reserva_id>/', views.obras_reserva, name="obras_reserva"),    
    # admin
    path("admin/", admin.site.urls),
]