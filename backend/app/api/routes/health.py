from fastapi import APIRouter

from app.core.config import SERVICE_NAME
from app.schemas.health import HealthResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Indica se a API está disponível para receber requisições."""
    return HealthResponse(status="ok", service=SERVICE_NAME)
