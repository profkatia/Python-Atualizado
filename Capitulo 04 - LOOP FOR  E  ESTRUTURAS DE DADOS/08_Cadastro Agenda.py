'''Adicionando um dicionario vazio para armazenas os contatos'''
agenda={}

#defindo quantos contatos serão adicionados

quantidade = int(input("Quantos contatos você quer adicionar na agenda:"))

#Loop para adicionar os contatos

for i in range(quantidade):
    nome=input(f"Digite o nome do contato {i+1}:")
    telefone=input(f"Digite o telefone de {nome}:")

    #adicionando ao dicionarios
    agenda[nome]=telefone

#exibindo os elementos cadastrados da agenda
print(f'\n----Agenda de Contatos-----')
for nome,telefone in agenda.items():
    print(f'Nome: {nome} :Telefone {telefone}')

