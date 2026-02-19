import json
import logging

import httpx

from utils.logger import logger
from utils.settings import Settings
from utils.client_setup import client


#refatorar isso aqui

def buscar_regiao():
    ...

def busca_estados(client=client):
    try:

        response = client.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        logger.debug(f"Status HTTP: {response.status_code} ")

        response.raise_for_status()
        
        return response 

    except httpx.HTTPStatusError as e:
        logger.error(f"✗ Erro HTTP {e.response.status_code}: {e} ")
        return False
    except httpx.RequestError as e:
        logger.error(f"✗ Erro de conexão: {e} ")
        return False
    except json.JSONDecodeError as e:
        logger.error(f"✗ Erro no formato JSON: {e} ")
        return False
    except IOError as e:
        logger.error(f"✗ Erro de I/O: {e} ")
        return False
    except Exception as e:
        logger.exception(f"✗ Erro inesperado: {e} ")
        return False



def buscar_municipios(uf, client=client):
    """Busca municípios de uma UF e salva em JSON"""


    logger.info(f"=== Iniciando busca de municípios para {uf} === ")

    try:
        # Fazer a requisição
        logger.debug("Conectando à API do IBGE... ")
        response = client.get(
            f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
        )

        logger.debug(f"Status HTTP: {response.status_code} ")

        response.raise_for_status()
        
        dados = response.json()
        # Log de exemplo dos primeiros municípios
        if logger.isEnabledFor(logging.DEBUG) and dados:
            logger.debug("Primeiros 3 municípios: ")
            for i, municipio in enumerate(dados[:3], 1):
                nome = municipio.get("nome", "N/A")
                id_municipio = municipio.get("id", "N/A")
                logger.debug(f"  {i}. {nome} (ID: {id_municipio})")

        return response

    except httpx.HTTPStatusError as e:
        logger.error(f"✗ Erro HTTP {e.response.status_code}: {e} ")
        return False
    except httpx.RequestError as e:
        logger.error(f"✗ Erro de conexão: {e} ")
        return False
    except json.JSONDecodeError as e:
        logger.error(f"✗ Erro no formato JSON: {e} ")
        return False
    except IOError as e:
        logger.error(f"✗ Erro de I/O: {e} ")
        return False
    except Exception as e:
        logger.exception(f"✗ Erro inesperado: {e} ")
        return False
