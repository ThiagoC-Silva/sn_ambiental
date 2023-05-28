#SERIALIZAÇÃO E DESSERIALIZAÇÃO - CONVERTER PARA MANIPULAR
from rest_framework import serializers
from app_livro import models

#CLASSE SERIALIZER:
class LivrosSerializer(serializers.ModelSerializer):
    #CLASSE INTERNA QUE RECEBE DOIS PARÂMETROS (model, campos-fields)
    class Meta:
        model = models.Livros
        fields = '__all__' #TODOS OS CAMPOS DO MODEL

