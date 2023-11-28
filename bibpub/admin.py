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

# registando o Autor
class AutorAdmin(ModelAdmin):
    list_display = ('nome','nascimento','biografia')
    list_display_icons = True
    list_per_page = 20

admin.site.register(Autor,AutorAdmin)

# registrando a Obra
class ObraAdmin(ModelAdmin):
    #categoria = models.ForeignKey 
    #autor =  models.ForeignKey 
    #editora = models.ForeignKey
    list_display = ('titulo', 'anopublicacao', 'edicao', 'tipo', 'quantidade', 'datacadastro')
    list_filter = ('titulo', 'autor')
    search_fields = ['titulo', 'autor__nome']
    list_display_icons = True
    list_per_page = 20

    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(Obra,ObraAdmin)

admin.site.register(User)
admin.site.register(Group)