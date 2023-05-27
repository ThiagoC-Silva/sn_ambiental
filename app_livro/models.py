#MODELO DOS DADOS NO BANCO DE DADOS
from django.db import models

class Livros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=35)
    autor = models.CharField(max_length=20)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=15)

