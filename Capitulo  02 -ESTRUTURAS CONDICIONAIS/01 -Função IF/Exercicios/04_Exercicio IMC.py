"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:


| Menor que 18.5      | Abaixo do peso       |
| >=18.5  E <= 24.9   | Peso Normal          |
| >= 25.0 E <= 29.9   | Excesso de peso      |
| >=30.0  E  <=34.9   | Obesidade classe I   |
| >=35.0  E  <=39.9   | Obesidade classe II  |
|caso contrário sera  | Obesidade classe III |

"""

# Solicita os dados do usuário
nome=input("Digite o nome do usuario").strip().title()

peso=float(input("Digite seu peso"))
altura= float(input("Digite a altura"))

# Calcula o IMC
imc=peso/(altura ** 2)

# Imprime o resultado com duas casas decimais
print(f"Seu IMC é {imc:.2f}")

# Determina a classificação com IF
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso Normal")

elif 25.0 <= imc <=29.9:
    print("Excesso de peso")

elif 30.0 <= imc <=34.9:
    print("Obesidade classe I")

elif 35.0 <= imc <=39.9:
    print("Obesidade classe II")

else:
    print("Obesidade classe III")

