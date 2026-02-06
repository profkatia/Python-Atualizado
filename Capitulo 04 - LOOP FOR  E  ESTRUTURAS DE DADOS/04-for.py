"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
"""



nomes = ["Ana", "Carlos", "Julia", "Pedro"]

for nome in nomes:
    print(nome)

   
'''
Crie um sistema que solicite a entrada de dados de 4  notas para
calcular a média aritmética .
'''


notas=[]

for i in range(1,5):
   nota=float(input(f"Digite a nota {i}º "))
   notas.append(nota)
#Calular a média aritmética (Média)
media=sum(notas)/len(notas)
#exibir o resultado 
print(f"Média é {media:.2f}")

#instrução if 
if media >=7:
    print("🤩 Parabéns você foi Aprovado")
else:
    print("😒 Aluno Reprovado")


    
