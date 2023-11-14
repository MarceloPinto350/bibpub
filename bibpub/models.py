from django.db import models

class Categoria(models.Model):
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.descricao

    class Meta:
        permissions = [
            ("can_view_categoria", "Can view categorias"),
            ("can_change_categoria", "Can change categorias"),
            ("can_add_categoria", "Can add categorias"),
            ("can_delete_categoria", "Can delete categorias"),
        ]