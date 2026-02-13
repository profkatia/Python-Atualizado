#IMPORTANDO A BIBLIOTECA GETPASS

'''Uma  Biblioteca para ocultar os digitos utilizado para senha'''
import getpass
username = input("Digite seu nome de usuario")
password =  getpass.getpass("Digite sua senha")

print(f"Usuario :{username} , senha: {password}")