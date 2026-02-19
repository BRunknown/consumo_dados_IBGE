import sys
from datetime import date

from utils.api_handler import busca_estados, buscar_municipios
from utils.storage import armazenar_dados_brutos, armazena_estados, armazena_municipios
from utils.logger import logger
from utils.database import get_uf_estados


def extracao_estados_ibge():

    try:

        nome_pasta = f"estados/{date.today().strftime('%Y%m%d')}"
         
        nome_arquivo = "estados.json"

        response = busca_estados()
        armazenar_dados_brutos(response,nome_pasta,nome_arquivo)
        armazena_estados(response)

        logger.info("Processo de extração de dados de estados concluido com sucesso!")

        return True

    except Exception as e:
        logger.error(f"Processo falhou! /n erro:{e}")


def extracao_municipio_ibge(uf):
    try:
        nome_arquivo = f"municipios/municipios_{uf}.json"

        response = buscar_municipios(uf)
        armazenar_dados_brutos(response, nome_arquivo)
        armazena_municipios(response)

        logger.info("Processo de extração de dados de municipios concluido com sucesso!")

    except Exception as e:
        logger.error(f"Processo falhou! /n erro:{e}")


if __name__ == "__main__":
    logger.info("app iniciado")

    # extracao_regiao_ibge()
    
    extracao_estados_ibge()

    lista_uf = get_uf_estados()
    
    for uf in lista_uf:
        extracao_municipio_ibge()
    

