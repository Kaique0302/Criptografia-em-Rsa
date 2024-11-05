# Retorna o MDC dos dois números
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Verifica se o número é primo
def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Calcula a função totiente fi(n), que é (p-1)*(q-1)
def fi(p, q):
    return (p - 1) * (q - 1)

# Retorna a chave pública n, que é o produto dos números primos p e q
def pub_key(p, q):
    return p * q

# Retorna o resultado da exponenciação modular: (base ^ expoente) % modulo
def expmod(base, expoente, modulo):
    result = 1
    while expoente > 0:
        if expoente % 2 == 1:
            result = (result * base) % modulo
        expoente = expoente >> 1
        base = (base * base) % modulo
    return result

# Calcula o inverso de uma chave em relação a um módulo (usado para encontrar a chave privada)
def inverse(chave, modulo):
    t, new_t = 0, 1
    r, new_r = modulo, chave
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("O número não tem inverso multiplicativo")
    if t < 0:
        t += modulo
    return t

# Desencripta o valor criptografado, retornando o caractere correspondente
def descripto(base, expoente, mod):
    return chr(expmod(base, expoente, mod))
