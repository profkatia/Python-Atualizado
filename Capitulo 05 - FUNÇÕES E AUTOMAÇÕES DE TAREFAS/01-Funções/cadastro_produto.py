

#-----------------------------------------------------------------
#Programa que cadastra Produto
  # Coleta os dados do usuário usando input()
def cadastrar_produto():
    nome_produto = input("Digite o nome do Produto")
    preco_produto=float(input("Digite o preço do produto R$  "))
    quantidade_produto=int(input("Digite a quantidade em estoque"))

    #Solicita ao usuário os dados de um produto e retorna um dicionário.
    produto={
        "Nome":nome_produto,
        "Preco":preco_produto,
        "Quantidade":quantidade_produto
        }

    # Retorna o dicionário para ser usado fora da função
    return produto

# --- ----------Exemplo de uso da função com um laço 'for' ------------------

# Pergunta ao usuário quantos produtos ele quer cadastrar
numero_produtos=int(input("Quantos produtos você deseja cadastrar"))

# Cria uma lista vazia para armazenar todos os produtos
estoque_de_produtos=[]

# Usa um laço 'for' para chamar a função repetidamente
# O 'range(numero_produtos)' fará o laço repetir o número de vezes 
# que o usuário escolheu
for i in range(numero_produtos):
    print(f'----cadastro do produto {i+1}-----')
    # Chama a função e armazena o dicionário retornado na lista
    novo_produto=cadastrar_produto()
    estoque_de_produtos.append(novo_produto)
 
# Exibe todos os produtos cadastrados após o laço
print(f"🚚-----Produtos cadastrados-------🚚")
for produto in estoque_de_produtos:
    print(f'Nome do Produto:{produto['Nome']} | Preço: {produto['Preco']:.2f} | Quantidade{produto['Quantidade']} ')