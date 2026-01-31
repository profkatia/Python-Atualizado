

""" Usando o Comando OR (ou)


O operador or em Python é um operador lógico usado para verificar se pelo menos uma das condições é verdadeira.

Ele retorna True se alguma das expressões for verdadeira.

Ele retorna False somente se todas as expressões forem falsas.

""" 

#Aqui, or é usado para verificar se pelo menos um campo não está vazio
#(ambos são strings, e strings vazias são consideradas False).

email = input("Digite o email ")
telefone=input("Digite seu telefone")

if email or telefone:
    print("cadastro aceito")
else:
    print("Preencha pelo menos uma das opções")