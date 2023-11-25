from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import User, Group
from .models import Categoria, Autor, Obra


class CustomAdminSite(admin.AdminSite):
    site_header = 'Biblioteca Pública'
    site_title = 'Biblioteca Pública'
    index_title = 'Bem-vindo à Biblioteca Pública'

admin.site = CustomAdminSite()

class CategoriaAdmin(ModelAdmin):
    list_display = ('descricao',)
    list_display_icons = True
    list_per_page = 20
    
admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(User)
admin.site.register(Group)
#class AutorAdmin(ModelAdmin):
#    list_display = ('nome','nascimento','biografia')
#    list_display_icons = True
#    list_per_page = 20

#admin.site.register(Autor,AutorAdmin)

#class ObraAdmin(ModelAdmin):
#    #categoria = models.ForeignKey 
#    #autor =  models.ForeignKey 
#    #editora = models.ForeignKey
#    list_display = ('titulo','anopublicacao','edicao','tipo','isbn','issn','datacadastro')
#    list_display_icons = True
#    list_per_page = 20

#admin.site.register(Obra,ObraAdmin)