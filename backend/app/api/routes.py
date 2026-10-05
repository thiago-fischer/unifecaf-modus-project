from fastapi import APIRouter, HTTPException

from app.api.schemas import (
    CatalogModel,
    CatalogOption,
    CatalogResponse,
    ComparisonItem,
    ModelEstimate,
    SimulationRequest,
    SimulationResponse,
)
from app.data import catalog
from app.domain.estimator import Estimate, InvalidSimulationError, compare_models, estimate

router = APIRouter()

GUIDANCE = [
    "Prompts claros e objetivos reduzem tokens de entrada desnecessários.",
    "Peça uma resposta do tamanho que o objetivo realmente exige.",
    "Escolha o modelo de forma proporcional à tarefa: o mais barato nem sempre é o mais "
    "adequado, e o mais caro nem sempre é necessário.",
]
RESULT_DISCLAIMER = (
    "Estimativa educativa baseada em valores fixos por cenário. Não é uma contagem real de "
    "tokens nem a cobrança de um provedor."
)


def _to_schema(item: Estimate) -> dict:
    return {
        "modelId": item.model_id,
        "modelName": item.model_name,
        "inputTokens": item.input_tokens,
        "outputTokens": item.output_tokens,
        "totalTokens": item.total_tokens,
        "cost": float(item.cost),
    }


@router.get("/catalog", response_model=CatalogResponse, tags=["catalog"])
def get_catalog() -> CatalogResponse:
    """Lista modelos, tipos de tarefa e tamanhos de resposta disponíveis."""
    return CatalogResponse(
        models=[
            CatalogModel(
                id=m.id,
                name=m.name,
                inputPricePerMillion=float(m.input_price_per_million),
                outputPricePerMillion=float(m.output_price_per_million),
            )
            for m in catalog.MODELS.values()
        ],
        taskTypes=[CatalogOption(id=t.id, name=t.name) for t in catalog.TASK_TYPES.values()],
        responseSizes=[
            CatalogOption(id=s.id, name=s.name) for s in catalog.RESPONSE_SIZES.values()
        ],
        currency=catalog.CURRENCY,
        updatedAt=catalog.CATALOG_UPDATED_AT,
        disclaimer=catalog.CATALOG_DISCLAIMER,
    )


@router.post(
    "/simulations",
    response_model=SimulationResponse,
    tags=["simulations"],
    responses={422: {"description": "Modelo, tarefa ou tamanho inválido."}},
)
def create_simulation(request: SimulationRequest) -> SimulationResponse:
    """Calcula tokens e custo aproximado e compara o resultado entre os modelos."""
    try:
        result = estimate(request.modelId, request.taskType, request.responseSize)
        comparison = compare_models(request.taskType, request.responseSize)
    except InvalidSimulationError as exc:
        raise HTTPException(
            status_code=422, detail={"code": exc.code, "message": exc.message}
        ) from exc

    return SimulationResponse(
        estimate=ModelEstimate(**_to_schema(result)),
        currency=catalog.CURRENCY,
        comparison=[
            ComparisonItem(**_to_schema(item), selected=item.model_id == result.model_id)
            for item in comparison
        ],
        guidance=GUIDANCE,
        disclaimer=RESULT_DISCLAIMER,
    )
