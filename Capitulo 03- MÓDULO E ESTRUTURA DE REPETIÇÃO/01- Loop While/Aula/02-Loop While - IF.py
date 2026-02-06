
# while + if
'''Cadastro de Produto com Validação e Classificação de Estoque

Lógica:

>>Cadastre produtos

>>Classifique o estoque

>>Permita repetir o cadastro 3 vezes



'''''
#inicia o contador
contador = 0 
#enquanto o contador for menor que 3 digite o produto
while contador < 3: 

    print("\n--- CADASTRO DE PRODUTO ---")
#Digite o nome do produto   
    nome = input("Digite o nome do produto: ")
#Digite a quantidade em estoque
    quantidade = int(input("Digite a quantidade em estoque: "))

    # Validação da quantidade (se a caso o aluno perguntar)
    # while quantidade < 0:
    #     print("Quantidade inválida!")
    #     quantidade = int(input("Digite a quantidade em estoque: "))

    # Classificação do estoque

    if quantidade == 0:
        print("Status: PRODUTO ESGOTADO")

    elif quantidade <= 5:
        print("Status: ESTOQUE BAIXO")

    else:
        print("Status: ESTOQUE NORMAL")

    contador += 1

print("\nSistema encerrado.")
print("Total de produtos cadastrados:", contador)







    




    








