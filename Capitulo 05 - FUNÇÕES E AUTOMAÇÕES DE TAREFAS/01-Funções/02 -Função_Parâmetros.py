'''

Eles permitem que a função seja mais flexível e reutilizável,
pois você pode passar diferentes valores para a função cada vez que a chamar.   
Exemplo:
'''

def media(a, b):
    resultado = (a + b) / 2
    return resultado

media_valor1 = float(input("Digite o primeiro número: "))
media_valor2 = float(input("Digite o segundo número: "))

resultado = media(media_valor1, media_valor2)

print(f"A média é: {resultado}")



#exemplo 2: cálculo de IMC (Índice de Massa Corporal)

def imc(peso, altura):
    return peso / (altura ** 2)


peso_usuario = float(input("Digite seu peso em kg: "))  
altura_usuario = float(input("Digite sua altura em metros: "))

resultado = imc(peso_usuario, altura_usuario)

print(f"Seu IMC é: {resultado:.2f}" )    



