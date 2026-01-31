# 1) .upper() = Transformar em letras maiúsculas
texto = "python"
print(texto.upper())

# 2) .lower() = Transformar em letras minúsculas
texto = "PYTHON"
print(texto.lower())

# 3) .capitalize() = Primeira letra maiúscula
# Coloca apenas a primeira letra em maiúscula
texto = "python"
print(texto.capitalize())

# 4) .title() = Primeira letra de cada palavra maiúscula
texto = "programação python"
print(texto.title())

# 5) .strip() = Remove espaços do início e do fim
texto = "  programação python  "
print(texto.strip())

# 6) .replace() = Substituir texto
texto = "programação python"
print(texto.replace("python", "Java"))

# -----------------------------------------------------
# Aplicação prática com input

nome = input("Digite seu nome completo: ").upper().strip()
mensagem = input("Digite uma mensagem: ").strip().capitalize()

# Exibir os resultados
print("\n--- RESULTADO FINAL ---")
print(f"Nome: {nome}")
print(f"Mensagem: {mensagem}")

















