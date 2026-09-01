# Escopo do MVP

## Objetivo

Validar a proposta central do Modus: permitir que uma pessoa compreenda, por meio de uma simulação simples, como o modelo escolhido, o tipo de tarefa e o tamanho da resposta influenciam a quantidade estimada de tokens e o custo aproximado de uma geração.

O MVP deve ser educativo, rápido de utilizar e pequeno o suficiente para ser desenvolvido e revisado pelo grupo em um primeiro ciclo.

## Usuário principal

Uma pessoa que utiliza ou deseja utilizar ferramentas de IA generativa e quer compreender melhor o custo aproximado de uma interação, sem precisar conhecer detalhes técnicos de tokens ou da infraestrutura dos provedores.

## Fluxo principal

1. A pessoa escolhe uma LLM disponível no catálogo do Modus.
2. Escolhe o tipo de tarefa.
3. Escolhe o tamanho esperado da resposta.
4. Solicita a simulação.
5. Consulta a estimativa de tokens de entrada, tokens de saída e custo aproximado.
6. Opcionalmente, consulta a comparação entre os modelos disponíveis.
7. Lê uma orientação curta sobre uso consciente de IA.

O fluxo não exige login, envio de uma chave de API ou persistência de dados.

## Funcionalidades obrigatórias

### 1. Seleção de modelo

O usuário deve conseguir escolher uma LLM a partir de um catálogo estático mantido pelo projeto. Cada opção deve ter as informações necessárias para a estimativa, como identificação do modelo e seus valores de referência.

### 2. Seleção do tipo de tarefa

O usuário deve escolher uma categoria predefinida de tarefa. A categoria será usada para representar uma quantidade estimada de tokens de entrada compatível com o cenário escolhido.

### 3. Seleção do tamanho da resposta

O usuário deve escolher um tamanho predefinido de resposta, como pequeno, médio ou grande. Essa escolha será usada para representar uma quantidade estimada de tokens de saída.

### 4. Estimativa de tokens

Após a simulação, o sistema deve apresentar separadamente:

- tokens de entrada estimados;
- tokens de saída estimados;
- total estimado de tokens.

Os valores são aproximações baseadas nas opções escolhidas e não representam a contagem real de um prompt enviado a um provedor.

### 5. Estimativa de custo

O sistema deve calcular e apresentar o custo aproximado da geração com base nos tokens estimados e nos valores de referência do modelo selecionado.

O resultado deve deixar claro que se trata de uma estimativa. Valores, moeda e regra matemática detalhada serão definidos em uma especificação posterior, antes da implementação da calculadora.

### 6. Comparação entre modelos

O usuário deve conseguir comparar o custo estimado da mesma simulação entre os modelos disponíveis no catálogo. A comparação deve permitir identificar diferenças de custo sem sugerir que o modelo mais barato é sempre o mais adequado.

### 7. Orientação educativa

O resultado deve apresentar uma explicação curta sobre como prompts mais claros, respostas adequadas ao objetivo e escolha proporcional do modelo podem contribuir para um uso mais consciente de IA.

## Fora do escopo do MVP

- integração com APIs reais de LLM;
- envio de prompts reais para provedores;
- cálculo da quantidade real de tokens de um texto;
- cálculo exato da pegada ambiental ou do consumo de energia;
- garantia de que a estimativa representa a cobrança final de um provedor;
- login, autenticação ou perfis de usuário;
- banco de dados e histórico de simulações;
- criação ou treinamento de modelos de IA;
- painel administrativo para atualização do catálogo;
- sistema de pagamentos;
- aplicativo nativo para celular;
- internacionalização;
- definição de layout final ou identidade visual completa.

## Premissas do MVP

- o catálogo de modelos e os valores de referência serão mantidos de forma estática;
- a simulação será determinística para as mesmas escolhas;
- todas as escolhas obrigatórias terão valores padrão ou validação clara;
- nenhuma chave, dado pessoal ou prompt real será solicitado;
- a interface explicará as limitações das estimativas;
- o MVP poderá ser executado localmente após a definição da stack.

## Critérios de aceite do escopo

- [ ] O grupo reconhece o fluxo principal descrito nesta especificação.
- [ ] As funcionalidades obrigatórias estão separadas das funcionalidades futuras.
- [ ] O MVP não depende de API externa, login ou banco de dados.
- [ ] A proposta de estimativa educativa está claramente diferenciada de um cálculo exato.
- [ ] Cada funcionalidade obrigatória pode ser transformada em uma issue de implementação.
- [ ] As decisões de stack e arquitetura estão documentadas; as regras matemáticas detalhadas permanecem nas issues de implementação.

## Decisões relacionadas

- [Issue #5: escolher stack tecnológica](https://github.com/thiago-fischer/unifecaf-modus-project/issues/5)
- [Issue #6: definir arquitetura inicial](https://github.com/thiago-fischer/unifecaf-modus-project/issues/6)

Não haverá uma issue separada para estratégia de testes neste mini projeto. Cada issue de implementação deverá registrar as verificações aplicáveis ao seu escopo.
