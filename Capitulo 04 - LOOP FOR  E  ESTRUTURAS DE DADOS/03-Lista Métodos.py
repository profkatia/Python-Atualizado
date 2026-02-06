'''    
LISTAS: 
       Métodos e Usos:
        
        * APPENDD >>> Atribui a lista, um elemento por vez no final da lista. 
        * INSERT >>> Atribui vários elementos, integrando à lista original.
        * POP >>> Remove um valor da lista por índice.
        * REMOVE >>> Remove um valor da lista por valor.
        * SORT >>> Ordena os dados de uma lista.
     '''   

#APPEND
# Gerencimanto de estoque com listas
# escreva seu código abaixo
produtos = ['monitor', 
            'notebook',
            'teclado',
            'mouse']

print('Estoque inicial:')
print(produtos)

# adicionar novos podutos
produtos.append('impressora') # adiciona no final
print(produtos)

produtos.insert(2, 'headset') # adiciona na 2a posição
print(produtos)

# remover produtos
produtos.remove('mouse') # remove pelo nome
print(produtos)

# remover pelo índice(posição) 1
removido = produtos.pop(1)

print(f'Produto removido: {removido}\n')
print('Estoque após remoção: ')
print(produtos)

# alteração de produtos
produtos[0] = 'monitor led' # altera o primeiro item

# altera o último item
produtos[-1] = 'impressora a laser'

print('\nApós a alteração:')
print(produtos)

# ordenação dos produtos
produtos.sort() # ordenar em ordemm alfabética
print('Produtos em ordem alfabética')
print(produtos)

# ordenação reversa
produtos.sort(reverse=True) # ordenação Z-A
print('Produtos em ordem reversa: ')
print(produtos)


