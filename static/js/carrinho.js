// Espera o HTML carregar completamente
document.addEventListener("DOMContentLoaded", function() {

    // --- 1. O "CÉREBRO" (Onde guardamos os itens) ---
    let carrinho = {}; 

    // --- 2. "OS OLHOS" (Encontrar os elementos na página) ---
    const botoesAdicionar = document.querySelectorAll(".btn-adicionar");
    
    // Elementos do Modal (pop-up)
    const modalOverlay = document.getElementById("modal-carrinho-overlay");
    const btnFecharModal = document.getElementById("btn-fechar-modal");
    const btnRevisarPedido = document.getElementById("btn-revisar-pedido");
    const btnFinalizar = document.getElementById("btn-finalizar-pedido");

    // Elementos de texto do carrinho
    const carrinhoItensDiv = document.getElementById("itens-do-carrinho");
    const carrinhoTotalSpan = document.getElementById("total-preco");
    const totalItensSpan = document.getElementById("total-itens-carrinho");

    
    // --- 3. "OS OUVIDOS" (Ações do Usuário) ---

    // OUVIR cliques nos botões "Adicionar"
    // (Esta é a parte que provavelmente estava faltando!)
    botoesAdicionar.forEach(botao => {
        botao.addEventListener("click", function() {
            const nome = botao.dataset.nome;
            const preco = parseFloat(botao.dataset.preco);
            const quantidadeInput = botao.previousElementSibling;
            const quantidade = parseInt(quantidadeInput.value);

            if (carrinho[nome]) {
                carrinho[nome].quantidade += quantidade;
            } else {
                carrinho[nome] = {
                    preco: preco,
                    quantidade: quantidade
                };
            }
            quantidadeInput.value = 1; // Reseta o input
            atualizarCarrinhoVisual(); // Atualiza o carrinho
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
        // Só fecha se clicar no fundo (overlay) e NÃO no conteúdo (modal-content)
        if (event.target === modalOverlay) {
            modalOverlay.classList.remove("visivel");
        }
    });

    // OUVIR clique para Finalizar o Pedido (WhatsApp)
    btnFinalizar.addEventListener("click", function() {
        
        // 1. VERIFICAR SE O CARRINHO NÃO ESTÁ VAZIO
        const itens = Object.keys(carrinho);
        if (itens.length === 0) {
            alert("Seu carrinho está vazio!");
            return;
        }

        // 2. PEGAR OS DADOS DO ENDEREÇO
        const rua = document.getElementById("endereco-rua").value;
        const numero = document.getElementById("endereco-numero").value;
        const bairro = document.getElementById("endereco-bairro").value;
        const referencia = document.getElementById("endereco-referencia").value;

        // 3. VALIDAR O ENDEREÇO
        if (!rua || !numero || !bairro) {
            alert("Por favor, preencha seu endereço completo (Rua, Número e Bairro).");
            return; // Para a execução e não envia o pedido
        }

        // 4. FORMATAR A MENSAGEM
        let mensagem = "*--- NOVO PEDIDO - DEPÓSITO DO MATUTO ---*\n\n";
        let totalGeral = 0;

        // Formata a lista de itens
        itens.forEach(nome => {
            const item = carrinho[nome];
            const subtotal = item.preco * item.quantidade;
            totalGeral += subtotal;
            mensagem += `*${item.quantidade}x* ${nome} - R$ ${subtotal.toFixed(2)}\n`;
        });

        mensagem += "\n*-------------------------*\n";
        mensagem += `*Total: R$ ${totalGeral.toFixed(2)}*\n\n`;

        // Pega a forma de pagamento
        const formaPagamento = document.querySelector('input[name="pagamento"]:checked').value;
        mensagem += `*Forma de Pagamento:* ${formaPagamento}\n\n`;

        // 5. ADICIONAR O ENDEREÇO NA MENSAGEM
        mensagem += "*--- ENDEREÇO DE ENTREGA ---*\n";
        mensagem += `${rua}, Nº ${numero}\n`;
        mensagem += `Bairro: ${bairro}\n`;
        
        // Só adiciona a referência se o cliente digitou uma
        if (referencia) {
            mensagem += `Referência: ${referencia}\n`;
        }
        
        // 6. ENVIAR PARA O WHATSAPP
        
        // !!! TROQUE PELO SEU NÚMERO DE WHATSAPP !!!
        const seuNumero = "558191251583"; // Formato 55 + DDD + Numero

        // Codifica a mensagem completa para uma URL
        const mensagemCodificada = encodeURIComponent(mensagem);
        const linkWhatsApp = `https://api.whatsapp.com/send?phone=${seuNumero}&text=${mensagemCodificada}`;
        
        // Abre o link em uma nova aba
        window.open(linkWhatsApp, '_blank');
    });


    // --- 4. FUNÇÃO AUXILIAR (Atualizar o visual do carrinho) ---
    // (Esta é a outra parte que provavelmente estava faltando!)
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

        // Cria o HTML para cada item
        itens.forEach(nome => {
            const item = carrinho[nome];
            const subtotal = item.preco * item.quantidade;
            totalGeral += subtotal;
            totalItens += item.quantidade;

            const itemHtml = `
                <div class="item-carrinho">
                    <span class="item-carrinho-nome">${item.quantidade}x ${nome}</span>
                    <span class="item-carrinho-preco">R$ ${subtotal.toFixed(2)}</span>
                </div>
            `;
            carrinhoItensDiv.innerHTML += itemHtml;
        });

        // Atualiza o total (no pop-up)
        carrinhoTotalSpan.textContent = totalGeral.toFixed(2);
        // Atualiza o contador de itens (no botão principal)
        totalItensSpan.textContent = totalItens;
    }

});