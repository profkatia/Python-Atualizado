#-----Entrada de dados----------
print(f"\n---------Entrada de dados do Usuário---------")

nome=input("Digite o nome do Funcionário").capitalize()
endereco=input("Digite o endereço onde Mora").capitalize()
empresa=input("Digite a Empresa que Trabalha").capitalize()
cargo=input("Digite o cargo atual").capitalize()
salario=float(input("Digite o salario bruto(R$):   "))


#Condições baseada na tabela
if salario <=1903.98:
    aliquota=0.0
    deducao=0.0

elif salario <= 2826.65:
    aliquota=0.075
    deducao= 142.80

elif salario <=3751.05:
    aliquota=0.15
    deducao=354.80 

elif salario <= 4664.68:
    aliquota=0.225
    deducao=636.13

else:
    aliquota=0.275
    deducao=869.36

#Calculo do imposto e salario liquido
imposto =(salario*aliquota)-deducao
liquido = salario-imposto

#Exibição dos dados do funcionário 
print(f"\n-----Resumo do funcionário")
print(f"Funcionario {nome}")
print(f"Endereço {endereco}")
print(f"Empresa {empresa}")
print(f"Cargo {cargo}")
print(f"Imposto de Renda {imposto:.2f} seu salário Liquido : {liquido:.2f}")
