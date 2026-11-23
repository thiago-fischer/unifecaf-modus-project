"""Agrega todas as rotas da API em um único roteador.

Para adicionar um novo domínio (ex.: simulação), crie o módulo em
`app/api/routes/` e registre-o aqui.
"""

from fastapi import APIRouter

from app.api.routes import health

api_router = APIRouter()
api_router.include_router(health.router)
