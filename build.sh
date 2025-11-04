#!/usr/bin/env bash
# (Isso diz ao servidor para tratar este arquivo como um script)

# Sai se qualquer comando falhar
set -o errexit

# 1. Instala todas as peças da nossa lista
pip install -r requirements.txt

# 2. Coleta todos os seus arquivos (CSS, JS, imagens) em um só lugar
python manage.py collectstatic --no-input

# 3. Aplica as migrações no banco de dados (cria as tabelas)
python manage.py migrate