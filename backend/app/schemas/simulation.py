from pydantic import BaseModel, Field


class SimulationRequest(BaseModel):
    modelId: str = Field(..., examples=["modus-equilibrado"])
    taskType: str = Field(..., examples=["summary"])
    responseSize: str = Field(..., examples=["medium"])


class ModelEstimate(BaseModel):
    modelId: str
    modelName: str
    inputTokens: int
    outputTokens: int
    totalTokens: int
    cost: float = Field(..., description="Custo aproximado em USD (6 casas decimais).")


class ComparisonItem(ModelEstimate):
    selected: bool


class SimulationResponse(BaseModel):
    estimate: ModelEstimate
    currency: str
    isEstimate: bool = True
    comparison: list[ComparisonItem]
    guidance: list[str]
    disclaimer: str


class ErrorBody(BaseModel):
    code: str
    message: str


class CatalogOption(BaseModel):
    id: str
    name: str


class CatalogModel(CatalogOption):
    inputPricePerMillion: float
    outputPricePerMillion: float


class CatalogResponse(BaseModel):
    models: list[CatalogModel]
    taskTypes: list[CatalogOption]
    responseSizes: list[CatalogOption]
    currency: str
    updatedAt: str
    disclaimer: str
