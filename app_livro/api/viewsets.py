#AGRUPAMENTO LÓGICO DA EXIBIÇÃO DE UM MODELO DE DADOS
from rest_framework import viewsets
from app_livro.api import serializers
from app_livro import models

class LivrosViewSet(viewsets.ModelViewSet):
    #RECEBE DOIS PARÂMETROS
    serializer_class = serializers.LivrosSerializer
    #TODOS OS CAMPOS DO MODELO
    queryset = models.Livros.objects.all()

