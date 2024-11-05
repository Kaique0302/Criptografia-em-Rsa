import json
from cryptography.fernet import Fernet

# Carregar a chave de criptografia
with open("chave_secreta.key", "rb") as key_file:
    chave_criptografia = key_file.read()

cipher = Fernet(chave_criptografia)

# Dados das chaves
chaves = {
    "publica": {"n": 143, "e": 13},
    "privada": {"n": 143, "d": 37}
}

# Serializar e criptografar
chaves_json = json.dumps(chaves).encode()  # Converter para bytes
chaves_criptografadas = cipher.encrypt(chaves_json)

# Salvar o arquivo criptografado
with open("chaves_criptografadas.bin", "wb") as file:
    file.write(chaves_criptografadas)

print("Chaves criptografadas e salvas em chaves_criptografadas.bin")
