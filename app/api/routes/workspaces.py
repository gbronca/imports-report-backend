from fastapi import APIRouter

from ...core.monday import monday_client

router = APIRouter()


@router.get("/")
async def read_workspaces():
    return await monday_client.workspaces.fetch_workspaces()
