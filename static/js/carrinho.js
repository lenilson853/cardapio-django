// Espera o HTML carregar completamente
document.addEventListener("DOMContentLoaded", function() {

    // --- 1. O "CÉREBRO" (Onde guardamos os itens) ---
    let carrinho = {}; 

    // --- 2. "OS OLHOS" (Encontrar os elementos na página) ---
    const botoesAdicionar = document.querySelectorAll(".btn-adicionar");
    
    const modalOverlay = document.getElementById("modal-carrinho-overlay");
    const btnFecharModal = document.getElementById("btn-fechar-modal");
    const btnRevisarPedido = document.getElementById("btn-revisar-pedido");
    const btnFinalizar = document.getElementById("btn-finalizar-pedido");

    const carrinhoItensDiv = document.getElementById("itens-do-carrinho");
    const carrinhoTotalSpan = document.getElementById("total-preco");
    const totalItensSpan = document.getElementById("total-itens-carrinho");

    
    // --- 3. "OS OUVIDOS" (Ações do Usuário) ---

    // OUVIR cliques nos botões "Adicionar"
    botoesAdicionar.forEach(botao => {
        botao.addEventListener("click", function() {
            const nome = botao.dataset.nome;
            const preco = parseFloat(botao.dataset.preco);
            const quantidadeInput = botao.previousElementSibling;
            const quantidade = parseInt(quantidadeInput.value);

            // Usa o 'nome' como ID único no carrinho
            if (carrinho[nome]) {
                carrinho[nome].quantidade += quantidade;
            } else {
                carrinho[nome] = {
                    preco: preco,
                    quantidade: quantidade
                };
            }
            quantidadeInput.value = 1; 
            atualizarCarrinhoVisual(); 
        });
    });

    // OUVIR clique para ABRIR o modal
    btnRevisarPedido.addEventListener("click", function() {
        modalOverlay.classList.add("visivel");
    });

    // OUVIR clique para FECHAR o modal (no 'X')
    btnFecharModal.addEventListener("click", function() {
        modalOverlay.classList.remove("visivel");
    });

    // OUVIR clique para FECHAR o modal (clicando no fundo)
    modalOverlay.addEventListener("click", function(event) {
        if (event.target === modalOverlay) {
            modalOverlay.classList.remove("visivel");
        }
    });

    // OUVIR clique para Finalizar o Pedido (WhatsApp)
    btnFinalizar.addEventListener("click", function() {
        
        const itens = Object.keys(carrinho);
        if (itens.length === 0) {
            alert("Seu carrinho está vazio!");
            return;
        }

        const rua = document.getElementById("endereco-rua").value;
        const numero = document.getElementById("endereco-numero").value;
        const bairro = document.getElementById("endereco-bairro").value;
        const referencia = document.getElementById("endereco-referencia").value;

        if (!rua || !numero || !bairro) {
            alert("Por favor, preencha seu endereço completo (Rua, Número e Bairro).");
            return; 
        }

        let mensagem = "*--- NOVO PEDIDO - DEPÓSITO DO MATUTO ---*\n\n";
        let totalGeral = 0;

        itens.forEach(nome => {
            const item = carrinho[nome];
            const subtotal = item.preco * item.quantidade;
            totalGeral += subtotal;
            mensagem += `*${item.quantidade}x* ${nome} - R$ ${subtotal.toFixed(2)}\n`;
        });

        mensagem += "\n*-------------------------*\n";
        mensagem += `*Total: R$ ${totalGeral.toFixed(2)}*\n\n`;

        const formaPagamento = document.querySelector('input[name="pagamento"]:checked').value;
        mensagem += `*Forma de Pagamento:* ${formaPagamento}\n\n`;

        mensagem += "*--- ENDEREÇO DE ENTREGA ---*\n";
        mensagem += `${rua}, Nº ${numero}\n`;
        mensagem += `Bairro: ${bairro}\n`;
        
        if (referencia) {
            mensagem += `Referência: ${referencia}\n`;
        }
        
        // !!! TROQUE PELO SEU NÚMERO DE WHATSAPP !!!
        const seuNumero = "5581912345678"; // Formato 55 + DDD + Numero

        const mensagemCodificada = encodeURIComponent(mensagem);
        const linkWhatsApp = `https://api.whatsapp.com/send?phone=${seuNumero}&text=${mensagemCodificada}`;
        
        window.open(linkWhatsApp, '_blank');
    });


    // --- 4. FUNÇÃO AUXILIAR (Atualizar o visual do carrinho) ---
    function atualizarCarrinhoVisual() {
        carrinhoItensDiv.innerHTML = "";
        let totalGeral = 0;
        let totalItens = 0;

        const itens = Object.keys(carrinho);

        if (itens.length === 0) {
            carrinhoItensDiv.innerHTML = "<p>Seu carrinho está vazio.</p>";
            carrinhoTotalSpan.textContent = "0.00";
            totalItensSpan.textContent = "0";
            return;
        }

        itens.forEach(nome => {
            const item = carrinho[nome];
            const subtotal = item.preco * item.quantidade;
            totalGeral += subtotal;
            totalItens += item.quantidade;

            // =============================================
            // 👇 ADIÇÃO DO BOTÃO REMOVER AQUI 👇
            // =============================================
            const itemHtml = `
                <div class="item-carrinho">
                    <span class="item-carrinho-nome">${item.quantidade}x ${nome}</span>
                    <span class="item-carrinho-preco">R$ ${subtotal.toFixed(2)}</span>
                    <button class="btn-remover" data-nome="${nome}">&times;</button>
                </div>
            `;
            carrinhoItensDiv.innerHTML += itemHtml;
        });

        carrinhoTotalSpan.textContent = totalGeral.toFixed(2);
        totalItensSpan.textContent = totalItens;
        
        // ATIVA OS NOVOS BOTÕES 'REMOVER' QUE ACABAMOS DE CRIAR
        ativarBotoesRemover();
    }
    
    // =============================================
    // 👇 NOVA FUNÇÃO PARA REMOVER ITENS 👇
    // =============================================
    function ativarBotoesRemover() {
        const botoesRemover = document.querySelectorAll('.btn-remover');
        botoesRemover.forEach(botao => {
            botao.addEventListener('click', function() {
                // Pega o nome do item direto do atributo 'data-nome'
                const nomeDoItem = botao.dataset.nome;
                
                // Remove o item do "cérebro" (carrinho)
                if (carrinho[nomeDoItem]) {
                    delete carrinho[nomeDoItem];
                }
                
                // Atualiza o visual
                atualizarCarrinhoVisual();
            });
        });
    }

});