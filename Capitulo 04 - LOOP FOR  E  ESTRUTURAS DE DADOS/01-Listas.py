'''
Listas:
Elas são coleções ordenadas e mutáveis, o que significa que você pode 
listar itens em uma sequência específica e alterar esses itens a qualquer momento
'''

# Lista de nomes de produtos
produtos_estoque = ["Smartphone","Notebook","Fone Bluetooth","Smart Art"]
print(produtos_estoque)

# Lista de preços de produtos

vendas=[1223.66,4848,150.00,2000.00]
print(vendas)

# Lista de status de vendas (cliente, valor, pago?)

status =["Joao silva",1500,True]
status2=["Maria da Silva",8900,False]
print(f"status de João {status} eStatus Maria {status2}")

# Lista de todas as vendas (lista de listas)

historico_vendas=[
["João da silva",1500,True],
["Maria Souza",850 ,False],
["Carlos Abreu",300.00,True]
]
print(historico_vendas)