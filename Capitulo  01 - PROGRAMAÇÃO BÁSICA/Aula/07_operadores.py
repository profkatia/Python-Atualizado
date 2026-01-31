"""
Operadores Aritméticos e lógicos:

+  Adição           *  Multiplicação
-  Subtração        ** Exponenciação

/  Divisão
// Retorna o valor inteiro da divisão
%  Retorna o resto da divisão

>   Maior           ==  Igual
<   Menor           !=  Diferente

>=  Maior ou igual
<=  Menor ou igual
=   Atribuição
"""

# Variáveis e Operadores em Python
a = 2
b = 3

print(a + b)   # adição
print(a - b)   # subtrair

print(a * b)   # multiplicar
print(a ** b)  # exp

print(a / b)   # divisão
print(a // b)  # divisão com valor inteiro
print(a % b)   # resto da divisão

print(a > b)   # [a] é maior que [b]?
print(a <= b)  # [a] é menor ou igual [b]?
print(a == b)  # [a] é igual [b]?
print(a != b)  # [a] é diferente de [b]?

#---------------------------------------------------------------------------------------
#Exemplos

'''
1)Soma de dois valores

Enunciado:
Crie um programa que declare duas variáveis 
com valores numéricos e calcule a soma entre elas. 
Exiba o resultado para o usuário.
'''
# Valor1=10
# valor2=25
# total= Valor1+valor2
# print(f"A soma de {Valor1} + {valor2} é igual a {total}")


'''
2)Cálculo da média de duas notas

Enunciado:
Crie um programa que receba duas notas de um aluno, 
calcule a média e exiba o resultado.
'''
# nota1=8.5
# nota2=9.0

# media=(nota1+nota2)/2
# print(f"A média das notas é {media}")



'''
3)Aumento de 5% no salário

Enunciado:
Crie um programa que receba o salário de um funcionário e 
calcule o novo salário com um aumento de 5%. Exiba o valor final
'''
salario = 2000.00
novo_salario= salario*1.05
print(f" O novo salario é R${novo_salario:.2f}" )

