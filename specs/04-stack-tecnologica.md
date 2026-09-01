# Stack tecnológica

## Decisão

O Modus será desenvolvido com uma arquitetura web separada em frontend e backend:

- **Backend:** Python com FastAPI.
- **Servidor da API:** Uvicorn.
- **Frontend:** React com TypeScript.
- **Ferramenta de desenvolvimento do frontend:** Vite.
- **Comunicação:** API HTTP seguindo o estilo REST e utilizando JSON.
- **Persistência inicial:** não haverá banco de dados; o catálogo de modelos e os valores de referência serão estáticos.
- **Integrações externas:** não haverá integração com APIs reais de LLM no MVP.

## Responsabilidades das camadas

### Backend

O backend será responsável por:

- expor os dados e as operações necessárias para a simulação;
- validar os dados recebidos;
- centralizar as regras de estimativa e cálculo;
- fornecer documentação OpenAPI gerada pelo FastAPI;
- manter o catálogo estático de modelos, quando essa responsabilidade não ficar no frontend.

### Frontend

O frontend será responsável por:

- apresentar o fluxo de seleção do MVP;
- enviar as escolhas da pessoa usuária para a API;
- exibir tokens, custo, comparação e orientações educativas;
- informar claramente que os resultados são estimativas;
- lidar com estados de carregamento, erro e validação.

## Ferramentas de ambiente

- Python 3.12 ou versão compatível definida pelo grupo;
- Node.js em versão LTS;
- `pip` e ambiente virtual para dependências Python;
- `npm` para dependências do frontend;
- Git para versionamento.

As versões exatas das dependências devem ser fixadas nos arquivos de configuração de cada camada quando a implementação começar.

## Motivos da escolha

- FastAPI oferece validação de dados, documentação da API e uma base simples para um backend REST.
- React facilita a divisão da interface em componentes e a evolução do fluxo de simulação.
- TypeScript adiciona verificação estática e ajuda a reduzir inconsistências entre os dados da interface e da API.
- Vite fornece um ciclo de desenvolvimento rápido para o frontend.
- A separação entre frontend e backend permite que o grupo divida o trabalho em branches e issues com responsabilidades claras.
- A ausência de banco e de APIs externas mantém o MVP pequeno e reduz dependências durante a aprendizagem.

## Alternativas consideradas

- **Frontend sem framework:** seria mais simples no início, mas ofereceria menos estrutura para o fluxo composto por seleção, resultado e comparação.
- **Next.js:** poderia unificar parte da aplicação, mas não é necessário enquanto o backend FastAPI for uma decisão do projeto.
- **Flask:** é uma alternativa válida em Python, porém o grupo priorizou os recursos integrados de validação e documentação do FastAPI.

## Limites desta decisão

Esta especificação define as tecnologias principais, mas não define ainda:

- endpoints e contratos detalhados da API;
- estrutura final de diretórios;
- biblioteca de componentes ou estratégia visual;
- regras matemáticas completas da estimativa;
- ferramenta definitiva de testes;
- processo de deploy.

Esses pontos serão definidos nas especificações de arquitetura, testes e implementação.

## Critérios de aceite

- [ ] O grupo reconhece Python + FastAPI como stack do backend.
- [ ] O grupo reconhece React + TypeScript + Vite como stack do frontend.
- [ ] A comunicação entre as camadas está definida como REST/JSON.
- [ ] Está registrado que o MVP não terá banco de dados nem integração com APIs reais de LLM.
- [ ] As responsabilidades do frontend e do backend estão separadas.
- [ ] Os detalhes que ainda não foram decididos estão explicitamente listados.
