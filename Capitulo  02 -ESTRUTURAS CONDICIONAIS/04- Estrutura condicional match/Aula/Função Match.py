"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
''' 
Exemplo: Escolha de produto no carrinho
'''
print("-----Menu de Produtos---")
print("1- Notebook")
print("2- Smartphone")
print("3-Fone de Ouvido")
print("4- cancelar")

opcao= input("Escolha um produto (1 a 4)")
 #instrução do match
match opcao:
    case "1":
        print("Você adicionou um notebook ao carrinho")
    case "2":
        print("Você adicionou um Smartphone ao carrinho")
    case "3":
        print("Você adicionou um Fone de Ouvido  ao carrinho")
    case "4":
        print("Compra cancelada")
    case _: #caso contrário
        print("Opção invalida , digite de 1 ate 4")

