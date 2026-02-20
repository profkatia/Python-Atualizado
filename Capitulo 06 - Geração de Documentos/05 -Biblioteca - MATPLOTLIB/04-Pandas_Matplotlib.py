import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("vendas_projeto.xlsx")

vendas_vendedor = df.groupby("Vendedor")["Valor"].sum()

print(vendas_vendedor)


 
#Gerar um grafico de barras para mostrar o total de vendas por vendedor
vendas_vendedor.plot(kind="bar")

plt.title("Total de Vendas por Vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Valor Total")
plt.show()



#Gerar um grafico de pizza para mostrar a distribuição de vendas por categoria
vendas_categoria = df.groupby("Categoria")["Valor"].sum()


#Gerar o grafico de pizza
vendas_categoria.plot(kind="pie", autopct="%1.1f%%")

plt.title("Distribuição de Vendas por Categoria")
plt.ylabel("")
plt.show()

#-------------------------------------------------------------------------------------


#Criar dashboard final com 2 gráficos combinado

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

vendas_vendedor.plot(kind="bar", ax=ax1)
ax1.set_title("Total de Vendas por Vendedor")
ax1.set_xlabel("Vendedor")
ax1.set_ylabel("Valor Total")

vendas_categoria.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_title("Distribuição de Vendas por Categoria")
ax2.set_ylabel("")

plt.tight_layout()
plt.show()