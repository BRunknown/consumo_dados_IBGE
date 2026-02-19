import httpx
from main import extracao_estados_ibge, extracao_municipio_ibge
from respx import MockRouter

def test_extracao_estados_ibge():
    extracao_municipio_ibge()
    retorno = extracao_estados_ibge()

    assert retorno

