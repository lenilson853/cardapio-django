# 🍺 Depósito do Matuto - Cardápio Digital com WhatsApp

Este é um sistema web completo para gestão de um depósito de bebidas, permitindo que clientes visualizem um cardápio dinâmico e enviem pedidos completos diretamente para o WhatsApp do proprietário.

## ✨ Funcionalidades Principais

O projeto foi desenvolvido em duas partes principais: a **Área Pública** (para clientes) e o **Painel Administrativo** (para o dono).

### 🏪 Para o Cliente (Cardápio Público)

* **Cardápio Dinâmico:** Os produtos são carregados diretamente do banco de dados e organizados por categorias (Ex: "Refrigerantes", "Naturais", "Cervejas").
* **Preços Flexíveis:** O sistema exibe preços por **Unidade** e por **Fardo/Caixa**, permitindo ao cliente escolher a opção que deseja.
* **Carrinho de Compras (JavaScript):** O cliente pode adicionar múltiplos itens (unidades ou fardos) ao seu pedido.
* **Revisão de Pedido (Modal Pop-up):** Um pop-up limpo permite que o cliente revise todos os itens, veja o preço total e preencha os dados de entrega.
* **Checkout Completo:**
    * Coleta de **Endereço de Entrega** (Rua, Número, Bairro, Referência).
    * Seleção de **Forma de Pagamento** (Pix, Dinheiro, Cartão).
* **Integração com WhatsApp:** Ao finalizar, o sistema valida os campos, formata uma mensagem completa com todos os itens, o total e o endereço, e a envia para o WhatsApp do depósito.

### 👨‍💼 Para o Dono (Painel Admin)

* Acesso seguro ao painel `/admin/`.
* **Gestão Total de Produtos:**
    * Adicionar, editar ou remover bebidas.
    * Definir preços de **unidade** e **fardo** separadamente (deixando um em branco, se necessário).
    * Organizar produtos por categorias personalizadas (o cardápio se atualiza sozinho).
    * Marcar produtos como "Disponível" ou "Indisponível" (controle de estoque).
    * Marcar produtos como "Gelada" (para aparecer em categorias especiais).

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Django 5.x
* **Frontend:** HTML5, CSS3 (com Flexbox), JavaScript (Vanilla JS)
* **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)
* **Controle de Versão:** Git & GitHub

## 🚀 Como Rodar Localmente

1.  Clone este repositório.
2.  Entre na pasta do projeto: `cd meu_deposito`
3.  Crie um ambiente virtual: `python -m venv venv`
4.  Ative o ambiente: `venv\Scripts\activate` (Windows)
5.  Instale as dependências: `pip install -r requirements.txt`
6.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7.  Crie um superusuário (para acessar o `/admin/`): `python manage.py createsuperuser`
8.  Rode o servidor de desenvolvimento: `python manage.py runserver`
9.  Acesse o site em `http://127.0.0.1:8000/`