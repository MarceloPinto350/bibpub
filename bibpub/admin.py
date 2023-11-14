from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Categoria

class CategoriaAdmin(ModelAdmin):
    list_display = ('descricao',)
    list_display_icons = True
    list_per_page = 20
admin.site.register(Categoria, CategoriaAdmin)