import json
import logging

import httpx

from utils.logger import logger
from utils.settings import Settings
from utils.client_setup import client


def buscar_municipios(uf, client=client):
    """Busca municípios de uma UF e salva em JSON"""
    nome_arquivo = f"{Settings().RESPONSE_SAVE_PATH}/municipios_{uf}.json"

    logger.info(f"=== Iniciando busca de municípios para {uf} === ")

    try:
        # Fazer a requisição
        logger.debug("Conectando à API do IBGE... ")
        response = client.get(
            f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
        )

        logger.debug(f"Status HTTP: {response.status_code} ")
        response.raise_for_status()

        # Processar resposta - SEPARAR
        dados = response.json()
        logger.info(f"✓ Dados recebidos: {len(dados)} municípios ")

        # Salvar arquivo - SEPARAR em outro módulo
        logger.debug(f"Salvando dados em {nome_arquivo}... ")
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        logger.info(f"✓ Arquivo salvo: {nome_arquivo} ")

        # Log de exemplo dos primeiros municípios
        if logger.isEnabledFor(logging.DEBUG) and dados:
            logger.debug("Primeiros 3 municípios: ")
            for i, municipio in enumerate(dados[:3], 1):
                nome = municipio.get("nome", "N/A")
                id_municipio = municipio.get("id", "N/A")
                logger.debug(f"  {i}. {nome} (ID: {id_municipio})")

        return True

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
