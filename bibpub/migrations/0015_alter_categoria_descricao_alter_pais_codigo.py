# Generated by Django 4.2.7 on 2023-12-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bibpub", "0014_alter_pessoa_origem_alter_pessoa_situacaocadastro_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.CharField(unique=True, verbose_name="Descrição"),
        ),
    ]