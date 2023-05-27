#função para quando a rota for acessada

from django.shortcuts import render
##criando função e acessar dados da página com o 'request'
def home(request):
    #retornar a renderização a página, os dados e caminho da página html
    return render(request,'home.html')
