"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> (inicio, fim, passo)
"""


'''
# Neste exemplo, a repetição deve ser feita 5 vezes, 
visto que o valor para posição fim é 5 e o passo é 1.
'''

for i in range(6):
    print(i)

"""
ENUNCIADO:
    ==========

    Peça o nome e preço de 3 produtos e mostre os dados no final.

    PARA CADA PRODUTO ATÉ O LIMITE

    Para numero_produto dentro limite(1,4):

        # Pede o nome do produto

        # Pede o preço e converte para float

        # Mostra o produto cadastrado com o preço formatado

"""
total = 0  # acumulador
for numero_produto in range(1,4):

    # pede o nome do produto
    nome = input(f'Digite o nome do produto: {numero_produto}:')

    # pede o preço e converte para float
    preco = float(input(f'Digite o preço do produto: {numero_produto}'))
    
    total += preco
    
    # mostra o produto cadastrado com o preço formatado
    print(f'Produto {numero_produto} : {nome} - Preço R$ {preco:.2f} \n')

print(f'Total da compra: R$ {total:.2f} \n' )
