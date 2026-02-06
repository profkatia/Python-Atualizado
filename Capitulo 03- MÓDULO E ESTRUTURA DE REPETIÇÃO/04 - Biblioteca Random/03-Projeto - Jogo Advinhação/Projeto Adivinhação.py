#
# Projeto: Jogo de Adivinhação

'''
Importando a biblioteca random para gerar um número aleatório
passo 1: Gerar um número secreto entre 1 e 10
passo 2: Inicializar o número de tentativas e o limite de tentativas
passo 3: Criar um loop while  para permitir que o jogador faça palpites até atingir o limite de tentativas
passo 4: Solicitar ao jogador que digite um palpite
passo 5: Verificar se o palpite é igual ao número secreto
passo 6: Se o palpite for correto, exibir uma mensagem de parabéns e encerrar o jogo
passo 7: Se o palpite for menor que o número secreto, informar que o número é maior
passo 8: Se o palpite for maior que o número secreto, informar que o número é menor
passo 9: Se o jogador atingir o limite de tentativas sem acertar, exibir uma mensagem de derrota e revelar o número secreto

'''

import random

numero_secreto = random.randint(1, 10)

tentativas = 0
limite = 3

while tentativas < limite:
    palpite = int(input("Digite um número entre 1 e 10: "))
    
    tentativas += 1
    
    if palpite == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número é MAIOR.")
    else:
        print("O número é MENOR.")
        
if palpite != numero_secreto:
    print("😢 Você perdeu!")
    print("O número era:", numero_secreto)