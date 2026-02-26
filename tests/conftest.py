import pytest
import httpx
import respx


@pytest.fixture(scope="session")
@respx.mock
def client():
    client = httpx.Client(
        base_url="https://servicodados.ibge.gov.br/api/v1/localidades"
    )
    return client


