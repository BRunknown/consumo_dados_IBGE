import json

import httpx
import respx

from src.utils.logger import logger
from src.utils.client_setup import client

uf = "MG"


def busca_municipios(uf, client=client):
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


@respx.mock()
def test_busca_municipío_timeout(uf=uf):

    mocked = respx.get(
        f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    ).mock(side_effect=httpx.Response(504))

    response = busca_municipios(uf)

    assert mocked.called
    assert not response
