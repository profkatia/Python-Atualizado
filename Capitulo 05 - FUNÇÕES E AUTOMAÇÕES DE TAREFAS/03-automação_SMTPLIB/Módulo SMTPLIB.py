import smtplib
import ssl
import getpass
from email.message import EmailMessage

# --- CONFIGURAÇÕES ---
remetente = "profkatia2025@gmail.com"
destinatarios = ["profkatia2025@gmail.com"]

senha_app = getpass.getpass("Digite a senha do Email: ")

# --- CRIANDO A MENSAGEM ---
msg = EmailMessage()
msg["Subject"] = "Email enviado com o Python"
msg["From"] = remetente
msg["To"] = ", ".join(destinatarios)

msg.set_content("""
Olá pessoal!

Este email está sendo enviado na aula de Python.
Até mais...
""")

# --- ENVIANDO ---
contexto_ssl = ssl.create_default_context()

try:
    print("Tentando conectar ao servidor...")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=contexto_ssl)
        server.login(remetente, senha_app)
        print("Login bem-sucedido!")

        server.send_message(msg)
        print("Email enviado com sucesso!")

except Exception as e:
    print(f"Ocorreu erro ao enviar o email: {e}")
