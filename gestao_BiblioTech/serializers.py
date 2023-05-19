from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario, Emprestimo, Livro

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'