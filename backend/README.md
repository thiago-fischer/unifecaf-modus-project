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

## Escopo atual

Esta etapa cria somente a aplicação base e o endpoint de saúde. O catálogo, as regras de estimativa e o endpoint de simulação serão adicionados nas issues seguintes.
