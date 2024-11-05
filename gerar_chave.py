from cryptography.fernet import Fernet

# Gerar uma nova chave
chave_nova = Fernet.generate_key()

# Salvar a chave em um arquivo
with open("chave_secreta.key", "wb") as key_file:
    key_file.write(chave_nova)

print("Nova chave gerada e salva em chave_secreta.key")
