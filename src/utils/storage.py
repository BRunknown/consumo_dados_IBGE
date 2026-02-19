import json
import os
from pathlib import Path

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from utils.logger import logger
from utils.models import Estado
from utils.schemas import EstadoSchema
from utils.settings import Settings



def armazenar_dados_brutos(response, nome_pasta, nome_arquivo):
    try:
        folderpath = f"{Settings().RESPONSE_SAVE_PATH}/{nome_pasta}"
        filepath = f"{folderpath}/{nome_arquivo}"

        folder_path = Path(folderpath)
        folder_path.mkdir(parents=True, exist_ok=True)

        logger.debug(f"Salvando dados em {filepath}... ")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(
            f"erro ao salvar requisição: {e}, id:{response.extensions.get('request_id')}"
        )


def armazena_estados(response, session=Session):

    try:
        lista_estados = [EstadoSchema(**item) for item in response.json()]

        for estado in lista_estados:
            db_estado = session.scalar(select(Estado).where(Estado.id_estado == estado.id))

            if db_estado:
                logger.debug(f"Informações já registradas! /n {estado}")
                continue

            db_estado = Estado(
                id=estado.id, nome=estado.nome, sigla=estado.sigla, regiao=estado.regiao
            )

            session.add(db_estado)
            session.commit()
            session.refresh(db_estado)

            logger.info(f"estado {estado.nome} registrado com sucesso!")

        return

    except Exception as e:
        logger.error(
            f"erro ao salvar requisição: {e}, id:{response.extensions.get('request_id')}"
        )


def armazena_municipios(): ...


def armazena_regioes(): ...
