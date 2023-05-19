from django.db import models

# Criação dos modelos de dados das entidades

class Usuario(models.Model):
    vNome = models.CharField(max_length=80)
    dNascimento = models.DateField()
    vCpf = models.CharField(max_length=11)
    vEmail = models.CharField(max_length=50)


class Livro(models.Model):
    vTitulo = models.CharField(max_length=35)
    vAutor = models.CharField(max_length=20)
    iAno_publicacao = models.IntegerField()
    vEditora = models.CharField(max_length=15)


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dData_emprestimo = models.DateField()
    dData_devolucao = models.DateField()
