"""
Variáveis:
É um espaço na memória reservado para armazenar dados.

Regras para Criar Variáveis
   
1) o nome da variável  não deve conter espaços
nome completo
2) o nome da variável não deve começar com um número
20total
3) só é aceito o símbolo _ (underline ou underscore); 
outros símbolos e caracteres especiais não são aceitos
4) não usar as palavras-chave (palavras reservadas) do Python

"""

# 1) Crie um código Python que leia Nome,Sobrenome,Profissão e Cidade e mostre as informações.

nome="Maria"
sobrenome="Silva"
profissao="Engenheiro"
cidade="São Paulo"

print("Meu nome é ", nome)
print("Sobrenome:", sobrenome)
print("Profissão:", profissao)
print("Cidade Atual:", cidade)


# Variáveis com texto formatado Usando f-string (Python 3.6+)
nome="Maria"
sobrenome="Silva"
profissao="Engenheira"
cidade="São Paulo"

print(f"Meu nome é {nome} {sobrenome}, sou {profissao}, moro na {cidade}.")


#Formatação Numérica usando casa decimal

nota = 8.567
print(f"Nota: {nota:.1f}")

#-----------------------------------------
preco = 3500.5

print(f"Preço: R$ {preco:.2f}")


#-----------------------------------------
#Porcentagem

taxa = 0.15
print(f"Taxa: {taxa:.0%}")


#-----------------------------------------
#Exemplo prático (financeiro)

produto = "Teclado"
preco = 150.5
quantidade = 3
total = preco * quantidade

print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total da compra: R$ {total:.2f}")

