export type CatalogOption = { id: string; name: string };

export type CatalogModel = CatalogOption & {
  inputPricePerMillion: number;
  outputPricePerMillion: number;
};

export type Catalog = {
  models: CatalogModel[];
  taskTypes: CatalogOption[];
  responseSizes: CatalogOption[];
  currency: string;
  updatedAt: string;
  disclaimer: string;
};

export type SimulationChoices = {
  modelId: string;
  taskType: string;
  responseSize: string;
};

export type Estimate = {
  modelId: string;
  modelName: string;
  inputTokens: number;
  outputTokens: number;
  totalTokens: number;
  cost: number;
};

export type Simulation = {
  estimate: Estimate;
  currency: string;
  isEstimate: boolean;
  comparison: (Estimate & { selected: boolean })[];
  guidance: string[];
  disclaimer: string;
};

const baseUrl = (import.meta.env.VITE_API_BASE_URL || "/api").replace(/\/$/, "");

async function readResponse<T>(response: Response): Promise<T> {
  if (response.ok) return (await response.json()) as T;

  const body = await response.json().catch(() => null);
  const message = body?.detail?.message;
  throw new Error(
    typeof message === "string"
      ? message
      : `Não foi possível concluir a solicitação (${response.status}).`,
  );
}

export async function getCatalog(signal?: AbortSignal): Promise<Catalog> {
  const response = await fetch(`${baseUrl}/catalog`, { signal });
  return readResponse<Catalog>(response);
}

export async function createSimulation(
  choices: SimulationChoices,
): Promise<Simulation> {
  const response = await fetch(`${baseUrl}/simulations`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(choices),
  });
  return readResponse<Simulation>(response);
}
