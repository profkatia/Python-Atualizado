''' 
O if é uma estrutura condicional. Ele verifica se 
uma condição é verdadeira (True) e, 
se for, executa o código que está 
indentado logo abaixo dele.

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
    
    Operadores Lógicos

            or	OU lógico
            and	E lógico
            not	Negação


O if é uma estrutura condicional. Ele verifica se
uma condição é verdadeira (True) e, se for , executa o código
que está indentado logo abaixo dele.

    RESUMO
    ======
    if:(significa SE) verifica se uma condição é verdadeira.

    elif: (significa SENÃO SE) verifica outra condição, se a anterior for falsa.

    else: (significa SENAO) executa um bloco de código se todas as condições anteriores forem falsas.

'''
'''
    ESCOLA XYZ
    ==========

    ENTRADA ( variáveis )
    =======
    nota 1
    nota 2
    nota 3
    nota 4

    CÁLCULO
    =======
    media = (soma das notas) / por 4

    ANÁLISE
    =======
    se a media for maior ou igual a 7, 'Aprovado'

    se a media for menor do que 7, 'Reprovado'

'''

# 1º passo - ENTRADAS (declaração das variáveis)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))


# 2º passo - CÁLCULO da média

media = (nota1 + nota2 + nota3 + nota4) / 4


# 3º passo - ANÁLISE com IF (decisão)

if media >= 7:
    print(f"Média: {media:.2f} - Aluno APROVADO ✅")
else:
    print(f"Média: {media:.2f} - Aluno REPROVADO ❌")




"""
Situação prática: Cálculo de comissão de vendedor

Enunciado:
Um vendedor recebe uma comissão com base nas vendas do mês.
Se ele vender R$ 5.000 ou mais, ganha 10% de comissão.
Caso contrário, ganha 5%.

Faça um programa que peça o nome do vendedor 
e o valor total de vendas, e mostre a comissão recebida.
"""
#Digite o Código aqui
 # entrada de dados
vendedor=input("Digite o nome do Vendedor")
venda=float(input("Digite o valor total da venda"))

if venda >=5000:
    comissao=venda*0.10
else:
    comissao=venda*0.05
    
#EXIBIR O RESULTADO
print(f"Vendedor:{vendedor}")
print(f"Total de vendas:{venda:.2f}")
print(f"Comissão Recebida:{comissao:.2f}")
