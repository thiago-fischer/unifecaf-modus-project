# Fluxo de colaboração

## 1. Issue é a unidade de trabalho

Toda demanda deve começar como uma issue. A issue precisa conter contexto, objetivo, critérios de aceite e eventuais dependências. Uma pessoa deve ser responsável pela execução; outras podem ser adicionadas como revisores ou colaboradores.

Antes de criar uma branch, confirme que a issue está clara e que não existe outra issue para o mesmo trabalho.

## 2. Convenção de branches

Use uma branch curta, descritiva e vinculada ao número da issue:

```text
feature/12-cadastro-usuario
fix/18-validacao-email
docs/7-atualiza-fluxo
chore/4-configura-repositorio
refactor/21-separa-servico
test/25-cobre-caso-limite
```

Tipos sugeridos:

- `feature`: nova funcionalidade;
- `fix`: correção de comportamento;
- `docs`: documentação;
- `chore`: manutenção ou configuração;
- `refactor`: reorganização sem mudança de comportamento;
- `test`: criação ou ajuste de testes.

Não faça desenvolvimento diretamente na `main`.

## 3. Commits

Faça commits pequenos, coesos e explicativos. Um commit deve representar uma mudança que possa ser entendida e revisada isoladamente.

Formato sugerido:

```text
#12 adiciona critérios de aceite da funcionalidade
```

Boas práticas:

- use verbos no presente e uma mensagem objetiva;
- evite misturar assuntos diferentes no mesmo commit;
- inclua o número da issue quando isso for possível;
- não inclua arquivos temporários, credenciais ou alterações sem relação com a issue.

## 4. Pull request

Ao concluir uma parte revisável do trabalho:

1. atualize a branch com a `main` quando necessário;
2. abra um pull request para `main`;
3. preencha o modelo do PR;
4. relacione a issue, usando `Closes #numero` quando o PR a concluir;
5. solicite pelo menos uma revisão;
6. responda aos comentários e atualize a branch;
7. faça o merge somente quando os critérios de aceite estiverem atendidos.

O título do PR deve indicar a issue e o resultado principal, por exemplo: `#12 Adiciona cadastro de usuário`.

## 5. Revisão

Quem revisa deve avaliar principalmente:

- atendimento dos critérios de aceite;
- clareza e tamanho da mudança;
- impactos em outras partes do projeto;
- qualidade da documentação e dos testes, quando aplicável;
- ausência de arquivos sensíveis ou alterações acidentais.

Comentários devem ser objetivos e respeitosos. Dúvidas, riscos e sugestões importantes precisam ficar registrados no PR para manter o histórico da decisão.

## 6. Merge

O merge é feito pelo GitHub ou pela plataforma adotada pelo grupo, após a aprovação. Recomenda-se usar **merge commit** durante a fase de aprendizagem para que a prática de integração entre branches fique visível no histórico.

Se houver conflito:

1. a pessoa responsável pela branch resolve o conflito;
2. os arquivos afetados são revisados com atenção;
3. os testes ou verificações disponíveis são executados novamente;
4. o PR é atualizado e passa por nova revisão, se o conflito alterar o comportamento.

Após o merge, a branch deve ser excluída na plataforma. A issue deve ser conferida e encerrada apenas quando todos os critérios estiverem atendidos.

## 7. Ordem resumida

```text
Issue -> Branch -> Commits -> Pull Request -> Revisão -> Ajustes -> Merge -> Fechamento da issue
```

## 8. Trabalho em paralelo

Quando uma tarefa depender de outra, registre a dependência na issue. Evite que duas branches alterem o mesmo trecho sem alinhamento prévio. Se o trabalho puder ser dividido, crie issues menores com critérios de aceite independentes.
