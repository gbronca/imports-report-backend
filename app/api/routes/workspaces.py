from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_workspaces():
    return [{"name": "Workspace 1"}, {"name": "Workspace 2"}]
