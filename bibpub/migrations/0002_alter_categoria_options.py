# Generated by Django 4.1.5 on 2023-11-14 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bibpub", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categoria",
            options={
                "permissions": [
                    ("can_view_categoria", "Can view categorias"),
                    ("can_change_categoria", "Can change categorias"),
                    ("can_add_categoria", "Can add categorias"),
                    ("can_delete_categoria", "Can delete categorias"),
                ]
            },
        ),
    ]
