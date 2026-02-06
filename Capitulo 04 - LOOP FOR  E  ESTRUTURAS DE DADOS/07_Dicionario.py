"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

pessoa ={ 
   "Nome":"João",
   "Idade":20,
   "cidade":"São Paulo"
}


#acessando valores pela chave
print(f"Seu nome é {pessoa["Nome"]}")
print(f"Sua idade é {pessoa["Idade"]}")
print(f"Cidade onde Mora {pessoa["cidade"]}")



#Adição de itens e Remoção de Elementos chave e valor
pessoa ={ 
   "Nome":"João",
   "Idade":20,
   "cidade":"São Paulo"
}


pessoa['Email']='João@gmail.com'
del pessoa["Idade"]
print(pessoa)



#Verificação de existencia da chave idade
if 'Idade' in pessoa: # se a idade contem dentro do dicionario pessoa
    print("Chave idade existe no dicionario")
else:
    print("A chave idade não existe no dicionario")



#Iteração sobre o Dicionario usando For

cliente={
    'Nome':'Ana da Silva',
    'Cargo':'Recursos Humanos',
    'Salario':1800
}


#iterando sobre as chaves
for item in cliente:
    print(item)



#Iterando sobre os valores da chave
for item in cliente.values():
    print(item)



#Iterando sobre (chave e Valor)
for chave,valor in cliente.items():
    print(chave,valor)