"""Motor de estimativa de tokens e custo.

Função pura e determinística, independente de FastAPI e sem acesso à rede.
Regras: `specs/06-regras-de-estimativa.md`.
"""

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

from app.data.catalog import MODELS, RESPONSE_SIZES, TASK_TYPES, ModelInfo

ONE_MILLION = Decimal(1_000_000)
SIX_DECIMALS = Decimal("0.000001")


class InvalidSimulationError(ValueError):
    """Escolha inválida: modelo, tarefa ou tamanho inexistente no catálogo."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class Estimate:
    model_id: str
    model_name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost: Decimal  # USD, já arredondado em seis casas decimais


def _round_cost(value: Decimal) -> Decimal:
    return value.quantize(SIX_DECIMALS, rounding=ROUND_HALF_UP)


def _lookup(table: dict, key: str, code: str, label: str):
    item = table.get(key)
    if item is None:
        valid = ", ".join(table)
        raise InvalidSimulationError(
            code, f"{label} '{key}' não existe no catálogo. Opções válidas: {valid}."
        )
    return item


def _estimate_for(model: ModelInfo, input_tokens: int, output_tokens: int) -> Estimate:
    input_cost = Decimal(input_tokens) / ONE_MILLION * model.input_price_per_million
    output_cost = Decimal(output_tokens) / ONE_MILLION * model.output_price_per_million
    return Estimate(
        model_id=model.id,
        model_name=model.name,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=input_tokens + output_tokens,
        cost=_round_cost(input_cost + output_cost),
    )


def estimate(model_id: str, task_type: str, response_size: str) -> Estimate:
    """Estima tokens e custo para uma combinação modelo + tarefa + tamanho."""
    model = _lookup(MODELS, model_id, "invalid_model", "Modelo")
    task = _lookup(TASK_TYPES, task_type, "invalid_task_type", "Tipo de tarefa")
    size = _lookup(RESPONSE_SIZES, response_size, "invalid_response_size", "Tamanho de resposta")
    return _estimate_for(model, task.input_tokens, size.output_tokens)


def compare_models(task_type: str, response_size: str) -> list[Estimate]:
    """Mesma tarefa e tamanho, variando apenas o modelo (ordem do catálogo)."""
    return [estimate(model_id, task_type, response_size) for model_id in MODELS]
