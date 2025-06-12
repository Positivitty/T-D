from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.customer import Customer, CustomerCreate, CustomerUpdate

router = APIRouter()


@router.get("/", response_model=List[Customer])
def read_customers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve customers.
    """
    customers = crud.customer.get_multi(db, skip=skip, limit=limit)
    return customers


@router.post("/", response_model=Customer)
def create_customer(
    *,
    db: Session = Depends(deps.get_db),
    customer_in: CustomerCreate,
):
    """
    Create new customer.
    """
    return crud.customer.create(db, obj_in=customer_in)


@router.get("/{customer_id}", response_model=Customer)
def read_customer(
    *,
    db: Session = Depends(deps.get_db),
    customer_id: int,
):
    """
    Get customer by ID.
    """
    customer = crud.customer.get(db, id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put("/{customer_id}", response_model=Customer)
def update_customer(
    *,
    db: Session = Depends(deps.get_db),
    customer_id: int,
    customer_in: CustomerUpdate,
):
    """
    Update customer.
    """
    customer = crud.customer.get(db, id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.customer.update(db, db_obj=customer, obj_in=customer_in)


@router.delete("/{customer_id}", response_model=Customer)
def delete_customer(
    *,
    db: Session = Depends(deps.get_db),
    customer_id: int,
):
    """
    Delete customer.
    """
    customer = crud.customer.get(db, id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.customer.remove(db, id=customer_id)


@router.get("/search/{name}", response_model=List[Customer])
def search_customers(
    *,
    db: Session = Depends(deps.get_db),
    name: str,
):
    """
    Search customers by name.
    """
    customers = crud.customer.get_by_name(db, name=name)
    return customers 