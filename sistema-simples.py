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
    "ARROZ":            {"unidade": "5kg",             "preco": 15.00},
    "FEIJÃO CARIOCA":   {"unidade": "1kg",             "preco":  6.00},
    "AÇÚCAR":           {"unidade": "1kg",             "preco":  4.00},
    "CAFÉ":             {"unidade": "500g",            "preco": 26.00},
    "LEITE":            {"unidade": "1L",              "preco":  4.00},
    "ÓLEO DE SOJA":     {"unidade": "900ml",           "preco":  6.00},
    "MACARRÃO":         {"unidade": "500g",            "preco":  4.00},
    "OVOS":             {"unidade": "cartela c/12",    "preco": 10.00},
    "FRANGO":           {"unidade": "1kg",             "preco":  9.00},
    "PÃO FRANCÊS":      {"unidade": "1kg",             "preco": 12.00},
    "MARGARINA":        {"unidade": "500g",            "preco":  7.00},
    "FARINHA DE TRIGO": {"unidade": "1kg",             "preco":  5.00},
    "TOMATE":           {"unidade": "1kg",             "preco":  6.00},
    "BATATA":           {"unidade": "1kg",             "preco":  5.00},
    "CEBOLA":           {"unidade": "1kg",             "preco":  4.00},
    "SABÃO EM PÓ":      {"unidade": "1kg",             "preco": 12.00},
    "PAPEL HIGIÊNICO":  {"unidade": "pacote 12 rolos", "preco": 15.00},
    "DETERGENTE":       {"unidade": "500ml",           "preco":  2.00},
    "ÁGUA SANITÁRIA":   {"unidade": "1L",              "preco":  3.00},
    "SABONETE":         {"unidade": "unidade",         "preco":  2.00},
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
        print (f"({i}) {nome} - {dados['unidade']} - R$ {dados['preco']:.2f}")

    numero         = int(input("\nDigite o número do produto: "))
    nome_escolhido, dados_escolhidos = produtos_lista[numero - 1]
    qtd_venda      = int(input("Quantidade vendida: "))
    total          = dados_escolhidos['preco'] * qtd_venda

    print (f"{verde}Venda registrada com sucesso!!{fim}")
    print (f"Produto: {nome_escolhido} ({dados_escolhidos['unidade']})")
    print (f"Quantidade: {qtd_venda}")
    print (f"Preço unit: R$ {dados_escolhidos['preco']:.2f}")
    print (f"Total: R$ {total:.2f}")

else:
    print (f"{vermelho}Opção Inválida{fim}")