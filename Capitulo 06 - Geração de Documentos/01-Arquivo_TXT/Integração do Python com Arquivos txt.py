# Integração do Python com Arquivos txt

'''
1. Método open: -> Abre um arquivo txt

arquivo = open('NomeArquivo.txt', 'r')

Usamos 'r' para abrir o arquivo para ler (read) e 
'w' quando estamos abrindo o arquivo para escrever (write) ou 
'a' se formos adicionar (append) uma informação no arquivo

'''

#Com o arquivo aberto, agora podemos efetivamente ler o arquivo com os métodos:

#Abrir o arquivo
with  open(r"C:\Users\pc\Desktop\Curso Python\Professor\Capitulo 06 - Geração de Documentos\01-Arquivo_TXT\Vendas.txt",'r') as arquivo:
    
    texto_arquivo=arquivo.read() #arquivo poucas linhas
    print(texto_arquivo)
 #-------------------------------------------------
    lista_linhas = arquivo.readlines() #muitas linhas
    print(lista_linhas)

#Leitura das linhas do arquivo
   
#------------------------------------------------------------------

 #adicionar novas linhas no txt
linhas = [
    "2026-08-06,rodrigo,Produto z,30.00,4,Cliente yX,São Paulo,SP\n",
    "\n2025-08-07,Joana,Produto zv,40.00,4,Cliente ayX,Rio de Janeiro,RJ"
 ]

# Cria o arquivo e escreve os dados
with open(r"C:\Users\pc\Desktop\Curso Python\Professor\Capitulo 06 - Geração de Documentos\01-Arquivo_TXT\Vendas.txt",'a') as f:
    f.writelines(linhas)
print("arquivo vendas foi atualizado com sucesso")