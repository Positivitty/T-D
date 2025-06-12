from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.models import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> List[Customer]:
        return db.query(Customer).filter(Customer.name.ilike(f"%{name}%")).all()

    def get_by_phone(self, db: Session, *, phone: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.phone == phone).first()


customer = CRUDCustomer(Customer) 