# Programa para calcular descontos com base na categoria do produto

#CRIAR MENU opções usando estrutura de repetição while

# Categorias:
# 1 - Eletrônicos: 10% de desconto
# 2 - Roupas: 20% de desconto
# 3 - Alimentos: 5% de desconto
# 4 - Sair

# O programa deve continuar exibindo o menu até que o usuário escolha a opção de sair (4).  
# Para cada categoria selecionada, o programa deve solicitar o preço do produto, calcular o desconto e exibir o valor final a pagar.
# Se o usuário escolher a opção de sair, o programa deve encerrar.
# Exibir mensagens apropriadas para cada etapa do processo.
"""
# Exemplo de saída: 
===== MENU DE CATEGORIAS =====
1 - Eletrônicos (10% desconto) 
2 - Roupas (20% desconto)
3 - Alimentos (5% desconto)    
4 - Sair

Escolha a categoria: 2     
Digite o preço do produto: R$ 150.00
Valor do desconto: R$ 30.00    
Valor final a pagar: R$ 120.00 


"""
#DIGITE O CÓDIGO AQUI:
# Inicializa a variável de opção IGUAL A 0

opcao = 0 
# Estrutura de repetição para exibir o menu até o usuário escolher sair
while opcao != 4:
    
    print("\n===== MENU DE CATEGORIAS =====")
    print("1 - Eletrônicos (10% desconto)")
    print("2 - Roupas (20% desconto)")
    print("3 - Alimentos (5% desconto)")
    print("4 - Sair")

#Solicita a escolha do usuário
    opcao = int(input("Escolha a categoria: "))
# SE OPCAO FOR  MAIOR OU IGUAL A 1 E MENOR OU IGUAL A 3 
    if opcao >= 1 and opcao <= 3:
# Solicita o preço do produto PARA O USUÁRIO
        preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto com base na categoria escolhida
#SE OPCAO FOR IGUAL A 1 CALCULA 10% DE DESCONTO
#SE OPCAO FOR IGUAL A 2 CALCULA 20% DE DESCONTO
#SENÃO CALCULA 5% DE DESCONTO
#CALCULA VALOR FINAL SUBTRAINDO O DESCONTO DO PREÇO
#EXIBE VALOR DO DESCONTO E VALOR FINAL A PAGAR

        if opcao == 1:
            desconto = preco * 0.10
        elif opcao == 2:
            desconto = preco * 0.20
        else:
            desconto = preco * 0.05
        
        valor_final = preco - desconto
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}") 