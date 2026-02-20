#Criar uma classe Professor 

'''
>>>Objetivo: mostrar como criar uma classe simples com atributos e métodos.

class Professor: → define a classe.

__init__ → método construtor que inicializa os atributos.

self → representa o próprio objeto.
'''

class Professor:
    def __init__(self,nome,cpf,rg,disciplina):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.disciplina = disciplina
usuario1 = Professor("João", "123.456.789-00", "MG-12.345.678", "Matemática")
print(usuario1.nome)




class Aluno:
    def __init__(self,nome,cpf,rg,matricula):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
usuario2 = Aluno("Maria", "987.654.321-00", "SP-87.654.321", "123456")
print(usuario2.nome)


#---------------------------------------------------------------





