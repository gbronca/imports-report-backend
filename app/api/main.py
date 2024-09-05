from fastapi import APIRouter  # noqa: D100

from app.api.routes import users, workspaces

api_router = APIRouter()
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
