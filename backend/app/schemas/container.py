from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.models.models import ContainerStatus


class ContainerBase(BaseModel):
    container_number: str
    status: Optional[ContainerStatus] = ContainerStatus.AVAILABLE
    location: Optional[str] = None
    notes: Optional[str] = None


class ContainerCreate(ContainerBase):
    pass


class ContainerUpdate(ContainerBase):
    container_number: Optional[str] = None
    current_customer_id: Optional[int] = None


class Container(ContainerBase):
    id: int
    current_customer_id: Optional[int] = None

    class Config:
        from_attributes = True 