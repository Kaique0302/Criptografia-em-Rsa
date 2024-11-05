import logging

# Configuração do logger
logging.basicConfig(
    filename='rsa_log.txt',  # Nome do arquivo de log
    level=logging.INFO,       # Nível do log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

# Função para registrar mensagens
def log_message(message):
    logging.info(message)

