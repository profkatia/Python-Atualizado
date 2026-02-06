
#Acessando Elemento
produtos_em_estoque = ["Smartphone X", "Notebook Pro", "Fone Bluetooth", "Smart TV 50"]

# Acessando o primeiro produto em estoque
 # "Smartphone X"
print(produtos_em_estoque[0])

# Acessando o terceiro produto
 #"Fone Bluetooth"
print(f'seu produto do estoque é {produtos_em_estoque[2]}')
# Acessando o último produto (ótimo para ver o último item adicionado)
 # Saída: "Smart TV 50"
print(f'Seu ultimo produto em estoque é {produtos_em_estoque[3]}')
print(f'Seu ultimo produto em estoque é {produtos_em_estoque[-1]}')
#-----------------------------------------------------------------------------------

#Fatiamento
#exibir os dois primeiros produtos 
print(produtos_em_estoque[:2])

#Exibir os dois últimos ("Fone Bluetooth", "Smart TV 50"
print(produtos_em_estoque[2:])

#Exibir os produtos do meio
print(produtos_em_estoque[1:3])


