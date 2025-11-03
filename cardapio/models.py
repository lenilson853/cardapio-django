from django.db import models

class Bebida(models.Model):
    # ===================================================================
    # 👇 MUDANÇA PRINCIPAL AQUI 👇
    # ===================================================================
    # Esta é a sua nova lista de categorias, na ordem que você pediu
    CATEGORIA_CHOICES = [
        ('Cerveja Natural', 'Cerveja Natural'),     # 1. (Temperatura ambiente)
        ('Cerveja Gelada', 'Cerveja Gelada'),       # 2.
        ('Refrigerante Gelado', 'Refrigerante Gelado'), # 3.
        ('Refrigerante Natural', 'Refrigerante Natural'), # 4. (Temperatura ambiente)
        ('Destilada', 'Destilada'),                   # 5. (Permanece)
        # (Você pode adicionar 'Sucos' ou 'Água' aqui se precisar)
    ]
    # ===================================================================

    nome = models.CharField(max_length=100, verbose_name="Nome do Produto (ex: Coca-Cola Lata 350ml)")

    preco_unidade = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name="Preço (Unidade)",
        null=True,
        blank=True
    )
    
    preco_fardo = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name="Preço (Fardo/Caixa)",
        null=True,
        blank=True
    )
    
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
    
    # ===================================================================
    # 👇 CAMPO REMOVIDO 👇
    # 'gelada = models.BooleanField(...)' FOI APAGADO.
    # ===================================================================

    disponivel = models.BooleanField(
        default=True, 
        verbose_name="Disponível para venda"
    )

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"
        ordering = ['nome'] # Vamos ordenar por nome

    def __str__(self):
        return self.nome