import matplotlib.pyplot as plt

# Dados
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [1000, 1500, 1200, 1800, 2000]

# Criar gráfico
plt.plot(meses, vendas)

# Adicionar pontos aos dados
plt.scatter(meses, vendas, color='red') 

# Título e rótulos
plt.title("Vendas por Mês")
plt.xlabel("Meses")
plt.ylabel("Valor de Vendas")

# Mostrar gráfico
plt.show()