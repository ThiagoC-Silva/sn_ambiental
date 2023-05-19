from django.db import models

# Criação dos modelos de dados das entidades

class Usuario(models.Model):
    Nome = models.CharField(max_length=80)
    Nascimento = models.DateField()
    Cpf = models.CharField(max_length=11)
    Email = models.CharField(max_length=50)


class Livro(models.Model):
    Titulo = models.CharField(max_length=35)
    Autor = models.CharField(max_length=20)
    Ano_publicacao = models.IntegerField()
    Editora = models.CharField(max_length=15)


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Data_emprestimo = models.DateField()
    Data_devolucao = models.DateField()
