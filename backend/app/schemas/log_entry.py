from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.models.models import LogEntryType


class LogEntryBase(BaseModel):
    container_id: int
    customer_id: int
    action: LogEntryType
    notes: Optional[str] = None


class LogEntryCreate(LogEntryBase):
    pass


class LogEntry(LogEntryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True 