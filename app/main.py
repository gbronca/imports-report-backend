from fastapi import FastAPI  # noqa: D100
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router

app = FastAPI()


origins = [
    "http://localhost:5173/",
    "http://127.0.0.1:49449",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
