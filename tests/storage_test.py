import json
import pytest
from pathlib import Path
from tempfile import gettempdir

from httpx import Response

from src.utils.storage import armazenar_dados_brutos






# def test_armazenar_dados_brutos(temp_folder):
#     response = Response(status_code=200, content='{"oi": "teste"}')
#     nome_arquivo = "teste.json"

#     armazenar_dados_brutos(response, temp_folder, nome_arquivo)

#     assert (temp_folder / nome_arquivo).exists()

# def busca_estados():
    
    