
# Jogo de adivinhação simples   

# O programa gera um número aleatório entre 1 e 5, e o usuário tem que adivinhar qual é.
# O programa informa se o palpite do usuário está correto ou não.
# Para jogar, basta executar o programa e digitar um número de 1 a 5 quando solicitado.




import random

numero_secreto = random.randint(1, 5)

palpite = int(input("Digite um número de 1 a 5: "))

if palpite == numero_secreto:
    print("Acertou!")
else:
    print("Errou! O número era", numero_secreto)