from django.contrib import admin
from .models import Bebida

@admin.register(Bebida)
class BebidaAdmin(admin.ModelAdmin):
    # ATUALIZADO: Removemos 'gelada' da lista
    list_display = (
        'nome', 
        'categoria', 
        'preco_unidade', 
        'preco_fardo', 
        'disponivel'
    )
    
    # ATUALIZADO: Removemos 'gelada' dos filtros
    list_filter = ('categoria', 'disponivel')
    
    # ATUALIZADO: Removemos 'gelada' da edição rápida
    list_editable = (
        'preco_unidade', 
        'preco_fardo', 
        'disponivel'
    )
    
    search_fields = ('nome', 'categoria')