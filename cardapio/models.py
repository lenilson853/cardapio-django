from django.db import models

class Bebida(models.Model):
    # ATUALIZADO: Lista final e limpa de categorias
    CATEGORIA_CHOICES = [
        ('Refrigerantes', 'Refrigerantes'), # (Coca-Cola, Guaraná, Água, etc.)
        ('Natural', 'Natural'),           # (Sucos naturais)
        ('Cerveja', 'Cerveja'),
        ('Destilada', 'Destilada'),
        # ('Vinho', 'Vinho/Espumante'),  <-- REMOVIDO CONFORME SEU PEDIDO
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Produto (ex: Coca-Cola Lata 350ml)")

    # --- MUDANÇA PRINCIPAL AQUI ---
    # Apagamos o 'preco' antigo
    # Adicionamos 'preco_unidade' (pode ser opcional)
    preco_unidade = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name="Preço (Unidade)",
        null=True, # Permite que o campo fique em branco
        blank=True # Permite que seja opcional no Admin
    )
    
    # Adicionamos 'preco_fardo' (também opcional)
    preco_fardo = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name="Preço (Fardo/Caixa)",
        null=True,
        blank=True
    )
    # --- FIM DA MUDANÇA ---
    
    # Adicionamos uma descrição para o fardo (ex: "Fardo (12 unidades)")
    descricao_fardo = models.CharField(
        max_length=50, 
        verbose_name="Descrição do Fardo",
        default="Fardo (12 unidades)",
        null=True,
        blank=True
    )
    
    categoria = models.CharField(
        max_length=50, 
        choices=CATEGORIA_CHOICES, 
        verbose_name="Categoria"
    )
    
    gelada = models.BooleanField(
        default=True,
        verbose_name="Está Gelada?"
    )

    disponivel = models.BooleanField(
        default=True, 
        verbose_name="Disponível para venda"
    )

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"
        ordering = ['nome']

    def __str__(self):
        return self.nome