# Backend do Modus

Backend inicial da aplicação Modus, construído com Python e FastAPI.

## Requisitos

- Python 3.12 ou versão compatível;
- `pip`;
- acesso ao terminal.

## Configuração local

No diretório `backend/`, crie e ative um ambiente virtual:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Execução

Ainda no diretório `backend/` e com o ambiente virtual ativo:

```bash
python -m uvicorn app.main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

## Verificação manual

Com a API em execução, acesse `http://127.0.0.1:8000/health`. A resposta esperada é:

```json
{
  "status": "ok",
  "service": "modus-api"
}
```

A documentação interativa gerada pelo FastAPI está disponível em `http://127.0.0.1:8000/docs`.

## Endpoints

| Método | Caminho | Descrição |
| --- | --- | --- |
| GET | `/health` | Verifica se a API está disponível. |
| GET | `/catalog` | Lista modelos, tipos de tarefa e tamanhos de resposta. |
| POST | `/simulations` | Calcula tokens e custo aproximado e compara os modelos. |

### Exemplo de simulação

```bash
curl -X POST http://127.0.0.1:8000/simulations \
  -H "Content-Type: application/json" \
  -d '{"modelId":"modus-equilibrado","taskType":"summary","responseSize":"medium"}'
```

Resposta (resumida):

```json
{
  "estimate": {
    "modelId": "modus-equilibrado",
    "modelName": "Modus Equilibrado",
    "inputTokens": 800,
    "outputTokens": 500,
    "totalTokens": 1300,
    "cost": 0.0069
  },
  "currency": "USD",
  "isEstimate": true,
  "comparison": [ "... um item por modelo, com o campo selected ..." ],
  "guidance": [ "..." ],
  "disclaimer": "..."
}
```

Escolhas inexistentes retornam `422` com `{"detail": {"code": "invalid_model", "message": "..."}}`.
Os códigos possíveis são `invalid_model`, `invalid_task_type` e `invalid_response_size`.

## Estrutura

```text
app/
  api/      rotas e schemas (camada HTTP)
  domain/   motor de estimativa (função pura, sem FastAPI)
  data/     catálogo estático com valores didáticos
tests/      testes automatizados
```

## Testes

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

Os testes reproduzem os exemplos calculados manualmente em
[`specs/06-regras-de-estimativa.md`](../specs/06-regras-de-estimativa.md).

## Escopo atual

Catálogo estático, motor de estimativa e endpoints de catálogo e simulação.
O frontend ainda não consome a API; essa integração fica para uma issue seguinte.
