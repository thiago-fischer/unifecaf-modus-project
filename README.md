# Modus

## O custo por trás da inteligência

O Modus é uma aplicação web educativa para tornar visível o custo estimado de uma interação com IA generativa. O objetivo é ajudar pessoas a compreender como a escolha do modelo, o tipo de tarefa e o tamanho da resposta afetam os tokens e o custo aproximado.

O MVP permite selecionar essas três opções, simular a geração, consultar tokens de entrada, saída e total, comparar modelos e ler orientações de uso consciente. A interface consulta a API; as regras de cálculo ficam no backend. Veja o [escopo detalhado](specs/03-escopo-do-mvp.md).

Os modelos e preços são fictícios e didáticos. Os valores em USD não representam uma cobrança real, contagem de um prompt ou impacto ambiental. O projeto não envia prompts para provedores, nem usa login ou banco de dados.

## Boas práticas para uso consciente de IA

- Escreva prompts claros e objetivos, com o contexto necessário desde o início.
- Evite repetir uma solicitação inteira quando apenas uma pequena correção é necessária.
- Peça respostas do tamanho adequado à tarefa.
- Revise e reaproveite informações já geradas.
- Use a IA como apoio, mantendo uma análise crítica das respostas.

## Stack

- Backend: Python, FastAPI e catálogo estático.
- Frontend: React, TypeScript e Vite.
- Comunicação: API REST com JSON.

As decisões e regras estão em [arquitetura inicial](specs/05-arquitetura-inicial.md) e [regras de estimativa](specs/06-regras-de-estimativa.md).

## Desenvolvimento local

Use dois terminais a partir da raiz do repositório. No primeiro:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

No segundo:

```powershell
cd frontend
npm ci
npm run dev
```

Abra `http://localhost:5173`. O Vite encaminha `/api` para a API em `http://127.0.0.1:8000`. A documentação interativa da API fica em `http://127.0.0.1:8000/docs`.

Para verificar o projeto:

```powershell
# em backend/
.\.venv\Scripts\python.exe -m pytest

# em frontend/
npm run build
npm run lint
```

Detalhes estão em [`backend/README.md`](backend/README.md) e [`frontend/README.md`](frontend/README.md).

## Contribuição e licença

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) para o fluxo de issues e pull requests. Licença [MIT](LICENSE).
