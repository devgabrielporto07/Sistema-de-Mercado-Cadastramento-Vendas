from time import sleep

# Variáveis das Cores no terminal:
verde = "\033[1;32m"
vermelho = "\033[1;31m"
magenta = "\033[1;34m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
fim = "\033[0m"

# Estoque
estoque = {
    "ARROZ":            {"unidade": "5kg",             "preco_min": 15.00, "preco_max": 25.00},
    "FEIJÃO CARIOCA":   {"unidade": "1kg",             "preco_min":  6.00, "preco_max": 10.00},
    "AÇÚCAR":           {"unidade": "1kg",             "preco_min":  4.00, "preco_max":  6.00},
    "CAFÉ":             {"unidade": "500g",            "preco_min": 26.00, "preco_max": 36.00},
    "LEITE":            {"unidade": "1L",              "preco_min":  4.00, "preco_max":  6.00},
    "ÓLEO DE SOJA":     {"unidade": "900ml",           "preco_min":  6.00, "preco_max":  9.00},
    "MACARRÃO":         {"unidade": "500g",            "preco_min":  4.00, "preco_max":  7.00},
    "OVOS":             {"unidade": "cartela c/12",    "preco_min": 10.00, "preco_max": 16.00},
    "FRANGO":           {"unidade": "1kg",             "preco_min":  9.00, "preco_max": 20.00},
    "PÃO FRANCÊS":      {"unidade": "1kg",             "preco_min": 12.00, "preco_max": 18.00},
    "MARGARINA":        {"unidade": "500g",            "preco_min":  7.00, "preco_max": 12.00},
    "FARINHA DE TRIGO": {"unidade": "1kg",             "preco_min":  5.00, "preco_max":  8.00},
    "TOMATE":           {"unidade": "1kg",             "preco_min":  6.00, "preco_max": 12.00},
    "BATATA":           {"unidade": "1kg",             "preco_min":  5.00, "preco_max":  9.00},
    "CEBOLA":           {"unidade": "1kg",             "preco_min":  4.00, "preco_max":  8.00},
    "SABÃO EM PÓ":      {"unidade": "1kg",             "preco_min": 12.00, "preco_max": 25.00},
    "PAPEL HIGIÊNICO":  {"unidade": "pacote 12 rolos", "preco_min": 15.00, "preco_max": 30.00},
    "DETERGENTE":       {"unidade": "500ml",           "preco_min":  2.00, "preco_max":  4.00},
    "ÁGUA SANITÁRIA":   {"unidade": "1L",              "preco_min":  3.00, "preco_max":  6.00},
    "SABONETE":         {"unidade": "unidade",         "preco_min":  2.00, "preco_max":  5.00},
}

# Estrutura do Código + Condicionais
print ("-=-"*8)
print ("  MERCADINHO DO SEU ZÉ ")
print ("-=-"*8)

print ("Inicializando o sistema...\n")
sleep (1.5)

print ("=== Olá, seja bem vindo ao sistema de estoque e vendas ===")
print ("(1) Cadastrar Produtos")
print ("(2) Vender Produtos")

escolha_usuario = int(input("\nEscolha uma opção: "))

if escolha_usuario == 1:
    print ("========== Cadastramento de Produto ===========")
    nome_produto       = str(input("Nome do produto: ")).upper().strip()
    preco_produto      = float(input("Preço do produto em (R$): "))
    quantidade_produto = int(input("Quantidade desejada: "))

    print (f"{verde}Produto cadastrado com sucesso!!{fim}")
    print (f"Nome: {nome_produto}")
    print (f"Preço: R$ {preco_produto:.2f}")
    print (f"Quantidade: {quantidade_produto}")

elif escolha_usuario == 2:
    print ("========== Venda de Produtos ==========")

    produtos_lista = list(estoque.items())
    for i, (nome, dados) in enumerate(produtos_lista, start=1):
        faixa = f"R$ {dados['preco_min']:.2f} a R$ {dados['preco_max']:.2f}"
        print (f"({i}) {nome} - {dados['unidade']} - {faixa}")

    numero        = int(input("\nDigite o número do produto: "))
    nome_escolhido, dados_escolhidos = produtos_lista[numero - 1]
    preco_venda   = float(input(f"Preço de venda em (R$): "))
    qtd_venda     = int(input("Quantidade vendida: "))
    total         = preco_venda * qtd_venda

    print (f"{verde}Venda registrada com sucesso!!{fim}")
    print (f"Produto: {nome_escolhido} ({dados_escolhidos['unidade']})")
    print (f"Quantidade: {qtd_venda}")
    print (f"Total: R$ {total:.2f}")

else:
    print (f"{vermelho}Opção Inválida{fim}")