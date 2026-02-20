'''
#Enunciado:
# Crie uma classe chamada "ContaBancaria" com os atributos "numero", "titular" e "saldo".
# Em seguida, crie duas subclasses chamadas "ContaCorrente" 
# e "ContaPoupanca" que herdam da classe "ContaBancaria". 
# A classe "ContaCorrente" deve ter um atributo adicional 
# chamado "limite", enquanto a classe "ContaPoupanca" 
# deve ter um atributo adicional chamado "rendimento". 
# Crie objetos de ambas as subclasses e imprima o número da conta de cada objeto.

'''


class ContaBancaria:
    def __init__(self,numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


class ContaCorrente(ContaBancaria):
    def __init__(self,numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite
conta1 = ContaCorrente("12345-6", "João", 1000.0, 500.0)
print(conta1.numero)


class ContaPoupanca(ContaBancaria):
    def __init__(self,numero, titular, saldo, rendimento):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento
conta2 = ContaPoupanca("98765-4", "Maria", 2000.0, 0.05)
print(conta2.numero)
