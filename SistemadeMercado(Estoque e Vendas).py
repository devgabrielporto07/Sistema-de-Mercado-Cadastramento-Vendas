# Bibliotecas:
from time import sleep

# Variáveis das Cores no terminal:

verde = "\033[1;32m"
vermelho = "\033[1;31m"
magenta = "\033[1;34m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
fim = "\033[0m"

# Estrutura do Código + Condicionais

print (f"{amarelo}-=-{fim}"*8)
print ("  MERCADINHO DO SEU ZÉ ")
print (f"{amarelo}-=-{fim}"*8)

print (f"{ciano}Inicializando o sistema...{fim}\n")
sleep (1)
print (f"{amarelo}Processando...{fim}")
sleep (1)
nome1 = str(input("\nAntes de tudo, Digite seu nome: ")).strip()
print (f"{verde}Tudo pronto, vamos lá{fim}")

print (f"=== Olá {nome1}, seja bem vindo ao sistema de Cadastramento e de Vendas Produtos ===")
print ("(1) Cadastrar Produtos")
print ("(2) Vender Produtos")


escolha_usuario = int(input("\nEscolha uma opção: "))

if escolha_usuario == 1:
    print ("========== Cadastramento de Produto ===========")
    nome_produto = str(input("Nome do produto: ")).upper().strip()
    preco_produto1 = float(input("Preço do produto em (R$): "))
    quantidade_produto = int(input("Quantidade desejada: "))

    print (f"{verde}Produto cadastrado com sucesso!!{fim}")
    print (f"Nome: {nome_produto}")
    print (f"Preço: {preco_produto1:.2f}")
    print (f"Quantidade: {quantidade_produto}")
# DANIEL MEXE AQUI NESSE ELIF NA PARTE DE VENDAS AS LISTAS VÊ COMO FUNCIONA
elif escolha_usuario == 2:
    print ("========== Vendas de Produto ==========")
    list  = ["ARROZ (0)", "FEIJÃO (1)", "PÃO (2)"]
    print (list)
    print (list [0])
    produto_venda = str(input("Nome do produto: ")).upper().strip()
    preco_produto2 = float(input("Preço do Produto (R$): "))
else:
    print (f"{vermelho}Opção Inválida{fim}")

