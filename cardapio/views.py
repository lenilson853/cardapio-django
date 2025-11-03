from django.shortcuts import render
from .models import Bebida # Importa seu modelo atualizado

def lista_bebidas(request):
    # 1. Pega TODAS as bebidas disponíveis
    bebidas_disponiveis = Bebida.objects.filter(disponivel=True)

    # 2. Pega TODAS as categorias que usamos no models.py
    #    (Isso é importante para manter a ordem correta)
    #    Ex: ['Cerveja Natural', 'Cerveja Gelada', 'Refrigerante Gelado', ...]
    categorias_ordenadas = [choice[0] for choice in Bebida.CATEGORIA_CHOICES]
    
    # 3. Cria o "dicionário" que o HTML precisa
    #    Ex: {'Cerveja Gelada': [lista de cervejas], 'Destilada': [lista de destiladas]}
    categorias = {}
    
    # 4. Adiciona as categorias na ordem certa
    for cat in categorias_ordenadas:
        # Adicionamos o .order_by('nome') aqui para garantir a ordem
        bebidas_da_categoria = bebidas_disponiveis.filter(categoria=cat).order_by('nome')
        
        # Só adiciona a categoria ao dicionário se ela tiver produtos disponíveis
        if bebidas_da_categoria.exists():
            categorias[cat] = bebidas_da_categoria

    # 5. Envia o dicionário 'categorias' para o HTML
    context = {
        'categorias': categorias
    }
    
    return render(request, 'cardapio/lista_bebidas.html', context)