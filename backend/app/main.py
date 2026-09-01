from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str


app = FastAPI(
    title="Modus API",
    description="API do simulador educativo de custo de interações com LLMs.",
    version="0.1.0",
)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    """Indica se a API está disponível para receber requisições."""
    return HealthResponse(status="ok", service="modus-api")
