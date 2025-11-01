from django.contrib import admin
from django.urls import path
from cardapio.views import lista_bebidas  # <--- IMPORTE A SUA VIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_bebidas, name='home'), # <--- ADICIONE ESTA LINHA
]