
'''Conversão de Tipo de dados com o Comando Input'''


# Str -  Armazena Caracter do Tipo Texto

# Int - Armazena Valor Numérico Inteiro

# Float - Variável que Armazena o Tipo Ponto Flutuante(.)

nome=str(input("Digite seu Nome:"))
sobrenome=str(input("Digite seu SobreNome:"))
idade=int(input("Digite sua Idade:")) #convertendo para numero inteiro
salario=float(input("Digite seu salario Atual:"))#Convertendo para Valor com casas 

print(f"\n-----Informações Fornecidas-----")
print(f"Nome: {nome}")
print(f"SobreNome: {sobrenome}")
print(f"Idade:{idade}")
print(f"Salario {salario:.2f}")








