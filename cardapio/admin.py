from django.contrib import admin
from .models import Bebida

@admin.register(Bebida)
class BebidaAdmin(admin.ModelAdmin):
    # ATUALIZADO: Mostra os dois preços
    list_display = (
        'nome', 
        'categoria', 
        'preco_unidade', 
        'preco_fardo', 
        'disponivel', 
        'gelada'
    )
    
    list_filter = ('categoria', 'disponivel', 'gelada')
    
    # ATUALIZADO: Permite editar os dois preços
    list_editable = (
        'preco_unidade', 
        'preco_fardo', 
        'disponivel', 
        'gelada'
    )
    
    search_fields = ('nome', 'categoria')