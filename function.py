# Retorna o MDC dos dois números
def mdc(a, b):
    return a if b == 0 else mdc(b, a % b)

# Verifica se o número é primo
def prime(num):
    if num in (0, 1):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Calcula a função totiente fi(n), que é (p-1)*(q-1)
def fi(p, q):
    return (p - 1) * (q - 1)

# Retorna a chave pública n, que é o produto dos números primos p e q
def pub_key(p, q):
    return p * q

# Retorna o resultado da exponenciação modular: (base ^ expoente) % modulo
def expmod(base, expoente, modulo):
    t = 1
    for _ in range(expoente):
        t = (t * base) % modulo
    return t

# Calcula o inverso modular da chave em relação ao módulo
def inverse(chave, modulo):
    i = 1
    while i <= modulo:
        if (chave * i) % modulo == 1:
            return i
        i += 1
    raise ValueError("Inverso não encontrado")  # Exceção para garantir que o inverso existe

# Desencripta o valor criptografado, retornando o caractere correspondente
def descripto(base, expoente, mod):
    return chr(expmod(base, expoente, mod))
