from fastapi import FastAPI

from app.api.endpoints import hello


def create_api():
    api = FastAPI()

    api.include_router(hello.router)

    return api
