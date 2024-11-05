import json
from cryptography.fernet import Fernet

# Gerar as chaves RSA
p_prime = 61  # Exemplo de número primo
q_prime = 53  # Outro exemplo de número primo
n = p_prime * q_prime
e = 17  # Exemplo de expoente público
d = 2753  # Exemplo de expoente privado (calculado)

# Armazenar as chaves
chaves_rsa = {
    "publica": {"n": n, "e": e},
    "privada": {"n": n, "d": d}
}

# Carregar a chave de criptografia
with open("chave_secreta.key", "rb") as key_file:
    chave_criptografia = key_file.read()

cipher = Fernet(chave_criptografia)

# Serializar e criptografar as chaves RSA
chaves_rsa_json = json.dumps(chaves_rsa).encode()
chaves_rsa_criptografadas = cipher.encrypt(chaves_rsa_json)

# Salvar as chaves criptografadas
with open("chaves_rsa_criptografadas.bin", "wb") as file:
    file.write(chaves_rsa_criptografadas)

print("Chaves RSA criptografadas e salvas em chaves_rsa_criptografadas.bin")
