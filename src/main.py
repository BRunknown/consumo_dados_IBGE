from datetime import date

from utils.api_handler import busca_estados, busca_municipios, busca_regioes
from utils.database import get_uf_estados
from utils.logger import logger
from utils.storage import (
    armazena_estados,
    armazena_municipios,
    armazena_regioes,
    armazenar_dados_brutos,
)


def extracao_estados_ibge():

    try:
        nome_pasta = f"estados/{date.today().strftime('%Y%m%d')}"

        nome_arquivo = "estados.json"

        response = busca_estados()
        armazenar_dados_brutos(response, nome_pasta, nome_arquivo)
        armazena_estados(response)

        logger.info("Processo de extração de dados de estados concluido com sucesso!")

        return True

    except Exception as e:
        logger.error(f"Processo falhou! /n erro:{e}")


def extracao_regiao_ibge():
    nome_pasta = f"regioes/{date.today().strftime('%Y%m%d')}"
    nome_arquivo = "regioes.json"

    response = busca_regioes()
    armazenar_dados_brutos(response, nome_pasta, nome_arquivo)
    armazena_regioes(response)

    logger.info("Processo de extração de regiões concluidas com sucesso")


def extracao_municipio_ibge(uf):
    try:
        nome_pasta = f"municipios/{date.today().strftime('%Y%m%d')}"
        nome_arquivo = f"municipios_{uf}.json"

        response = busca_municipios(uf)
        armazenar_dados_brutos(response, nome_pasta, nome_arquivo)
        armazena_municipios(uf, response)

        logger.info(
            "Processo de extração de dados de municipios concluido com sucesso!"
        )

    except Exception as e:
        logger.error(f"Processo falhou! /n erro:{e}")


if __name__ == "__main__":
    logger.info("app iniciado")

    extracao_regiao_ibge()

    extracao_estados_ibge()

    lista_uf = get_uf_estados()

    for uf in lista_uf:
        extracao_municipio_ibge(uf)
