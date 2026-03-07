from http import HTTPStatus

import httpx
import respx

from utils.api_handler import busca_municipios

uf = "MG"


@respx.mock
def test_client(client):
    respx.get("").mock(return_value=httpx.Response(200))

    response = client.get("")

    assert response.status_code == HTTPStatus.OK


@respx.mock
def test_tratativa_erro_http(client, uf=uf):

    url = f"estados/{uf}/municipios"

    respx.get(url).mock(return_value=httpx.Response(504))

    response = busca_municipios(uf, client=client)

    assert not response
