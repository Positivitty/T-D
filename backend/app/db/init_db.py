from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.models import base  # noqa: F401
from app.db.session import engine

# Make sure all SQLAlchemy models are imported before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly


def init_db(db: Session) -> None:
    base.Base.metadata.create_all(bind=engine) 