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
    print("========= Cadastramento de Produto =========")

    lista = []

    n = int(input('Digite a quantidade de produtos que você deseja cadastrar: '))

    for i in range(n):
        prod = input(f'Digite o nome do {i+1}º Produto: ')
        valor = float(input(f'Digite o valor do {i+1}º Produto: '))

        lista.append([prod, valor])

    print("\nLista Atualizada:")
    for item in lista:
        print(f"Produto: {item[0]} | Valor: R$ {item[1]:.2f}")

# Consegui mexer na parte de vendas (vou explicar aqui embaixo oque eu fiz, algumas coisas pedi ajuda ao GPT)
elif escolha_usuario == 2:
    print ("========== Vendas de Produto ==========")

    produtos  = {
        'ARROZ': 12.00,
        'FEIJAO': 14.00,
        'PAO': 4.00
    } #Isso é um dicionario onde consigo guardar como uma lista so que atribuir valores também tlgd

    lista3 = [] #essa lista sera atribuida os valores que o usuario digitar nela mais pra frente no while
    total = 0 #essa variavel é feita para atribuir valores a ela a cada produto digitado pelo usuário

    print(f"{verde}Produtos disponíveis:{fim} ")

    for nome, preco in produtos.items():
        print(f"{nome} - R$ {preco:.2f}") #esse for ele basicamente consegue adicionar os produtos que tem no estoque juntamente com o preço de cada produto tlgd.

    while True:
        prod2 = input('Digite o nome do produto que você quer comprar (ou SAIR): ').upper().strip() #aqui é a entrada do usuario no qual vai se atribuir os valores no proximo if
        if prod2 == "SAIR":
            break #aqui se encerra o while pois se não ele fica infinito

        if prod2 in produtos:
            lista3.append(prod2) #atribuiçao dos valores digitados
            total += produtos[prod2]#soma dos valores de cada produto

            print(f'{verde}Sua lista de compras: {lista3}{fim}') #aqui nesse print usuario consegue ver a sua lista de compras
            print(f'{verde}Valor atual: R$ {total:.2f}{fim}') #aqui eke consegue ver o valor do seu carrinho
        else:
            print(f"{vermelho}Produto não encontrado.{fim}") #caso o usuario digite algo diferente do que esta no dicionario ele ira mostrar essa mensagem de erro

else:
    print (f"{vermelho}Opção Inválida{fim}")

