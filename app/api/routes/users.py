from fastapi import APIRouter, Query

from ...core.monday import monday_client

router = APIRouter()


@router.get("/")
async def read_users(
    ids: str | list[str] | None = Query(None),
    emails: str | list[str] | None = Query(None),
    kind: str | None = None,
    limit: int | None = None,
    name: str | None = None,
    page: int = 1,
) -> dict:
    return await monday_client.users.fetch_users(
        ids=ids, emails=emails, kind=kind, limit=limit, name=name, page=page
    )


@router.get("/{user_id}")
async def read_user(user_id: str) -> dict:
    return await monday_client.users.fetch_users(ids=user_id)
