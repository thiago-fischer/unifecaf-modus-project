# Critérios de aceite e conclusão

## Critérios de aceite

Cada issue deve descrever condições observáveis para que o trabalho seja aceito. Prefira frases verificáveis:

```text
- [ ] Dado um usuário válido, o sistema permite concluir o cadastro.
- [ ] Dado um e-mail já cadastrado, o sistema informa o problema.
- [ ] A documentação de uso foi atualizada.
```

Evite critérios vagos como “fazer funcionar” ou “melhorar a tela”. Se a demanda não puder ser validada, ela ainda precisa ser refinada.

## Definition of Done

Uma issue pode ser considerada concluída quando:

- [ ] todos os critérios de aceite foram atendidos;
- [ ] a solução está na branch da issue e foi revisada em um pull request;
- [ ] verificações e testes aplicáveis foram executados;
- [ ] a documentação afetada foi atualizada;
- [ ] não há comentários de revisão pendentes;
- [ ] o pull request foi integrado à `main`;
- [ ] a issue foi fechada com referência ao pull request.

Para uma issue exclusivamente documental, marque como não aplicáveis os itens de testes de software e registre essa justificativa no PR.

## Quando não concluir uma issue

Se o escopo crescer, divida o trabalho em novas issues. Se a solução não estiver pronta para merge, mantenha o PR aberto ou converta-o em rascunho. Não feche uma issue apenas para retirar uma pendência da lista.
