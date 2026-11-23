"""Catálogo estático do Modus.

Os valores seguem `specs/06-regras-de-estimativa.md` e são DIDÁTICOS:
não representam preços oficiais de nenhum provedor de LLM.
"""

from dataclasses import dataclass
from decimal import Decimal

CURRENCY = "USD"
CATALOG_UPDATED_AT = "2026-10-05"
CATALOG_DISCLAIMER = (
    "Valores didáticos e fictícios, usados apenas para comparação educativa. "
    "Não representam preços oficiais de nenhum provedor."
)


@dataclass(frozen=True)
class ModelInfo:
    id: str
    name: str
    input_price_per_million: Decimal  # USD por 1 milhão de tokens de entrada
    output_price_per_million: Decimal  # USD por 1 milhão de tokens de saída


@dataclass(frozen=True)
class TaskType:
    id: str
    name: str
    input_tokens: int


@dataclass(frozen=True)
class ResponseSize:
    id: str
    name: str
    output_tokens: int


MODELS: dict[str, ModelInfo] = {
    m.id: m
    for m in (
        ModelInfo("modus-economico", "Modus Econômico", Decimal("0.50"), Decimal("1.50")),
        ModelInfo("modus-equilibrado", "Modus Equilibrado", Decimal("3.00"), Decimal("9.00")),
        ModelInfo("modus-avancado", "Modus Avançado", Decimal("10.00"), Decimal("30.00")),
    )
}

TASK_TYPES: dict[str, TaskType] = {
    t.id: t
    for t in (
        TaskType("summary", "Resumo", 800),
        TaskType("explanation", "Explicação", 500),
        TaskType("text", "Texto", 350),
        TaskType("code", "Código", 700),
    )
}

RESPONSE_SIZES: dict[str, ResponseSize] = {
    s.id: s
    for s in (
        ResponseSize("small", "Pequena", 150),
        ResponseSize("medium", "Média", 500),
        ResponseSize("large", "Grande", 1000),
    )
}
