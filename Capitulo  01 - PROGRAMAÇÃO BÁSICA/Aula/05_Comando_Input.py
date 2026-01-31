"""
Input:
    Função responsável por entrada de dados no terminal do python
"""

"""
Exemplo: Entrada de dados com a função input()

Este programa solicita ao usuário seu Nome, Sobrenome , Idade e  Salário
e exibe essas informações formatadas.
"""

# Solicita os dados ao usuário
nome=input("Digite seu Nome:")
sobrenome=input("Digite seu SobreNome:")
idade=type(input("Digite sua Idade:"))
salario=type(input("Digite seu salario Atual:"))

print(f"\n-----Informações Fornecidas-----")
print(f"Nome: {nome}")
print(f"SobreNome: {sobrenome}")
print(f"Idade:{idade}")
print(f"Salario {salario}")

# Exibe os dados formatados usando o F string
