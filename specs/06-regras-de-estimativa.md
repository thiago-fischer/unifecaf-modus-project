# Regras de estimativa de tokens e custo

## Objetivo

Definir uma regra determinística e educativa para estimar tokens e custo a partir de três escolhas: modelo, tipo de tarefa e tamanho esperado da resposta.

Os valores desta especificação são didáticos e genéricos. Eles não representam preços oficiais de OpenAI, Google, Anthropic ou qualquer outro provedor.

## Entradas da simulação

Toda simulação deve receber:

- `modelId`: identificador de um modelo do catálogo;
- `taskType`: identificador do tipo de tarefa;
- `responseSize`: identificador do tamanho esperado da resposta.

O MVP não recebe um prompt real. Portanto, os tokens de entrada são estimados a partir do tipo de tarefa, e não por uma contagem textual.

## Tipos de tarefa

| ID | Nome | Tokens de entrada estimados |
| --- | --- | ---: |
| `summary` | Resumo | 800 |
| `explanation` | Explicação | 500 |
| `text` | Texto | 350 |
| `code` | Código | 700 |

Os valores representam o tamanho médio didático do contexto necessário para cada cenário.

## Tamanhos de resposta

| ID | Nome | Tokens de saída estimados |
| --- | --- | ---: |
| `small` | Pequena | 150 |
| `medium` | Média | 500 |
| `large` | Grande | 1.000 |

## Modelos genéricos do catálogo

| ID | Nome de exibição | Entrada (USD por 1 milhão) | Saída (USD por 1 milhão) |
| --- | --- | ---: | ---: |
| `modus-economico` | Modus Econômico | 0,50 | 1,50 |
| `modus-equilibrado` | Modus Equilibrado | 3,00 | 9,00 |
| `modus-avancado` | Modus Avançado | 10,00 | 30,00 |

Os nomes e valores são perfis fictícios para comparação. O catálogo deve informar que os preços são referências didáticas e registrar a data da última atualização.

## Cálculo dos tokens

Para uma simulação válida:

```text
tokensEntrada = tokens definidos pelo taskType
tokensSaida = tokens definidos pelo responseSize
tokensTotal = tokensEntrada + tokensSaida
```

Não são adicionados tokens ocultos de sistema, ferramentas, histórico ou formatação.

## Cálculo do custo

Os preços do modelo são expressos em USD por 1 milhão de tokens:

```text
custoEntrada = tokensEntrada / 1000000 * precoEntrada
custoSaida = tokensSaida / 1000000 * precoSaida
custoTotal = custoEntrada + custoSaida
```

O custo deve ser calculado com precisão suficiente internamente e apresentado em USD com seis casas decimais. Não haverá conversão para reais no MVP.

## Exemplos de cálculo

### Exemplo 1: resumo pequeno no Modus Econômico

```text
tokensEntrada = 800
tokensSaida = 150
custo = (800 / 1000000 * 0.50) + (150 / 1000000 * 1.50)
custo = 0.000625 USD
```

### Exemplo 2: explicação média no Modus Equilibrado

```text
tokensEntrada = 500
tokensSaida = 500
custo = (500 / 1000000 * 3.00) + (500 / 1000000 * 9.00)
custo = 0.006000 USD
```

### Exemplo 3: código grande no Modus Avançado

```text
tokensEntrada = 700
tokensSaida = 1.000
custo = (700 / 1000000 * 10.00) + (1000 / 1000000 * 30.00)
custo = 0.037000 USD
```

## Comparação entre modelos

A comparação deve manter `taskType` e `responseSize` iguais e variar apenas o `modelId`. Para `summary` + `medium`, por exemplo:

| Modelo | Tokens totais | Custo aproximado |
| --- | ---: | ---: |
| Modus Econômico | 1.300 | 0,001150 USD |
| Modus Equilibrado | 1.300 | 0,006900 USD |
| Modus Avançado | 1.300 | 0,023000 USD |

A comparação deve apresentar custo, não uma recomendação absoluta de modelo. O modelo mais caro pode ser adequado a uma tarefa mais complexa, mas essa avaliação está fora do cálculo do MVP.

## Validações

Uma simulação não deve ser calculada quando:

- o modelo não existe no catálogo;
- o tipo de tarefa não é reconhecido;
- o tamanho da resposta não é reconhecido;
- faltam preços ou tokens para uma entrada válida;
- algum valor numérico é negativo ou inválido.

Nesses casos, a API deve devolver um erro compreensível e não um custo parcial.

## Limitações

- os tokens são aproximações fixas por cenário;
- os preços são fictícios e estáticos;
- a moeda é USD;
- não há contagem de um prompt real;
- não há custo de ferramentas, cache, contexto ou infraestrutura;
- não há estimativa de energia ou pegada ambiental;
- o valor não representa necessariamente uma cobrança de provedor.

## Critérios de aceite

- [ ] As categorias de tarefa estão definidas.
- [ ] Os tamanhos de resposta e tokens estimados estão definidos.
- [ ] Os modelos, preços e moeda estão definidos.
- [ ] A fórmula e o arredondamento estão definidos.
- [ ] Existem pelo menos três cenários calculados manualmente.
- [ ] As limitações da estimativa estão registradas.
