""""

#CONCEITO SOBRE IMPORTAÇÃO DE BIBLIOTECAS NO PYTHON

O Python possui uma vasta biblioteca padrão, que inclui módulos 
para realizar diversas tarefas. Para utilizar essas funcionalidades, 
é necessário importar os módulos correspondentes.
A importação de bibliotecas é feita usando a palavra-chave "import" seguida do nome do módulo ou pacote que se deseja utilizar.


# Existem diferentes formas de importar bibliotecas, como:

1. Importação direta: import random
2. Importação com alias: import random as rnd

A escolha da forma de importação depende do contexto e das necessidades do programa.

"""

#Importando a biblioteca random
'''
RANDOM
======
Essa biblioteca é muito interessante quando precisamos 
trabalhar com dados aleatórios. Sendo uma ferramenta muito
interessante na área de estatística para simular valores aleatórios
'''

#Gerar número inteiro aleatório entre 1 e 100
import random 
numero_aleatorio = random.randint(1,100) # Gera um número aleatório entre 1 e 100
print("O número aleatório gerado é:", numero_aleatorio)



#importando a biblioteca random com alias
import random as rnd
numero_aleatorio = rnd.randint(1,100) # Gera um número aleatório entre 1 e 100
print("O número aleatório gerado é:", numero_aleatorio)


