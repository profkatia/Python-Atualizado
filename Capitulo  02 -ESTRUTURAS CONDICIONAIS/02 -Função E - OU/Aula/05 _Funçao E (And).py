"""Função And(E)"""

"""Situação
media >= 7 and media <= 10: só entra se a média for de 7 a 10

media >= 5 and media < 7: de 5 até antes de 7

media >= 0 and media < 5: de 0 até antes de 5

Senão: qualquer valor negativo ou acima de 10 é considerado inválido


"""
#Digite o Código

#Solicita a média do aluno


# Entrada de dados
nome = input("Digite o nome do aluno")
media =float(input("Digite a média do aluno(0 a 10):"))
print(f"\n aluno:{nome}")
print(f"Média:{media}")

# Aplica a lógica com AND
if media>=7 and media<=10:
    print("Situação: Aprovado")
elif  media>=5 and media <7:
    print(" Situação Exame")
elif media >=0 and media <5:
    print("Situação: Reprovado")
else:
    print("Situação invalida, fora do intervalo de 0 a 10")
    







