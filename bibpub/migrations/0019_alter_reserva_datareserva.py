# Generated by Django 4.2.7 on 2023-12-15 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibpub', '0018_alter_autor_nascimento_alter_reserva_datareserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='datareserva',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 20, 8, 57, 711359), verbose_name='Data da reserva'),
        ),
    ]
