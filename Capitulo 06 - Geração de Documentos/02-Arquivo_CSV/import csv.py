# #Importação da biblioteca
# import csv
# #Abertura do arquivo
# with open(r"C:\Users\pc\Desktop\Curso Python\Professor\Capitulo 06 - Geração de Documentos\01-Arquivo_TXT\Vendas.txt",'r') as arquivo:
#     leitor=csv.reader(arquivo)
#     for linha in leitor:
#         print(linha)
#------------------------------------------------------------------------------------

#Importação usando a Bibioteca Pandas
import pandas as pd
df=pd.read_csv(r"C:\Users\pc\Desktop\Curso Python\Professor\Capitulo 06 - Geração de Documentos\01-Arquivo_TXT\Vendas.txt",sep=",")
print(df.head)# mostrar as linhas ta tabela

