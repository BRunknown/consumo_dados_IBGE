from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


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
    uf: str
    microrregiao: dict
    regiao_imediata: dict
