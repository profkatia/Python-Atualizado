#Herança class pessoa
class Pessoa:
    def __init__(self,nome,cpf,rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg        

class Professor(Pessoa):
    def __init__(self,nome,cpf,rg,disciplina):
        super().__init__(nome,cpf,rg)
        self.disciplina = disciplina                                        
usuario1 = Professor("João", "123.456.789-00", "MG-12.345.678", "Matemática")
print(usuario1.nome)  
              
              
class Aluno(Pessoa):
    def __init__(self,nome,cpf,rg,matricula):
        super().__init__(nome,cpf,rg)
        self.matricula = matricula  
usuario2 = Aluno("Maria", "987.654.321-00", "SP-87.654.321", "123456")
print(usuario2.nome) 


class Funcionario(Pessoa):
    def __init__(self,nome,cpf,rg,cargo):
        super().__init__(nome,cpf,rg)
        self.cargo = cargo
usuario3 = Funcionario("Carlos", "111.222.333-44", "RJ-55.666.777", "Secretário")
print(usuario3.nome)


class Coordenador(Pessoa):
    def __init__(self,nome,cpf,rg,departamento):
        super().__init__(nome,cpf,rg)
        self.departamento = departamento
usuario4 = Coordenador("Ana", "555.666.777-88", "BA-99.888.777", "Departamento de Coordenação")
print(usuario4.nome)



