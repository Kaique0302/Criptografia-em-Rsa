from cryptography.fernet import Fernet
import json

# Carregar a chave de criptografia
with open("chave_secreta.key", "rb") as key_file:
    chave_criptografia = key_file.read()

cipher = Fernet(chave_criptografia)

# Ler e descriptografar o arquivo de chaves criptografado
with open("chaves_criptografadas.bin", "rb") as file:  # Novo nome de extensão
    chaves_criptografadas = file.read()

# Descriptografar e carregar o JSON
chaves_json = cipher.decrypt(chaves_criptografadas)
chaves = json.loads(chaves_json.decode())

# Acessar as chaves
chave_publica = chaves["publica"]
chave_privada = chaves["privada"]
