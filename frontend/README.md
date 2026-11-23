# Frontend do Modus

Interface React e TypeScript do simulador educativo. O catálogo, os tokens, o custo e a comparação vêm da API FastAPI.

## Executar

Inicie o backend na porta 8000 conforme o [README principal](../README.md). Em outro terminal, neste diretório:

```powershell
npm ci
npm run dev
```

Abra `http://localhost:5173`. O Vite encaminha as chamadas `/api` para `http://127.0.0.1:8000` durante o desenvolvimento.

## Configuração

Por padrão o frontend chama `/api`. Se a API estiver em outra origem, defina `VITE_API_BASE_URL` antes de compilar, por exemplo `VITE_API_BASE_URL=https://api.exemplo.com`. Nesse caso, inclua a origem do frontend em `MODUS_ALLOWED_ORIGINS` no backend. Em produção, o proxy de desenvolvimento do Vite não é usado: configure um proxy `/api` no servidor web ou forneça essa variável.

## Verificação

```powershell
npm run build
npm run lint
```

A simulação requer o backend em execução. Se o catálogo não puder ser carregado, a interface mostra o erro e permite tentar novamente.
