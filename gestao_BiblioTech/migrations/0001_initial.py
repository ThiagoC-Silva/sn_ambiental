# Generated by Django 4.2.1 on 2023-05-19 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vTitulo', models.CharField(max_length=35)),
                ('vAutor', models.CharField(max_length=20)),
                ('iAno_publicacao', models.IntegerField()),
                ('vEditora', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vNome', models.CharField(max_length=80)),
                ('dNascimento', models.DateField()),
                ('vCpf', models.CharField(max_length=11)),
                ('vEmail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dData_emprestimo', models.DateField()),
                ('dData_devolucao', models.DateField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_BiblioTech.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_BiblioTech.usuario')),
            ],
        ),
    ]
