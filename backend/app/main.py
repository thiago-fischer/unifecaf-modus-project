from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


TASK_TYPES: dict[str, int] = {
    "summary": 800,
    "explanation": 500,
    "text": 350,
    "code": 700,
}

RESPONSE_SIZES: dict[str, int] = {
    "small": 150,
    "medium": 500,
    "large": 1000,
}

MODELS: list[dict[str, Any]] = [
    {
        "id": "modus-economico",
        "name": "Modus Econômico",
        "inputPriceUsdPer1M": 0.50,
        "outputPriceUsdPer1M": 1.50,
        "currency": "USD",
        "lastUpdated": "2026-09-14",
    },
    {
        "id": "modus-equilibrado",
        "name": "Modus Equilibrado",
        "inputPriceUsdPer1M": 3.00,
        "outputPriceUsdPer1M": 9.00,
        "currency": "USD",
        "lastUpdated": "2026-09-14",
    },
    {
        "id": "modus-avancado",
        "name": "Modus Avançado",
        "inputPriceUsdPer1M": 10.00,
        "outputPriceUsdPer1M": 30.00,
        "currency": "USD",
        "lastUpdated": "2026-09-14",
    },
]


class HealthResponse(BaseModel):
    status: str
    service: str


class ModelCatalogItem(BaseModel):
    id: str
    name: str
    inputPriceUsdPer1M: float
    outputPriceUsdPer1M: float
    currency: str
    lastUpdated: str


class ModelsResponse(BaseModel):
    models: list[ModelCatalogItem]


class SimulationRequest(BaseModel):
    modelId: str = Field(..., description="Identificador do modelo no catálogo.")
    taskType: str = Field(..., description="Tipo de tarefa de entrada estimada.")
    responseSize: str = Field(..., description="Tamanho esperado da resposta.")


class TokenSummary(BaseModel):
    input: int
    output: int
    total: int


class CostSummary(BaseModel):
    inputUsd: float
    outputUsd: float
    totalUsd: float


class ComparisonItem(BaseModel):
    modelId: str
    modelName: str
    totalTokens: int
    totalCostUsd: float


class SimulationResponse(BaseModel):
    modelId: str
    modelName: str
    taskType: str
    responseSize: str
    tokens: TokenSummary
    cost: CostSummary
    currency: str
    comparison: list[ComparisonItem]
    educationalNote: str
    isEstimate: bool = True


app = FastAPI(
    title="Modus API",
    description="API do simulador educativo de custo de interações com LLMs.",
    version="0.1.0",
)


def _get_model(model_id: str) -> dict[str, Any]:
    for model in MODELS:
        if model["id"] == model_id:
            return model
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Modelo inválido: {model_id}.",
    )


def _validate_choice(choice: str, valid_choices: dict[str, int], field_name: str) -> str:
    if choice not in valid_choices:
        valid_choices_text = ", ".join(sorted(valid_choices))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} inválido: '{choice}'. Opções válidas: {valid_choices_text}.",
        )
    return choice


def _calculate_total_cost(model: dict[str, Any], input_tokens: int, output_tokens: int) -> tuple[float, float, float]:
    input_cost = (input_tokens / 1_000_000) * float(model["inputPriceUsdPer1M"])
    output_cost = (output_tokens / 1_000_000) * float(model["outputPriceUsdPer1M"])
    total_cost = input_cost + output_cost
    return input_cost, output_cost, total_cost


def _build_comparison(model_id: str, task_type: str, response_size: str) -> list[ComparisonItem]:
    comparison: list[ComparisonItem] = []
    for model in MODELS:
        input_tokens = TASK_TYPES[task_type]
        output_tokens = RESPONSE_SIZES[response_size]
        total_tokens = input_tokens + output_tokens
        _, _, total_cost = _calculate_total_cost(model, input_tokens, output_tokens)
        comparison.append(
            ComparisonItem(
                modelId=model["id"],
                modelName=model["name"],
                totalTokens=total_tokens,
                totalCostUsd=round(total_cost, 6),
            )
        )

    return sorted(comparison, key=lambda item: item.totalCostUsd)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    """Indica se a API está disponível para receber requisições."""
    return HealthResponse(status="ok", service="modus-api")


@app.get("/models", response_model=ModelsResponse, tags=["catalog"])
def list_models() -> ModelsResponse:
    """Lista o catálogo estático de modelos disponíveis para simulação."""
    return ModelsResponse(models=[ModelCatalogItem(**model) for model in MODELS])


@app.post("/simulate", response_model=SimulationResponse, tags=["simulation"])
def simulate(request: SimulationRequest) -> SimulationResponse:
    """Calcula uma estimativa determinística de tokens e custo para a combinação escolhida."""
    model = _get_model(request.modelId)
    _validate_choice(request.taskType, TASK_TYPES, "taskType")
    _validate_choice(request.responseSize, RESPONSE_SIZES, "responseSize")

    input_tokens = TASK_TYPES[request.taskType]
    output_tokens = RESPONSE_SIZES[request.responseSize]
    total_tokens = input_tokens + output_tokens

    input_cost, output_cost, total_cost = _calculate_total_cost(model, input_tokens, output_tokens)

    comparison = _build_comparison(request.modelId, request.taskType, request.responseSize)

    response = SimulationResponse(
        modelId=model["id"],
        modelName=model["name"],
        taskType=request.taskType,
        responseSize=request.responseSize,
        tokens={
            "input": input_tokens,
            "output": output_tokens,
            "total": total_tokens,
        },
        cost={
            "inputUsd": round(input_cost, 6),
            "outputUsd": round(output_cost, 6),
            "totalUsd": round(total_cost, 6),
        },
        currency="USD",
        comparison=comparison,
        educationalNote=(
            "A estimativa considera o tamanho do contexto e da resposta para educar sobre o custo "
            "aproximado de uma interação com IA. Prompts claros e respostas proporcionais ajudam a usar "
            "melhor os recursos disponíveis."
        ),
    )
    return response
