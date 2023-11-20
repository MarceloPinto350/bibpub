# Generated by Django 4.2.7 on 2023-11-17 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibpub', '0003_alter_categoria_options_alter_categoria_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do autor')),
                ('nascimento', models.DateField(null=True, verbose_name='Data de nascimento')),
                ('biografia', models.TextField(max_length=1000, verbose_name='Biografia do autor')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'tb_autor',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome da editora')),
                ('email', models.CharField(max_length=254, verbose_name='E-Mail de contato da editora')),
                ('pais', models.CharField(max_length=100, verbose_name='Pas da editora')),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
                'db_table': 'tb_editora',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('nascimento', models.DateField(verbose_name='Data nascimento')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('I', 'Intersexo'), ('N', 'Não informado')], default='N', max_length=1, verbose_name='Sexo')),
                ('genero', models.IntegerField(choices=[(1, 'Cisgênero'), (2, 'Transgênero'), (3, 'Transexual'), (4, 'Travesti'), (5, 'Gênero fluido'), (6, 'Agênero'), (7, 'Outra'), (8, 'Não informado')], default=1, verbose_name='Identidade de Gênero')),
                ('eMail', models.CharField(max_length=254, verbose_name='E-Mail')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('AC', 'Ac'), ('AL', 'Al'), ('AP', 'Ap'), ('AM', 'Am'), ('BA', 'Ba'), ('CE', 'Ce'), ('DF', 'Df'), ('ES', 'Es'), ('GO', 'Go'), ('MA', 'Ma'), ('MT', 'Mt'), ('MS', 'Ms'), ('MG', 'Mg'), ('PA', 'Pa'), ('PB', 'Pb'), ('PR', 'Pr'), ('PE', 'Pe'), ('PI', 'Pi'), ('RJ', 'Rj'), ('RO', 'Ro'), ('RR', 'Rr'), ('SC', 'Sc'), ('SP', 'Sp'), ('SE', 'Se'), ('TO', 'To')], max_length=2, verbose_name='Unidade da federação')),
                ('cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro')),
                ('origem', models.CharField(choices=[('Internet', 'Internet'), ('Aplicação', 'Aplicação')], max_length=10, verbose_name='Origem do cadastro da pessoa')),
                ('situacaocadastro', models.CharField(choices=[('Ativo', 'Ativo'), ('Pendente', 'Pendente'), ('Suspenso', 'Suspenso'), ('Cancelado', 'Cancelado')], max_length=10, verbose_name='Situação do cadastro da pessoa')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'db_table': 'tb_pessoa',
                'permissions': [('can_view_pessoa', 'Pode ver pessoas'), ('can_change_pessoa', 'Pode alterar pessoas'), ('can_add_pessoa', 'Pode adicionar pessoas'), ('can_delete_pessoa', 'Pode apagar pessoas')],
            },
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='tb_categoria',
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True, verbose_name='Título da obra')),
                ('anopublicacao', models.PositiveSmallIntegerField(verbose_name='Ano de publicação da obra')),
                ('edicao', models.PositiveSmallIntegerField(default=1, verbose_name='Número da edição da obra')),
                ('isbn', models.CharField(null=True, max_length=20, verbose_name='Número do ISBN da obra')),
                ('issn', models.CharField(null=True, max_length=20, verbose_name='Número do ISSN da obra')),
                ('tipo', models.CharField(choices=[('Livro', 'Livro'), ('Periódico', 'Periódico'), ('Jornal', 'Jornal'), ('Outro', 'Outro')], max_length=10, verbose_name='Tipo de obra')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibpub.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibpub.categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibpub.editora')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
                'db_table': 'tb_obra',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprest', models.DateTimeField(auto_now_add=True, verbose_name='Data do empréstimos')),
                ('prazo', models.PositiveSmallIntegerField(default=10, verbose_name='Prazo do empréstimo em dias')),
                ('data_devol', models.DateTimeField(null=True, verbose_name='Data da efetiva devolução')),
                ('obras', models.ManyToManyField(to='bibpub.obra')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibpub.pessoa')),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
                'db_table': 'tb_emprestimo',
            },
        ),
    ]
