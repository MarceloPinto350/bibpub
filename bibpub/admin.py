from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import User, Group
from .models import Categoria, Autor, Obra, Unidade, Pais, Editora, Pessoa, Reserva #, ReservaObra

class CustomAdminSite(admin.AdminSite):
    site_header = 'Biblioteca Pública'
    site_title = 'Biblioteca Pública'
    index_title = 'Bem-vindo à Biblioteca Pública'

admin.site = CustomAdminSite()

class CategoriaAdmin(ModelAdmin):
    list_display = ('descricao',)
    list_display_icons = True
    list_per_page = 10
    
admin.site.register(Categoria, CategoriaAdmin)

# registando o Autor
class AutorAdmin(ModelAdmin):
    list_display = ('nome','nascimento','biografia')
    list_display_icons = True
    list_per_page = 10
admin.site.register(Autor,AutorAdmin)

#registrando a Editora
class EditoraAdmin(ModelAdmin):
    list_display = ('nome','email',) # 'pais',)
    list_display_icons = True
    list_per_page = 10
admin.site.register(Editora,EditoraAdmin)   

# registrando a Obra
class UnidadeEmLinha(admin.TabularInline):
    model = Unidade 
    list_per_page = 10
    readonly_fields = ('obra','datainclusao',)
    extra = 2

class ObraAdmin(ModelAdmin):
    list_display = ('titulo', 'anopublicacao', 'tipo', 'datacadastro', 'descricao',) #, 'mostra_categoria', 'mostra_autor')
    list_filter = ('titulo', 'autor')
    search_fields = ['titulo', 'autor__nome']
    inlines = [UnidadeEmLinha]
    list_display_icons = True
    list_per_page = 10

    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(Obra,ObraAdmin)

# registrando o Pais
class PaisAdmin(ModelAdmin):
    list_display = ('codigo','nome','datainicial','datafinal',)
    list_display_icons = True
    list_per_page = 10
admin.site.register(Pais,PaisAdmin)    

# registrando a Reserva    
class ReservaAdmin(ModelAdmin):
    list_display = ('pessoa','datareserva','situacaoreserva',)
    list_display_icons = True
    list_per_page = 10
    #filter = (ObraAdmin.get_unidades_disponiveis(self.obra_id) > 0)
    readonly_fields = ('situacaoreserva','datareserva',)
    #inlines = [ObraEmLinha]
admin.site.register(Reserva,ReservaAdmin)

#   acrescetando as reservas feitas para a pessoa
class ReservaEmLinha(admin.TabularInline):
    model = Reserva
    extra = 0
    max_num = 10
    ordering   = ('situacaoreserva','-datareserva',)
    readonly_fields = ('obra','situacaoreserva','datareserva')
    can_delete = False 
    
class PessoaAdmin(ModelAdmin):
    list_display = ('nome', 'nascimento', 'cpf', 'sexo', 
                    'genero', 'email', 'cep', 'endereco',
                    'cidade', 'uf', 'cadastro', 'origem',
                    'situacaocadastro')
    list_display_icons = True
    list_per_page = 10
    inlines = [ReservaEmLinha]  
admin.site.register(Pessoa, PessoaAdmin)

admin.site.register(User)
admin.site.register(Group)
