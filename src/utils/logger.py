import logging
import sys

from utils.settings import Settings



# Configurar o logger
def setup_logger(log_to_console=True):
    """Configura o logger com opção para salvar em arquivo"""
    logger = logging.getLogger(__name__)
    logger.setLevel(Settings().LOG_LEVEL)  # Captura todos os níveis

    # Formato das mensagens
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
    )

    # Handler para terminal (stdout)
    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)  # Mostra INFO e acima no terminal
        console_handler.setFormatter(formatter)

    # Adicionar handlers
    logger.addHandler(console_handler)

    return logger


# Criar e configurar o logger
logger = setup_logger(
    log_to_console=Settings().CONSOLE_LOG
)  # Altere para True para salvar em arquivo também
