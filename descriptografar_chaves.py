import json
from cryptography.fernet import Fernet

# Carregar a chave de criptografia
with open("chave_secreta.key", "rb") as key_file:
    chave_criptografia = key_file.read()

cipher = Fernet(chave_criptografia)

# Ler o arquivo criptografado
with open("chaves_criptografadas.bin", "rb") as file:
    chaves_criptografadas = file.read()

# Descriptografar o conteúdo
try:
    chaves_json = cipher.decrypt(chaves_criptografadas)
    chaves = json.loads(chaves_json.decode())  # Decodificar de bytes para string e carregar JSON

    # Acessar as chaves
    chave_publica = chaves["publica"]
    chave_privada = chaves["privada"]
    print("Chave pública:", chave_publica)
    print("Chave privada:", chave_privada)
except Exception as e:
    print("Erro ao descriptografar ou carregar JSON:", e)
