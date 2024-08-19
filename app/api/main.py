from fastapi import APIRouter
from app.api.routes import workspaces

api_router = APIRouter()
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
