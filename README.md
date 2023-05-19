# sn_ambiental
Projeto prático de implementação back end - Seleção para estágio na empresa SN Ambiental 
##COMO EXECUTAR A APLICAÇÃO
-Faça o download do projeto no GitHub.

-Extraia o arquivo compactado.

-Abra o terminal de comando e vá até o diretório do projeto.

-Ative o ambiente virtual Python:
. cmd Windows : sn_AmbienteVirtual\Scripts\activate
. gitbash : source sn_AmbienteVirtual/Scripts/activate


-Com o servidor MySQL ativado, crie a base de dados:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bibliotech_database',
        'USER': 'root',
        'PASSWORD': 'ads2000',
        'HOST': 'localhost',
        'PORT': ' 3306 ',
#esse é o exemplo existente do DATABASES no meu projeto. Conforme a critério do avaliador, modificar as especificações acima.
    }
}

-Crie todas as tabelas com a migração de dados:
python manage.py makemigrations 
python manage.py migrate

Execute o comando python manage.py runserver.

Acesse a aplicação em seu navegador no endereço http://127.0.0.1:8000/.
