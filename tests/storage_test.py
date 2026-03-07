import os
from httpx import Response

from src.utils.storage import armazenar_dados_brutos
from src.utils.settings import Settings


def test_armazenar_dados_brutos(tmp_path):

    response = Response(status_code=200, content='{"oi": "teste"}')
    nome_arquivo = "teste.json"

    armazenar_dados_brutos(response, tmp_path, nome_arquivo)                    

    assert os.path.exists(
        f"{Settings().RESPONSE_SAVE_PATH}/{tmp_path._str}/{nome_arquivo}"
    )
 