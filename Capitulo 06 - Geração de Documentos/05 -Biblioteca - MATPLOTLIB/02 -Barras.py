import matplotlib.pyplot as plt

produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
vendas = [50, 150, 80, 40]

plt.bar(produtos, vendas)#
#mudar a cor das barras

plt.bar(produtos, vendas, color=['blue', 'orange', 'green', 'red'])


plt.title("Vendas por Produto")
plt.xlabel("Produtos")
plt.ylabel("Quantidade")

plt.show()