
#Polimorfismo gerar o mesmo exemplo 
class ContaBancaria:
    def __init__(self,numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def imprimir_numero(self):
        print(self.numero)



class ContaCorrente(ContaBancaria):
    def __init__(self,numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite
conta1 = ContaCorrente("12345-6", "João", 1000.0, 500.0)
conta1.imprimir_numero()
saldo1 = conta1.saldo
print(saldo1)



class ContaPoupanca(ContaBancaria):
    def __init__(self,numero, titular, saldo, rendimento):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento
conta2 = ContaPoupanca("98765-4", "Maria", 2000.0, 0.05)
conta2.imprimir_numero()  
saldo2 = conta2.saldo
print(saldo2)




#--------------------------------------------------------------------------------

class deposito(ContaBancaria):
    def __init__(self, numero, titular, saldo, valor_deposito):
        super().__init__(numero, titular, saldo)
        self.valor_deposito = valor_deposito


    def realizar_deposito(self):
        self.saldo += self.valor_deposito
        print(f"Depósito de R${self.valor_deposito} realizado. Novo saldo: R${self.saldo}") 
conta3 = deposito("54321-0", "João", 1000.0, 300.0)
conta3.realizar_deposito()



                                