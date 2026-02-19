from contextlib import contextmanager

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from utils.settings import Settings
from utils.models import Estado

engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session() -> Session:
    """Context manager that yields a database session."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_uf_estados(session: Session):
    try:
        lista_uf_estados = session.scalar(select(Estado.uf))
        if lista_uf_estados:
            return lista_uf_estados

    except Exception as e:
        raise e
