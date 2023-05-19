
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import Usuario, Emprestimo, Livro
from .serializers import UsuarioSerializer, EmprestimoSerializer, LivroSerializer

class ListaUsuarios(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]

class DetalhesUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ListaEmprestimos(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class DetalhesEmprestimo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class ListaLivros(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class DetalhesLivro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer