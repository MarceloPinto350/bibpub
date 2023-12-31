# Generated by Django 4.2.7 on 2023-11-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibpub', '0012_pais_rename_email_pessoa_email_alter_editora_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ['pessoa', 'datareserva'], 'permissions': [('can_view_reserva', 'Can view reservas'), ('can_change_reserva', 'Can change reservas'), ('can_add_reserva', 'Can add reservas'), ('can_delete_reserva', 'Can delete reservas')], 'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.IntegerField(choices=[(1, 'Cisgênero'), (2, 'Transgênero'), (3, 'Transexual'), (4, 'Travesti'), (5, 'Gênero fluido'), (6, 'Agênero'), (7, 'Outra'), (8, 'Não informado')], default=8, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='uf',
            field=models.CharField(choices=[('AC', 'Ac'), ('AL', 'Al'), ('AP', 'Ap'), ('AM', 'Am'), ('BA', 'Ba'), ('CE', 'Ce'), ('DF', 'Df'), ('ES', 'Es'), ('GO', 'Go'), ('MA', 'Ma'), ('MT', 'Mt'), ('MS', 'Ms'), ('MG', 'Mg'), ('PA', 'Pa'), ('PB', 'Pb'), ('PE', 'Pe'), ('PR', 'Pr'), ('PI', 'Pi'), ('RJ', 'Rj'), ('RN', 'Rn'), ('RO', 'Ro'), ('RR', 'Rr'), ('RS', 'Rs'), ('SC', 'Sc'), ('SP', 'Sp'), ('SE', 'Se'), ('TO', 'To')], max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='situacaoreserva',
            field=models.CharField(choices=[('ATIVA', 'Ativa'), ('CANCELADA', 'Cancelada'), ('EXPIRADA', 'Expirada')], default='ATIVA', max_length=10, verbose_name='Situação da reserva'),
        ),
    ]
