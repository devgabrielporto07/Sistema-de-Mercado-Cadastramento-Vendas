# Bibliotecas:

from time import sleep # O intuito de usar é para ter uma impressão de tela de carregamento de sistema mesmo

# Variáveis das Cores no terminal para ficar mais organizado e exibir de uma forma melhor para o usuário:

verde = "\033[1;32m"
vermelho = "\033[1;31m"
magenta = "\033[1;34m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
negrito = "\033[1m"
inverte = "\033[7m"
finalizacor = "\033[0m"

# Exibição na tela do usuário com a ideia de menu e processamento:

print (f"{amarelo}-=-{finalizacor}"*31)
print (f"                                    {negrito}MERCADINHO DO SEU ZÉ{finalizacor} ")
print (f"{amarelo}-=-{finalizacor}"*31)

print (f"{ciano}\nInicializando o sistema...{finalizacor}\n")
sleep (1)
print (f"{amarelo}Processando...{finalizacor}")
sleep (2)
nome1 = str(input("\nAntes de tudo, Digite seu nome: ")).replace (" ", "").upper()
print (f"{verde}Tudo pronto, vamos lá{finalizacor}\n")

print (f"   === Olá {negrito}{nome1}{finalizacor}!, seja bem vindo ao sistema de Cadastramento e de Compras de Produtos ===\n")
print ("                               (1) Cadastrar Produtos")
print ("                               (2) Comprar Produtos")

# Condicionais + Estruturas de Repetição:

escolha_usuario = int(input("\nEscolha uma opção: ")) # Entrada para o usuário escolher a opção de acordo com o menu

if escolha_usuario == 1: # Para a opção 1 geramos essa condicional com uma lista vazia para fazer o cadastramento dos produtos
    print("     ========= Cadastramento de Produto =========")

    lista = []

    n = int(input("\nDigite a quantidade de produtos que você deseja cadastrar: ")) # A quantidade de produto que o usuário queira cadastrar seguindo pelo o seu nome e valor

    if n == 0: # Se caso o usuário digite 0 exibe uma mensagem na tela informando que nenhum produto foi cadastrado
        print (f"{vermelho}Nenhum produto cadastrado. Por vavor renicie o sistema e tente novamente{finalizacor}")
    else: #Se não procede pela a estrutura de repetição usando a lista gerada anteriormente
        for i in range(n):
            prod = input(f'Digite o nome do {i+1}º Produto: ').replace (" ", "")
            valor = float(input(f'Digite o valor do {i+1}º Produto (R$): '))

            lista.append([prod, valor])
        print (f"\n{magenta}Lista de produtos atualizada!\n{finalizacor}")
        for item in lista:
            print(f"Produto: {item[0]} | Valor: R$ {item[1]:.2f}")
        print (f"\n{magenta}Obrigado, Volte sempre! :){finalizacor}\n")

elif escolha_usuario == 2: # Para a opção 2 geramos essa condicional com um dicionário e e uma lista
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
    
    lista3 = [] # Oque o usuário digitar do dicionário será adicionado a um carrinho de compras
    
    total = 0 # Aqui é inicialmente o valor ser 0 até porque não foi adicionado nada na lista

    print(f"\n{verde}Produtos disponíveis no estoque:{finalizacor}\n")

    for nome, preco in produtos.items(): # Aqui é a exibição do dicionário para o usuário escolher os produtos seguido pela a variável dentro da estrutura de repetição
        print(f"{nome} - R$ {preco:.2f}") # O que for nome está no dicionário como string seguido pelas as aspas e oque for preço está seguindo pelo o valor e formatado para duas casas decimais

    while True:
        prod2 = input("\nDigite o nome do produto que você quer adicionar ao seu carrinho de compras ou se quiser ir para o Pagamento digite (PAGAMENTO): ").upper().strip().replace (" ", "") # entrada seguindo pelo o strip e o replace para retirar os espaços e o upper para colocar em maiúsculas evitando o erro do usuário e seguindo o programa
        if prod2 == "PAGAMENTO": 
            print (f"\n{negrito}Processando tela de pagamento...{finalizacor}")
            sleep (1.5) 
            break
        if prod2 in produtos:
            lista3.append(prod2)
            total += produtos[prod2]

            print(f"{verde}Seu carrinho de compras: {lista3}{finalizacor}")
            print(f"{verde}Valor atual: R$ {total:.2f}{finalizacor}")
        else:
            print(f"{vermelho}O Produto {negrito}{prod2}{finalizacor} {vermelho}não foi encontrado. Por vavor, verifique a ortografia ou escolha um item da lista acima{finalizacor}")

    if total == 0: # Caso o usuário digite pagamento sendo que não tenha nada na sua lista de compras é informado que o carrinho está vazio
        print(f"\n{vermelho}Carrinho vazio! Nenhum produto foi adicionado. Por favor renicie o sistema e tente novamente{finalizacor}")
    else: # Se não processa a tela de pagamento e vai para o pagamento
        print(f"{negrito}\n=========Tela de Pagamento========={finalizacor}")
        print(f"{negrito}O valor para o pagamento é de {magenta}R$ {total:.2f}{finalizacor}") # Informando qual é o valor para o usuário

        valor_pagamento = float(input("\nDigite o valor do pagamento (R$): ")) # Entrada para o usuário digitar o valor do pagamento em reais
        troco = valor_pagamento - total # Variável de troco
        if valor_pagamento > total: # Caso o usuário digite um valor acima do total terá seu troco
            print(f"{negrito}\nO seu troco é {magenta}R$ {troco:.2f}{finalizacor}")
            print(f"\n{verde}Produto comprado com sucesso! Volte Sempre :){finalizacor}")
        elif valor_pagamento == total: # Caso o usuário digite um valor igual ao total não terá troco 
            print(f"\n{verde}Produto comprado com sucesso! Volte Sempre :){finalizacor}")
        else: # Se não um valor abaixo uma mensagem informando que o valor foi insuficiente
            print(f"{vermelho}Valor Insuficiente. Por favor Digite um valor válido e renicie o sistema novamente. Aqui num é lugar de liso não kkkk{finalizacor}")

else: # Esse else recai na parte do menu seguindo a indentação caso o usuário digite uma opção que não faz parte do menu terá uma mensagem informando que a opção é inválida
    print (f"{vermelho}Opção Inválida. Renicie o sistema e tente novamente{finalizacor}")