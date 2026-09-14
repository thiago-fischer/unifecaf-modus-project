export type ModelOption = {
  name: string;
  task: string;
  inputTokens: number;
  outputTokens: number;
  estimatedCost: number;
  context: string;
};

export const modelOptions: ModelOption[] = [
  {
    name: "GPT-4o mini",
    task: "Resumo de texto",
    inputTokens: 1200,
    outputTokens: 450,
    estimatedCost: 0.08,
    context: "Bom equilíbrio entre custo e qualidade.",
  },
  {
    name: "Claude 3.5 Sonnet",
    task: "Criação de conteúdo",
    inputTokens: 1400,
    outputTokens: 600,
    estimatedCost: 0.11,
    context: "Mais robusto para redações e raciocínio.",
  },
  {
    name: "Gemini 1.5 Flash",
    task: "Busca orientada",
    inputTokens: 1000,
    outputTokens: 350,
    estimatedCost: 0.05,
    context: "Excelente custo para respostas rápidas.",
  },
];
