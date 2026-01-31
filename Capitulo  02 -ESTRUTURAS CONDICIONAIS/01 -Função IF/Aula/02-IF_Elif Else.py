

"""
IF,   = (significa SE)
ELIF, = (significa SENÃO SE)
ELSE  = (significa SENAO)

Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Resumo: tomar decisões lógicas com base em diferentes cenários

    Tabela - Operadores Relacionais

            ==	Igual a
            !=	Diferente
            >=	Maior ou igual
            >	Maior que
            <	Menor que
            <=	Maior ou igual
"""
#Digite o Código aqui

#Exemplo 1:Classificação de notas escolares
""""
Digite a nota
      |
nota >= 7 ?
   Sim → Aprovado
   Não
      |
nota >= 5 ?
   Sim → Recuperação
   Não
      |
   Reprovado
   """

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


#Exemplo 2: Sistema de Cálculo de Bônus por Vendas

"""
Uma empresa deseja automatizar o cálculo de bônus mensal de seus vendedores com base 
no valor total de vendas realizadas no mês.O sistema deve solicitar ao usuário o 
valor total vendido e aplicar as seguintes regras:
"""

# Se o valor de vendas for maior ou igual a R$ 70.000, o vendedor receberá 25% de bônus.

# Se o valor de vendas for maior ou igual a R$ 50.000, o vendedor receberá 20% de bônus.

# Se o valor de vendas for maior ou igual a R$ 30.000, o vendedor receberá 10% de bônus.

# Se o valor de vendas for menor que R$ 30.000, o vendedor não receberá bônus.  

vendas = float(input("Digite o valor total de vendas do mês: R$ "))

if vendas >= 70000:
    bonus = vendas * 0.25
  

elif vendas >= 50000:
    bonus = vendas * 0.20
    

elif vendas >= 30000:
    bonus = vendas * 0.10

else:
    bonus = 0

print(f"Total vendido: R$ {vendas:.2f}")
print(f"Valor do bônus: R$ {bonus:.2f}")


    

