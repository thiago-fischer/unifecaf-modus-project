# Modus

## O custo por trás da inteligência

O Modus será uma aplicação web educativa para tornar mais compreensível o custo estimado por trás de uma interação com uma ferramenta de Inteligência Artificial generativa.

## Sobre o projeto

Cada prompt envolve processamento, infraestrutura e uso de tokens, mas esse custo normalmente não é visível para quem utiliza uma LLM. O Modus pretende tornar essa relação mais clara para incentivar um uso consciente de IA.

O foco inicial é educativo: o Modus será uma ferramenta de estimativa e não uma calculadora exata de impacto ambiental ou dos custos internos de cada provedor.

## Escopo inicial

A proposta do primeiro incremento é permitir que a pessoa usuária simule uma geração escolhendo:

- a LLM desejada;
- o tipo de tarefa;
- o tamanho esperado da resposta.

Com base nisso, a aplicação deverá apresentar estimativas de tokens de entrada e saída, custo aproximado, comparação entre modelos e orientações sobre uso consciente. O escopo detalhado da primeira versão está registrado em [`specs/03-escopo-do-mvp.md`](specs/03-escopo-do-mvp.md).

## Limites conhecidos

O projeto não pretende calcular a pegada ambiental real de uma geração. Esse cálculo exigiria dados específicos sobre datacenters, matriz energética, hardware e infraestrutura de cada provedor.

Também não fazem parte desta etapa a integração com APIs reais de LLM, banco de dados, autenticação ou definição da stack tecnológica.

## Stack prevista

- Backend: Python + FastAPI.
- Frontend: React + TypeScript + Vite.
- Comunicação: API REST utilizando JSON.
- Dados iniciais: catálogo estático, sem banco de dados.

Consulte [`specs/04-stack-tecnologica.md`](specs/04-stack-tecnologica.md) para conhecer as responsabilidades e os limites dessa decisão.

## Estado do projeto

O projeto está em fase de planejamento colaborativo e ainda não possui código de aplicação. As decisões são acompanhadas pelas [issues do repositório](https://github.com/thiago-fischer/unifecaf-modus-project/issues).

## Documentação

- [Visão geral do projeto](specs/00-visao-geral.md)
- [Fluxo de colaboração](specs/01-fluxo-de-colaboracao.md)
- [Critérios de aceite e conclusão](specs/02-criterios-de-aceite-e-conclusao.md)
- [Índice das especificações](specs/README.md)
- [Arquitetura inicial](specs/05-arquitetura-inicial.md)
- [Regras de estimativa](specs/06-regras-de-estimativa.md)

## Próximos passos

1. [Configurar regras de proteção da branch `main`](https://github.com/thiago-fischer/unifecaf-modus-project/issues/9)
2. Transformar as funcionalidades do MVP em issues de implementação.
3. Fazer verificações manuais ou testes pontuais dentro de cada issue, conforme a necessidade.

## Como contribuir

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) para conhecer o fluxo de issues, branches, pull requests, revisões e merges. Toda alteração deve estar relacionada a uma issue e passar por pull request antes de chegar à `main`.

## Desenvolvimento local

O backend inicial está documentado em [`backend/README.md`](backend/README.md). O frontend será configurado em uma etapa posterior.

## Licença

Este projeto está licenciado sob a [licença MIT](LICENSE).
