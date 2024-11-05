import tkinter as tk
from tkinter import messagebox
import random
import logging

# Configuração do logger
logging.basicConfig(
    filename='rsa_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(message):
    logging.info(message)

# Funções de criptografia e descriptografia
def encrypt_message():
    try:
        p_prime = int(p_entry.get())
        q_prime = int(q_entry.get())
        e_coprime = int(e_entry.get())
        message = message_entry.get()

        # Realiza a criptografia (a lógica de expmod e pub_key deve estar definida)
        n_key = pub_key(p_prime, q_prime)
        encrypted_message = [expmod(ord(char), e_coprime, n_key) for char in message]

        with open("Mensagem_encriptada.txt", "w") as file:
            file.write(" ".join(map(str, encrypted_message)))
        
        log_message(f"Mensagem encriptada: {message} para {encrypted_message}")
        messagebox.showinfo("Sucesso", "Mensagem criptografada e salva!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def decrypt_message():
    try:
        p_prime = int(p_entry.get())
        q_prime = int(q_entry.get())
        e_coprime = int(e_entry.get())
        
        # Lógica para descriptografar a mensagem (a lógica de inverse e descripto deve estar definida)
        n_key = pub_key(p_prime, q_prime)
        k = fi(p_prime, q_prime)
        d_key = inverse(e_coprime, k)

        with open("Mensagem_encriptada.txt", "r") as file:
            encrypted_numbers = list(map(int, file.read().split()))

        decrypted_message = ''.join(chr(descripto(num, d_key, n_key)) for num in encrypted_numbers)
        
        with open("Mensagem_original.txt", "w") as file:
            file.write(decrypted_message)

        log_message(f"Mensagem descriptografada: {decrypted_message}")
        messagebox.showinfo("Sucesso", "Mensagem descriptografada e salva!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Funções auxiliares
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fi(p, q):
    return (p - 1) * (q - 1)

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def expmod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def inverse(e, fi_n):
    t, new_t = 0, 1
    r, new_r = fi_n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("O número não tem inverso multiplicativo")
    if t < 0:
        t += fi_n
    return t

def pub_key(p, q):
    return p * q

def descripto(c, d, n):
    return expmod(c, d, n)

# Configurando a interface gráfica
root = tk.Tk()
root.title("Criptografia RSA")

# Labels e Entradas
tk.Label(root, text="Primo p:").grid(row=0, column=0)
p_entry = tk.Entry(root)
p_entry.grid(row=0, column=1)

tk.Label(root, text="Primo q:").grid(row=1, column=0)
q_entry = tk.Entry(root)
q_entry.grid(row=1, column=1)

tk.Label(root, text="Expoente e:").grid(row=2, column=0)
e_entry = tk.Entry(root)
e_entry.grid(row=2, column=1)

tk.Label(root, text="Mensagem:").grid(row=3, column=0)
message_entry = tk.Entry(root)
message_entry.grid(row=3, column=1)

# Botões
encrypt_button = tk.Button(root, text="Criptografar", command=encrypt_message)
encrypt_button.grid(row=4, column=0)

decrypt_button = tk.Button(root, text="Descriptografar", command=decrypt_message)
decrypt_button.grid(row=4, column=1)

root.mainloop()
