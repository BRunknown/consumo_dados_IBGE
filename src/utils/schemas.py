from pydantic import BaseModel, Field


class RegiaoSchema(BaseModel):
    id: int
    sigla: str
    nome: str


class EstadoSchema(BaseModel):
    id: int
    nome: str
    sigla: str
    regiao: RegiaoSchema


class MunicipioSchema(BaseModel):
    id: int
    nome: str
    microrregiao: dict
    regiao_imediata: dict = Field(alias="regiao-imediata")
