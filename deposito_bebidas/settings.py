import os  # <-- MUDANÇA 1: Adicionado
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ===================================================================
# 👇 MUDANÇA 2: Configurações de Segurança para Produção
# ===================================================================

# IMPORTANTE: Cole sua chave secreta original (que começa com 'django-insecure-...')
# no lugar de '...'
SECRET_KEY = os.environ.get('SECRET_KEY', '3blwy7$^o1kuqjsvw68cem8_lt0))-gvj4p29gu13)tc24c7yt')

# O DEBUG será 'False' no servidor, mas 'True' se você rodar local
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# O '*' permite que o servidor do Render acesse seu site.
ALLOWED_HOSTS = ['*']
# ===================================================================


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cardapio', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- MUDANÇA 3: Adicionado
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deposito_bebidas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # (Está correto)
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

WSGI_APPLICATION = 'deposito_bebidas.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation (Não precisa mexer)
AUTH_PASSWORD_VALIDATORS = [
    # ... (pode deixar o que já estava aqui) ...
]


# Internationalization (Não precisa mexer)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===================================================================
# 👇 MUDANÇA 4: Configuração de Arquivos Estáticos para Produção
# ===================================================================
STATIC_URL = 'static/'

# Onde o Django vai procurar seus arquivos (CSS, JS) no seu PC
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Onde o 'collectstatic' vai juntar todos os arquivos para o servidor
STATIC_ROOT = BASE_DIR / 'staticfiles'

# O "motor" que o WhiteNoise usa para entregar os arquivos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ===================================================================


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'