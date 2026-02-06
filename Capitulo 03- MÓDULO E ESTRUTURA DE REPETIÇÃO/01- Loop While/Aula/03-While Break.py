'''
    While com Break
    while True: >>> este laço será executado enquanto 
    não encontrar o Break pelo caminho.
    Break >>> Condição de parada/encerramento(stop) de um loop. 

'''


while True: # enquanto verdadeiro
    menu = int(input('''
            [1] CADASTRAR
            [2] SAIR
            Digite a opção: 
            '''))    
    match menu:
        case 1:
            nome = input('Digite o nome: ')
        case 2: 
            print('Obrigado e volte sempre!')
            break # interrompe a execução do While/Stop
            #exit()
        case _: # caso contrário
            print('Opção inválida!')

print('Sai do While')
print('Fim do programa')







