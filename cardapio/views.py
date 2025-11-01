from django.shortcuts import render
from .models import Bebida

def lista_bebidas(request):
    # 1. Pega TODAS as bebidas disponíveis
    bebidas_disponiveis = Bebida.objects.filter(disponivel=True).order_by('nome')

    # 2. Pega TODAS as categorias que usamos no models.py
    #    (Isso é importante para manter a ordem correta)
    categorias_ordenadas = [choice[0] for choice in Bebida.CATEGORIA_CHOICES]
    
    # 3. Cria o "dicionário" que o HTML precisa
    #    Ex: {'Cerveja': [lista de cervejas], 'Destilada': [lista de destiladas]}
    categorias = {}
    
    # Adiciona as categorias principais na ordem certa
    for cat in categorias_ordenadas:
        bebidas_da_categoria = bebidas_disponiveis.filter(categoria=cat)
        # Só adiciona a categoria ao dicionário se ela tiver produtos
        if bebidas_da_categoria.exists():
            categorias[cat] = bebidas_da_categoria

    # 4. (Opcional) Adiciona a seção "Geladas" no FINAL
    #    (Ela pode conter itens que JÁ ESTÃO em outras categorias)
    bebidas_geladas = bebidas_disponiveis.filter(gelada=True)
    if bebidas_geladas.exists():
        categorias['Bebidas Geladas'] = bebidas_geladas
        
    # 5. Envia o dicionário 'categorias' para o HTML
    context = {
        'categorias': categorias
    }
    
    return render(request, 'cardapio/lista_bebidas.html', context)