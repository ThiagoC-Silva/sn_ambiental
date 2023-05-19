# sn_ambiental
Projeto prático de implementação back end - Seleção para estágio na empresa SN Ambiental 

## COMO EXECUTAR A APLICAÇÃO

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
         }
    }
        
esse é o exemplo existente do DATABASES no meu projeto. Conforme a critério do avaliador, modificar as especificações acima.
       
-Crie todas as tabelas com a migração de dados:

python manage.py makemigrations 

python manage.py migrate

-Execute o seguinte comando para criar um superusuário do admin:

python manage.py createsuperuser

Siga as instruções e forneça um nome de usuário, endereço de e-mail (opcional) e senha para o superusuário.

-Inicie o servidor de desenvolvimento do Django executando o seguinte comando:

python manage.py runserver

-Acesse a aplicação em seu navegador no endereço http://127.0.0.1:8000/.

-Possível monitorar o banco de dados pelo arquivo bd.sql dentro do diretório principal sn_ambiental

# DECLARAÇÃO:

Sou acadêmico do primeiro período em Análise e Desenvolvimento de Sistemas 2023.1 no IFPI - Campus parnaíba. Minha base até iniciar o projeto se resumia a HTML, CSS, lógica de programação e JavaScript. Por isso, com o tempo que tive disponível de estudo, esse foi o máximo que pude extrair da implementação do que foi pedido no teste. Mesmo sem conhecimento prévio sobre grande parte do conteúdo,  acredito que esse esforço para concluir possa ser válido. Aprendi muito, e se, por consequência, ser selecionado para a vaga, creio que irei aprender muito mais.

