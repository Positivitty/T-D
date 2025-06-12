from typing import Optional, List
from pydantic import BaseModel
from .container import Container


class CustomerBase(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    job_site_info: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    name: Optional[str] = None


class Customer(CustomerBase):
    id: int
    current_containers: List[Container] = []

    class Config:
        from_attributes = True 