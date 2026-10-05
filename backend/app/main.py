from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import APP_DESCRIPTION, APP_NAME, APP_VERSION


def create_app() -> FastAPI:
    application = FastAPI(
        title=APP_NAME,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
    )
    application.include_router(api_router)
    return application


app = create_app()
