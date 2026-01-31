
"""
3. Desenvolva um programa em Python que calcule o salário líquido de um 
    profissional que trabalha por hora.

Para isso, o programa deve solicitar ao usuário as seguintes informações:

valor_hora → valor recebido por hora de trabalho;

horas_trabalhadas → quantidade de horas trabalhadas no mês;

percentual_inss → percentual de desconto do INSS (em %).

Após receber os dados, o programa deverá realizar os seguintes cálculos:

"""

#Faça seu Código aqui

#solicita as informações de entrada

valor_hora=float(input("Informe o valor por hora"))
horas_trabalhadas=float(input("Informe o numero de horas trabalhada"))
percentual_inss=float(input("Informe o percentual de desconto do inss"))

#Calcular o salário bruto (valor_hora × horas_trabalhadas)
salario_bruto = valor_hora*horas_trabalhadas

#Calcular o valor do desconto do INSS ( salario_bruto × percentual_inss / 100)
desconto= salario_bruto*(percentual_inss/100)

#Calculo do salario Liquido =salario_bruto−desconto_inss
liquido= salario_bruto-desconto

#exibir os resultados:
#Salário Bruto
#Valor do Desconto do INSS
#Salário Líquido
print(f"Salario Bruro: R$ {salario_bruto:.2f}")
print(f"Desconto do Inss:R$ {desconto:.2f}")
print(f"Salário Liquido :R$ {liquido:.2f}")