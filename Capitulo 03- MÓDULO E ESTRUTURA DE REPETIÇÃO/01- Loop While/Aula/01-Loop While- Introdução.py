"""
While >>> Permite que você crie um programa que execulte  repetições(loops) 
diversas vezez dependendo de uma condição.

vezes será repetido.
* Necessário atentar para o critério de parada.(loop infinito)

Quando usar while?
-Quando não sabe quantas vezes vai repetir (ex: esperar entrada do usuário);

-Quando quer validar algo até estar certo;

-Para menus interativos, autenticação, jogos, etc.


Sintaxe básica:

while condição:
    # bloco de código que será repetido
"""

   
"""
#exemplo
  Exemplo 1: Contando de 1 até 3

Logica: 
Enquanto o contador for menor ou igual a 3, imprima o valor do contador e incremente ele em 1.
"""
contador =0 # armazena a quantidade de loops realizados
while contador <=3: #condição que resulta em verdadeiro ou falso
    print(f'Numero {contador}') # bloco de código que será repetido
    contador+=1 #atualiza o contador para evitar loop infinito

#Usar a Ferramenta de Debug do VSCode para acompanhar o fluxo do código.


    








