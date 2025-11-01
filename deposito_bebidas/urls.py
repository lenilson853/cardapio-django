from django.contrib import admin
from django.urls import path

# 1. Importe a sua view do cardápio (como já tínhamos feito)
from cardapio.views import lista_bebidas

urlpatterns = [
    # 2. ESTA É A LINHA QUE ESTAVA FALTANDO!
    path('admin/', admin.site.urls),
    
    # 3. Esta é a linha da sua página principal (o cardápio)
    path('', lista_bebidas, name='home'),
]