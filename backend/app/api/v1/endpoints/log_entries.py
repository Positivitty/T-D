from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.log_entry import LogEntry, LogEntryCreate

router = APIRouter()


@router.get("/", response_model=List[LogEntry])
def read_log_entries(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve log entries.
    """
    log_entries = crud.log_entry.get_multi(db, skip=skip, limit=limit)
    return log_entries


@router.post("/", response_model=LogEntry)
def create_log_entry(
    *,
    db: Session = Depends(deps.get_db),
    log_entry_in: LogEntryCreate,
):
    """
    Create new log entry.
    """
    return crud.log_entry.create(db, obj_in=log_entry_in)


@router.get("/container/{container_id}", response_model=List[LogEntry])
def read_container_log_entries(
    *,
    db: Session = Depends(deps.get_db),
    container_id: int,
):
    """
    Get log entries for a specific container.
    """
    log_entries = crud.log_entry.get_by_container(db, container_id=container_id)
    return log_entries


@router.get("/customer/{customer_id}", response_model=List[LogEntry])
def read_customer_log_entries(
    *,
    db: Session = Depends(deps.get_db),
    customer_id: int,
):
    """
    Get log entries for a specific customer.
    """
    log_entries = crud.log_entry.get_by_customer(db, customer_id=customer_id)
    return log_entries 