import os
from pathlib import Path # Garanta que esta linha existe

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 
# 👇 GARANTA QUE ESTE BLOCO DE CÓDIGO EXISTA E ESTEJA CORRETO 👇
BASE_DIR = Path(__file__).resolve().parent.parent
# 👆 A LINHA MAIS IMPORTANTE 👆


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '...' # (Deixe a sua chave secreta original que já está aí)
DEBUG = True

# ... (o resto do arquivo) ...
# ... (deixe todo o resto do arquivo como está) ...

# 1. Adicione 'cardapio' à lista de INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cardapio',  # <--- ADICIONE ESTA LINHA
]
ROOT_URLCONF = 'deposito_bebidas.urls'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# ... (deixe o resto como está) ...

# 2. Configure o diretório de templates
#    Encontre a seção TEMPLATES e modifique a linha 'DIRS'
import os # Verifique se 'import os' ou 'from pathlib import Path' está no topo

# Se estiver usando 'from pathlib import Path', o BASE_DIR já existe.
# A configuração de TEMPLATES ficará assim:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # <--- MODIFIQUE ESTA LINHA
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ... (deixe todo o resto do arquivo como está) ...
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]