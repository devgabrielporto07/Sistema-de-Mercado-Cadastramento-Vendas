# Bibliotecas:
from time import sleep

# Variáveis das Cores no terminal:

verde = "\033[1;32m"
vermelho = "\033[1;31m"
magenta = "\033[1;34m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
branco = "\033[1;37m"
negrito = "\033[1m"
finalizacor = "\033[0m"

# Exibição na tela do usuário

print (f"{amarelo}-=-{finalizacor}"*8)
print ("  MERCADINHO DO SEU ZÉ ")
print (f"{amarelo}-=-{finalizacor}"*8)

print (f"{ciano}Inicializando o sistema...{finalizacor}\n")
sleep (1)
print (f"{amarelo}Processando...{finalizacor}")
sleep (2)
nome1 = str(input("\nAntes de tudo, Digite seu nome: ")).replace (" ", "").upper()
print (f"{verde}Tudo pronto, vamos lá{finalizacor}\n")

print (f"   === Olá {negrito}{nome1}{finalizacor}!, seja bem vindo ao sistema de Cadastramento e de Compras de Produtos ===\n")
print ("                               (1) Cadastrar Produtos")
print ("                               (2) Comprar Produtos")

# Condicionais 

escolha_usuario = int(input("\nEscolha uma opção: "))

if escolha_usuario == 1:
    print("     ========= Cadastramento de Produto =========")

    lista = []

    n = int(input("\nDigite a quantidade de produtos que você deseja cadastrar: "))
    if n == 0:
        print (f"{vermelho}Nenhum produto cadastrado. Por vavor renicie o sistema e tente novamente{finalizacor}")
    else:
        for i in range(n):
            prod = input(f'Digite o nome do {i+1}º Produto: ').replace (" ", "")
            valor = float(input(f'Digite o valor do {i+1}º Produto (R$): '))

            lista.append([prod, valor])
        print (f"\n{magenta}Lista atualizada{finalizacor}")
        for item in lista:
            print(f"Produto: {item[0]} | Valor: R$ {item[1]:.2f}")
        print ("Obrigado, Volte sempre! :)\n")

elif escolha_usuario == 2:
    print ("     ========== Compras de Produto ==========")

    produtos  = {
    "ARROZ": 22.75,
    "FEIJÃO": 7.25,
    "ÓLEO": 7.50,
    "AÇÚCAR": 5.00,
    "CAFÉ": 21.50,
    "LEITE": 6.25,
    "CARNE": 42.50,
    "MACARRÃO": 4.25,
    "FARINHA": 5.75,
    "PÃO": 18.50,
    "MANTEIGA": 12.50,
    "TOMATE": 8.00,
    "BATATA": 8.00
    } 
    
    lista3 = []
    
    total = 0 

    print(f"\n{verde}Produtos disponíveis no estoque:{finalizacor}\n")

    for nome, preco in produtos.items():
        print(f"{nome} - R$ {preco:.2f}")

    while True:
        prod2 = input("\nDigite o nome do produto que você quer adicionar a sua lista de compras ou se quiser ir para o Pagamento digite (PAGAMENTO): ").upper().strip().replace (" ", "") 
        if prod2 == "PAGAMENTO":
            print (f"\n{negrito}Processando tela de pagamento...{finalizacor}")
            sleep (1.5) 
            break
        if prod2 in produtos:
            lista3.append(prod2)
            total += produtos[prod2]

            print(f"{verde}Sua lista de compras: {lista3}{finalizacor}")
            print(f"{verde}Valor atual: R$ {total:.2f}{finalizacor}")
        else:
            print(f"{vermelho}O Produto {branco}{prod2}{finalizacor} {vermelho}não foi encontrado. Por favor, verifique a ortografia ou escolha um item da lista acima{finalizacor}")

    if total == 0:
        print(f"\n{vermelho}Carrinho vazio! Nenhum produto foi adicionado. Por favor renicie o sistema e tente novamente{finalizacor}")
    else:
        print(f"{negrito}\n=========Tela de Pagamento========={finalizacor}")
        print(f"{negrito}O valor para o pagamento é de {magenta}R$ {total:.2f}{finalizacor}")

        valor_pagamento = float(input("\nDigite o valor do pagamento (R$): "))
        troco = valor_pagamento - total
        if valor_pagamento > total:
            print(f"{branco}\nO seu troco é {magenta}R$ {troco:.2f}{finalizacor}")
            print(f"\n{verde}Produto comprado com sucesso! Volte Sempre :){finalizacor}")
        elif valor_pagamento == total:
            print(f"\n{verde}Produto comprado com sucesso! Volte Sempre :){finalizacor}")
        else:
            print(f"{vermelho}Valor Insuficiente. Por favor Digite um valor válido e renicie o sistema novamente. Aqui num é lugar de liso não kkkk{finalizacor}")

else:
    print (f"{vermelho}Opção Inválida. Renicie o sistema e tente novamente{finalizacor}")