Tutorial

Passo a passo para criar as aplicações


# Instalar Django

# Início
mkdir folder
cd folder

# Cria um ambiente virtual isolado, do restante do seu sistema operacional
python3 -m venv env
source env/bin/activate

# Instalar Django e DRF
pip3 install django==3.2.5 (LTS atual)
pip install djangorestframework
pip install markdown (auxilia na documentação da API)
pip install django-filter (verificar a necessidade)
django-admin startproject project_name
cd project_name
python3 manage.py startapp app_name
python3 manage.py createsuperuser

# ADD txt do requirements
pip freeze > requirements.txt


# Default Config
Em project_folder/project_folder/settings.py
    Colocar os pacotes add no INSTALLED_APPS
        'django-filters',
        'rest_framework',
    Colocar o nome das aplicações em INSTALLED_APPS
    Alterar a linguagem em LANGUAGE_CODE para pt-br
    Alterar TIME_ZONE para America/Sao_Paulo
    Adicionar: 'STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')' no final do arquivo
    Adicionar: 'MEDIA_URL = 'media/'' no final do arquivo
    Adicionar: 'MEDIA_ROOT = os.path.join(BASE_DIR, 'media')" no final do arquivo


# Config para MySQL
terminal >  pip3 install mysqlclient
(talvez precisa instalar via apt: apt install default-libmysqld-dev)

Ex: do settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

se for mais de um banco:
DATABASES = {
    'default': {},
    'users': {
        'NAME': 'user_data',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'superS3cret'
    },
    'customers': {
        'NAME': 'customer_data',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_cust',
        'PASSWORD': 'veryPriv@ate'
    }
}
O DEFAULT em branco. Deve ser especificado o DB quando for executar o migrate
./manage.py migrate --database=customers




# MODELO DE MODEL
from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Post(Base):
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-created_at']


class Vote(Base):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



# MODELO DE SERIALIZER
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'created_at']
    
    
    


# MODELO DE VIEW
