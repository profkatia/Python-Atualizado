'''
Enunciado: 

Você irá desenvolver um programa em Python que simule um sistema simples de cadastro de usuário.

O programa deverá solicitar ao usuário as seguintes informações:
'''


""" Regras do Cadastro"""

# Ao receber os dados digitados pelo usuário, o programa deverá:

"""Nome Completo"""

# -Remover os espaços extras do início e do final.
# -Deixar a primeira letra de cada palavra em maiúscula.


"""E-mail"""

# Remover os espaços extras do início e do final.

# Converter todo o texto para letras minúsculas.

"""Mensagem"""

# Remover os espaços extras do início e do final.

# Colocar apenas a primeira letra em maiúscula.

nome = input("Digite seu nome: ").strip().title()
email = input("Digite seu email: ").strip().lower()
mensagem = input("Digite uma mensagem: ").strip().capitalize()

print("\n--- DADOS CADASTRADOS ---")
print("Nome:", nome)
print("Email:", email)
print("Mensagem:", mensagem)