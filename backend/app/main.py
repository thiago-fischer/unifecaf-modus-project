from fastapi import FastAPI
from pydantic import BaseModel

import json
import os


class HealthResponse(BaseModel):
    status: str
    service: str


app = FastAPI(
    title="Modus API",
    description="API do simulador educativo de custo de interações com LLMs.",
    version="0.1.0",
)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    """Indica se a API está disponível para receber requisições."""
    return HealthResponse(status="ok", service="modus-api")


def carregar_catalogo():
    """
    Carrega o catálogo estático de modelos e valores de referência.
    Retorna uma lista de dicionários com os dados do catálogo.
    """
    # Obtém o diretório atual onde o main.py está localizado
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Monta o caminho completo para o arquivo catalogo.json
    caminho_arquivo = os.path.join(diretorio_atual, 'catalogo.json')
    
    try:
        # Abre e lê o arquivo JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            catalogo = json.load(arquivo)
            return catalogo
            
    except FileNotFoundError:
        print(f"Aviso: O arquivo {caminho_arquivo} não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: Falha ao ler o formato do arquivo JSON. Verifique a sintaxe.")
        return []

# Exemplo de uso (você pode integrar isso à rota da sua API depois)
if __name__ == "__main__":
    dados_catalogo = carregar_catalogo()
    print("Catálogo carregado com sucesso:")
    print(json.dumps(dados_catalogo, indent=2, ensure_ascii=False))