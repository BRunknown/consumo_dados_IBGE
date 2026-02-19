from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from utils.settings import Settings
from utils.models import Estado

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def get_uf_estados(session: Session):
    try:
        lista_uf_estados = session.scalar(select(Estado.uf))
        if lista_uf_estados:
            return lista_uf_estados
    
    except Exception as e:
        raise e
    
