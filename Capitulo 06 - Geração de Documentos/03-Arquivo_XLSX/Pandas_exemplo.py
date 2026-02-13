import pandas as pd

caminho_arquivo = "Base_Dados Vendedor.xlsx"

df = pd.read_excel(r'03-Arquivo_XLSX\Base_Dados Vendedor.xlsx')

print(df.head()) #exibe as 5 primeiras linhas do DataFrame


#exibe informações sobre o DataFrame, 

print(df.info()) 

#exibe estatísticas descritivas do DataFrame, como média, desvio padrão, valores mínimos e máximos, etc.
total_vendido = df["Vlr Unit"].sum()
print(f"Total vendido:", total_vendido)

#exibe o valor máximo da coluna "Valor_Vendido"
maior_venda = df["Vlr Unit"].max()
print("Maior venda:", maior_venda)

#exibe o valor mínimo da coluna "Valor_Vendido"
menor_venda = df["Vlr Unit"].min()     
print("Menor venda:", menor_venda)

#exibe o valor mínimo da coluna "Valor_Vendido"
media_vendas = df["Vlr Unit"].mean()
print("Média de vendas:", media_vendas)

#exibe a soma total de vendas por estado
vendas_estado = df.groupby("UF")["Vlr Unit"].sum()
print(vendas_estado)

