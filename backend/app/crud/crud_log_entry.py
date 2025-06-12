from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.models import LogEntry
from app.schemas.log_entry import LogEntryCreate, LogEntry as LogEntrySchema


class CRUDLogEntry(CRUDBase[LogEntry, LogEntryCreate, LogEntrySchema]):
    def get_by_container(self, db: Session, *, container_id: int) -> List[LogEntry]:
        return (
            db.query(LogEntry)
            .filter(LogEntry.container_id == container_id)
            .order_by(LogEntry.timestamp.desc())
            .all()
        )

    def get_by_customer(self, db: Session, *, customer_id: int) -> List[LogEntry]:
        return (
            db.query(LogEntry)
            .filter(LogEntry.customer_id == customer_id)
            .order_by(LogEntry.timestamp.desc())
            .all()
        )


log_entry = CRUDLogEntry(LogEntry) 