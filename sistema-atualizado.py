from time import sleep

# Cores
verde = "\033[1;32m"
vermelho = "\033[1;31m"
magenta = "\033[1;34m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
fim = "\033[0m"

# Estoque fixo
estoque = {
    "ARROZ":              {"unidade": "5kg",            "preco_min": 15.00, "preco_max": 25.00},
    "FEIJÃO CARIOCA":     {"unidade": "1kg",            "preco_min":  6.00, "preco_max": 10.00},
    "AÇÚCAR":             {"unidade": "1kg",            "preco_min":  4.00, "preco_max":  6.00},
    "CAFÉ":               {"unidade": "500g",           "preco_min": 26.00, "preco_max": 36.00},
    "LEITE":              {"unidade": "1L",             "preco_min":  4.00, "preco_max":  6.00},
    "ÓLEO DE SOJA":       {"unidade": "900ml",          "preco_min":  6.00, "preco_max":  9.00},
    "MACARRÃO":           {"unidade": "500g",           "preco_min":  4.00, "preco_max":  7.00},
    "OVOS":               {"unidade": "cartela c/12",   "preco_min": 10.00, "preco_max": 16.00},
    "FRANGO":             {"unidade": "1kg",            "preco_min":  9.00, "preco_max": 20.00},
    "PÃO FRANCÊS":        {"unidade": "1kg",            "preco_min": 12.00, "preco_max": 18.00},
    "MARGARINA":          {"unidade": "500g",           "preco_min":  7.00, "preco_max": 12.00},
    "FARINHA DE TRIGO":   {"unidade": "1kg",            "preco_min":  5.00, "preco_max":  8.00},
    "TOMATE":             {"unidade": "1kg",            "preco_min":  6.00, "preco_max": 12.00},
    "BATATA":             {"unidade": "1kg",            "preco_min":  5.00, "preco_max":  9.00},
    "CEBOLA":             {"unidade": "1kg",            "preco_min":  4.00, "preco_max":  8.00},
    "SABÃO EM PÓ":        {"unidade": "1kg",            "preco_min": 12.00, "preco_max": 25.00},
    "PAPEL HIGIÊNICO":    {"unidade": "pacote 12 rolos","preco_min": 15.00, "preco_max": 30.00},
    "DETERGENTE":         {"unidade": "500ml",          "preco_min":  2.00, "preco_max":  4.00},
    "ÁGUA SANITÁRIA":     {"unidade": "1L",             "preco_min":  3.00, "preco_max":  6.00},
    "SABONETE":           {"unidade": "unidade",        "preco_min":  2.00, "preco_max":  5.00},
}

# ── ABERTURA ────────────────────────────────────────────────────
print(f"{amarelo}-=-{fim}" * 8)
print(f"{amarelo}     🛒  MERCADINHO DO SEU ZÉ  🛒{fim}")
print(f"{amarelo}-=-{fim}" * 8)

print(f"\n{ciano}Ligando o sistema, um momento...{fim}")
sleep(1)
print(f"{ciano}Quase lá...{fim}")
sleep(1)
print(f"{verde}Tudo pronto! Vamos lá! ✅{fim}\n")
sleep(0.5)

nome_atendente = input("Antes de começar, qual é o seu nome? ").strip().capitalize()
print(f"\n{verde}Boa, {nome_atendente}! Bom trabalho hoje. 💪{fim}\n")
sleep(0.8)

print(f"{'─'*40}")
print(f"  O que você quer fazer agora, {nome_atendente}?")
print(f"{'─'*40}")
print(f"  {amarelo}(1){fim} 📦  Cadastrar um produto novo")
print(f"  {amarelo}(2){fim} 💰  Registrar uma venda")
print(f"{'─'*40}")

escolha_usuario = int(input("\n👉 Digite sua escolha: "))

# ── OPÇÃO 1: CADASTRO ───────────────────────────────────────────
if escolha_usuario == 1:
    print(f"\n{ciano}{'─'*40}")
    print(f"  📦 Cadastro de Produto Novo")
    print(f"{'─'*40}{fim}")
    print("Preencha as informações abaixo:\n")

    nome_produto = input("📝 Nome do produto: ").upper().strip()
    preco_produto = float(input("💲 Preço de venda (R$): "))
    quantidade_produto = int(input("📊 Quantidade em estoque: "))

    print(f"\n{verde}{'─'*40}{fim}")
    print(f"{verde}  ✅ Produto cadastrado com sucesso!{fim}")
    print(f"{verde}{'─'*40}{fim}")
    print(f"  📦 Produto:    {nome_produto}")
    print(f"  💲 Preço:      R$ {preco_produto:.2f}")
    print(f"  📊 Quantidade: {quantidade_produto} unidade(s)")
    print(f"{verde}{'─'*40}{fim}")
    print(f"\n{amarelo}Ótimo trabalho, {nome_atendente}! Produto no sistema. 👍{fim}")

# ── OPÇÃO 2: VENDA ──────────────────────────────────────────────
elif escolha_usuario == 2:
    print(f"\n{ciano}{'─'*40}")
    print(f"  💰 Registrar Venda")
    print(f"{'─'*40}{fim}")
    print(f"Aqui estão os produtos disponíveis, {nome_atendente}:\n")

    print(f"  {'N°':<4} {'PRODUTO':<22} {'EMBALAGEM':<16} {'FAIXA DE PREÇO'}")
    print(f"  {'─'*60}")

    produtos_lista = list(estoque.items())
    for i, (nome, dados) in enumerate(produtos_lista, start=1):
        faixa = f"R$ {dados['preco_min']:.2f} ~ R$ {dados['preco_max']:.2f}"
        print(f"  {amarelo}{i:<4}{fim} {nome:<22} {dados['unidade']:<16} {faixa}")

    print(f"  {'─'*60}")

    try:
        numero = int(input(f"\n👉 Número do produto vendido: "))

        if numero < 1 or numero > len(produtos_lista):
            print(f"\n{vermelho}Eita! Esse número não existe na lista. Tenta de novo.{fim}")
        else:
            nome_escolhido, dados_escolhidos = produtos_lista[numero - 1]
            print(f"\n{verde}Produto selecionado: {nome_escolhido} ({dados_escolhidos['unidade']}){fim}")

            preco_venda = float(input(f"💲 Preço cobrado por unidade (R$): "))
            quantidade_venda = int(input(f"📊 Quantas unidades foram vendidas? "))

            total = preco_venda * quantidade_venda

            print(f"\n{verde}{'─'*40}{fim}")
            print(f"{verde}  ✅ Venda registrada com sucesso!{fim}")
            print(f"{verde}{'─'*40}{fim}")
            print(f"  🛍️  Produto:    {nome_escolhido}")
            print(f"  📦 Embalagem:  {dados_escolhidos['unidade']}")
            print(f"  🔢 Quantidade: {quantidade_venda}")
            print(f"  💲 Preço unit: R$ {preco_venda:.2f}")
            print(f"  💵 Total:      R$ {total:.2f}")
            print(f"{verde}{'─'*40}{fim}")
            print(f"\n{amarelo}Boa venda, {nome_atendente}! O Seu Zé agradece. 🤝{fim}")

    except ValueError:
        print(f"\n{vermelho}Ops! Você digitou algo que não é número. Tenta de novo com calma.{fim}")

# ── OPÇÃO INVÁLIDA ──────────────────────────────────────────────
else:
    print(f"\n{vermelho}Hmm, essa opção não existe no sistema, {nome_atendente}. Era (1) ou (2). 😅{fim}")