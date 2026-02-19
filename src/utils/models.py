from typing import Any

from sqlalchemy import PickleType, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Regiao:
    __tablename__ = "regioes_ibge"

    id_regiao: Mapped[int] = mapped_column(primary_key=True)
    cod_regiao: Mapped[str]
    nome_regiao: Mapped[str]


@table_registry.mapped_as_dataclass
class Estado:
    __tablename__ = "estados_ibge"

    id_estado: Mapped[int] = mapped_column(primary_key=True)
    nome_estado: Mapped[str] = mapped_column(unique=True)
    cod_estado: Mapped[str] = mapped_column(unique=True)
    id_regiao: Mapped[int] = mapped_column(
        ForeignKey(
            "regioes_ibge.id_regiao", ondelete="cascade", onupdate="cascade"
        )
    )


# TO-DO: criar tabelas para microregião e reigião imediata
@table_registry.mapped_as_dataclass
class Municipio:
    __tablename__ = "munícipios_ibge"

    id_municipio: Mapped[str] = mapped_column(primary_key=True)
    nome_municipio: Mapped[str]
    cod_estado: Mapped[str] = mapped_column(
        ForeignKey(
            "estados_ibge.id_estado", ondelete="cascade", onupdate="cascade"
        )
    )
    microrregiao: Mapped[Any] = mapped_column(PickleType)
    regiao_imediata: Mapped[Any] = mapped_column(PickleType)
