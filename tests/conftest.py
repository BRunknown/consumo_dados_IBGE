import pytest
import httpx
import respx


@pytest.fixture
def temp_folder(tmp_path):
    # Criar estrutura de pastas
    pasta_dados = tmp_path / "teste"
    pasta_dados.mkdir()

    yield pasta_dados


@pytest.fixture(scope="session")
@respx.mock
def client():
    client = httpx.Client(
        base_url="https://servicodados.ibge.gov.br/api/v1/localidades"
    )
    return client
