"""1.Uma escola precisa de um software que calcule a 
média de alunos. 
Para isso o software deve receber o nome e três 
notas dos alunos. Com estes dados o software deve imprimir:
| ---------------------------------- | 
| Média	    | Imprimir               | 
| ---------------------------------- | 
| ==10	    | Aprovado com Distinção |
| >=7	    | Aprovado!              |
| >=5   	| Em exame               |
| senão     | Reprovado              |
| ---------------------------------- | 
"""

# Solicita o nome do aluno com entrada de dados
nome=input("Digite o nome do aluno").strip().title()

# Solicita a entrada de dados de três notas
nota1=float(input("Digite a 1° nota"))
nota2=float(input("Digite a 2° nota"))
nota3=float(input("Digite a 3° nota"))

# Calcular a média
media=(nota1+nota2+nota3)/3

# condição
if media==10:
    print(f"Aprovado com distinção {media}")
elif media>=7:
    print(f"Aprovado {media}" )
elif media >=5:
    print(f" em exame {media}")
else:
    print("Reprovado")
 


