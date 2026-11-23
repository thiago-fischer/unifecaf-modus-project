"""Configurações centrais da aplicação.

Mantidas em um único lugar para que nome, versão e descrição não fiquem
espalhados pelo código. Quando surgirem variáveis de ambiente, este é o
ponto de extensão (por exemplo, migrando para pydantic-settings).
"""

import os

APP_NAME = "Modus API"
APP_DESCRIPTION = "API do simulador educativo de custo de interações com LLMs."
APP_VERSION = "0.1.0"

# Identificador do serviço retornado pelo endpoint de saúde.
SERVICE_NAME = "modus-api"

# Origens permitidas quando o frontend usa uma URL direta para a API.
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "MODUS_ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
    ).split(",")
    if origin.strip()
]
