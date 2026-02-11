import httpx
from src.utils.api_handler import buscar_municipios
from respx import MockRouter

UF = "SP"


def test_busca_municipío_timeout(respx_mock: MockRouter):
    mocked = respx_mock.get().mock(side_effect=httpx.ReadTimeout("timeout"))

    response = buscar_municipios(UF)

    assert mocked.called
