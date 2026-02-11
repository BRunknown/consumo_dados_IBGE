# Executar
from utils.logger import logger
from utils.api_handler import buscar_municipios
import sys

if __name__ == "__main__":
    UF = "SP"

    logger.info("Script iniciado")
    
    retorno = buscar_municipios(UF)

    if retorno:
        logger.info("Processo concluído com sucesso!")
    else:
        logger.error("Processo falhou!")
        sys.exit(1)
