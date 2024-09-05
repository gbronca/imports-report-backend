from fastapi import APIRouter

from ...core.monday import monday_client

router = APIRouter()


@router.get("/")
async def read_users():
    return await monday_client.users.fetch_users()
