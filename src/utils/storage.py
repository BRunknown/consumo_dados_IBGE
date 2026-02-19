import json

from pathlib import Path

from sqlalchemy import select

from utils.database import get_session
from utils.logger import logger
from utils.models import Estado, Municipio, Regiao
from utils.schemas import EstadoSchema, MunicipioSchema, RegiaoSchema
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


def armazena_estados(response):

    try:
        lista_estados = [EstadoSchema(**item) for item in response.json()]

        with get_session() as session:
            for estado in lista_estados:
                db_estado = session.scalar(
                    select(Estado).where(Estado.id_estado == estado.id)
                )

                if db_estado:
                    logger.debug(f"Informações já registradas! /n {estado}")
                    continue

                db_estado = Estado(
                    id_estado=estado.id,
                    nome_estado=estado.nome,
                    cod_estado=estado.sigla,
                    id_regiao=estado.regiao.id,
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


def armazena_municipios(uf, response):
    try:
        lista_municipios = [MunicipioSchema(**item) for item in response.json()]

        with get_session() as session:
            for municipio in lista_municipios:
                db_municipio = session.scalar(
                    select(Municipio).where(Municipio.id_municipio == municipio.id)
                )

                if db_municipio:
                    logger.debug(f"Informações já registradas! /n {municipio}")
                    continue

                db_municipio = Municipio(
                    id_municipio=municipio.id,
                    nome_municipio=municipio.nome,
                    cod_estado=uf,
                    microrregiao=municipio.microrregiao,
                    regiao_imediata=municipio.regiao_imediata,
                )

                session.add(db_municipio)
                session.commit()
                session.refresh(db_municipio)

                logger.info(f"municipio {municipio.nome} registrado com sucesso!")

        return

    except Exception as e:
        logger.error(
            f"erro ao salvar requisição: {e}, id:{response.extensions.get('request_id')}"
        )


def armazena_regioes(response):
    try:
        lista_regioes = [RegiaoSchema(**item) for item in response.json()]

        with get_session() as session:
            for regiao in lista_regioes:
                db_regiao = session.scalar(
                    select(Regiao).where(Regiao.id_regiao == regiao.id)
                )

                if db_regiao:
                    logger.debug(f"Informações já registradas! /n {regiao}")
                    continue

                db_regiao = Regiao(
                    id_regiao=regiao.id,
                    cod_regiao=regiao.sigla,
                    nome_regiao=regiao.nome,
                )

                session.add(db_regiao)
                session.commit()
                session.refresh(db_regiao)

                logger.info(f"regiao {regiao.nome} registrado com sucesso!")

        return

    except Exception as e:
        logger.error(
            f"erro ao salvar requisição: {e}, id:{response.extensions.get('request_id')}"
        )
