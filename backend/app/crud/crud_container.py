from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.models import Container
from app.schemas.container import ContainerCreate, ContainerUpdate


class CRUDContainer(CRUDBase[Container, ContainerCreate, ContainerUpdate]):
    def get_by_container_number(self, db: Session, *, container_number: str) -> Optional[Container]:
        return db.query(Container).filter(Container.container_number == container_number).first()

    def get_by_status(self, db: Session, *, status: str) -> List[Container]:
        return db.query(Container).filter(Container.status == status).all()

    def get_by_customer(self, db: Session, *, customer_id: int) -> List[Container]:
        return db.query(Container).filter(Container.current_customer_id == customer_id).all()


container = CRUDContainer(Container) 