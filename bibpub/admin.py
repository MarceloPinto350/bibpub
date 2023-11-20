from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bibpub.models import Editora
from .models import Categoria,Autor,Obra

class CategoriaAdmin(ModelAdmin):
    list_display = ('descricao',)
    list_display_icons = True
    list_per_page = 20

admin.site.register(Categoria, CategoriaAdmin)

class AutorAdmin(ModelAdmin):
    list_display = ('nome', 'nascimento', 'biografia')
    list_display_icons = True
    list_per_page = 20

admin.site.register(Autor, AutorAdmin)

class ObraAdmin(ModelAdmin):
    #categoria = models.ForeignKey 
    #autor =  models.ForeignKey 
    #editora = models.ForeignKey
    list_display = ('titulo', 'anopublicacao', 'edicao', 'tipo', 'isbn', 'issn', 'datacadastro')
    list_display_icons = True
    list_per_page = 20

admin.site.register(Obra, ObraAdmin)

class EditoraAdmin(ModelAdmin):
    list_display = ('nome', 'email', 'pais')
    list_display_icons = True
    list_per_page = 20

admin.site.register(Editora, EditoraAdmin)