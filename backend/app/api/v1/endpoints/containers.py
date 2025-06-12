from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.container import Container, ContainerCreate, ContainerUpdate
from app.models.models import ContainerStatus

router = APIRouter()


@router.get("/", response_model=List[Container])
def read_containers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    status: Optional[ContainerStatus] = None,
):
    """
    Retrieve containers with optional status filter.
    """
    if status:
        containers = crud.container.get_by_status(db, status=status)
    else:
        containers = crud.container.get_multi(db, skip=skip, limit=limit)
    return containers


@router.post("/", response_model=Container)
def create_container(
    *,
    db: Session = Depends(deps.get_db),
    container_in: ContainerCreate,
):
    """
    Create new container.
    """
    container = crud.container.get_by_container_number(
        db, container_number=container_in.container_number
    )
    if container:
        raise HTTPException(
            status_code=400,
            detail="Container with this number already exists.",
        )
    return crud.container.create(db, obj_in=container_in)


@router.get("/{container_id}", response_model=Container)
def read_container(
    *,
    db: Session = Depends(deps.get_db),
    container_id: int,
):
    """
    Get container by ID.
    """
    container = crud.container.get(db, id=container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return container


@router.put("/{container_id}", response_model=Container)
def update_container(
    *,
    db: Session = Depends(deps.get_db),
    container_id: int,
    container_in: ContainerUpdate,
):
    """
    Update container.
    """
    container = crud.container.get(db, id=container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return crud.container.update(db, db_obj=container, obj_in=container_in)


@router.delete("/{container_id}", response_model=Container)
def delete_container(
    *,
    db: Session = Depends(deps.get_db),
    container_id: int,
):
    """
    Delete container.
    """
    container = crud.container.get(db, id=container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return crud.container.remove(db, id=container_id) 