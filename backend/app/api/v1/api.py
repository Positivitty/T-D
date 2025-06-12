from fastapi import APIRouter

from app.api.v1.endpoints import containers, customers, log_entries

api_router = APIRouter()
api_router.include_router(containers.router, prefix="/containers", tags=["containers"])
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(log_entries.router, prefix="/log-entries", tags=["log-entries"]) 