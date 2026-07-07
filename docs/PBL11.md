# Aula 16 – Qualidade em Metodologias Ágeis
# Entrega PBL – LocalEats

## 👥 Integrante

- Tiago Jesus Pereira

---

# 🔹 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|----------|----------|----------|----------|
| **Planejamento iterativo** | Sim | As entregas são planejadas e executadas em ciclos curtos guiados pelas atividades (PBLs).  | Sim, formalizando o escopo de cada iteração antes de abrir o editor de código.  |
| **Priorização de funcionalidades** | Sim | A priorização segue a ordem de complexidade e os requisitos das entregas solicitadas.  | Sim, criando um backlog pessoal no GitHub Projects para visualizar a ordem de ataque.  |
| **Entregas incrementais** | Sim | A cada nova atividade, o LocalEats recebe uma nova camada (testes unitários, E2E, BDD) agregando valor contínuo.  | Fazer commits ainda menores para cada etapa do desenvolvimento.  |
| **Feedback frequente** | Parcial | Como o trabalho é individual, não há feedback de outros devs, mas há feedback rápido dos testes automatizados (TDD).  | Sim, implementando ferramentas de linting ou CI/CD para feedback estático de código.  |
| **Trabalho colaborativo** | Não | O desenvolvimento e a garantia da qualidade estão centralizados em uma única pessoa.  | Sim, utilizando inteligência artificial (como Copilot) para simular *Pair Programming* e revisões.  |
| **Controle visual das atividades** | Não | O controle atual é feito mentalmente ou verificando o histórico de commits no repositório.  | Sim, adotando um quadro Kanban simples para mapear o status das tarefas.  |
| **Melhoria contínua** | Sim | Refatorações constantes no código após os testes passarem (fase Refactor) e reflexões ao final de cada PBL.  | Sim, documentando os gargalos encontrados para evitar repetição nos próximos módulos.  |

### Conclusão

O processo atual já possui uma forte herança do *Extreme Programming (XP)* devido ao uso massivo de automação de testes, TDD e BDD. O principal ponto forte é o feedback técnico imediato fornecido pelas suítes de teste, o que garante a confiabilidade das entregas incrementais. Por outro lado, a maior oportunidade de melhoria é adotar ferramentas visuais de gestão e estabelecer critérios estritos de início e fim de tarefa, compensando a ausência de um Scrum Master ou de uma equipe para manter a cadência e a organização estrutural do projeto[cite: 886].

---

# 🔹 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|------------------|------------------------|--------------------|
| Criar um quadro visual (GitHub Projects) para as tarefas.  | Kanban  | Maior visibilidade do andamento das atividades, limitando o trabalho em progresso (WIP) e reduzindo a carga mental.  |
| Integrar o desenvolvimento com commits pequenos e contínuos.  | XP (Extreme Programming - Continuous Integration)  | Facilita a rastreabilidade, isolamento de bugs e torna a reversão de código muito mais simples caso um teste quebre.  |
| Focar apenas no código estritamente necessário para o teste passar (YAGNI).  | Lean Software Development  | Reduzir o desperdício de tempo com *overengineering* (desenvolver lógicas complexas que não foram solicitadas pelo requisito).  |
| Registrar um "Log Diário" das atividades ao iniciar e terminar de programar.  | Scrum (Daily Standup adaptada)  | Manter o alinhamento e o foco nas metas do dia, identificando impedimentos técnicos de forma rápida, mesmo trabalhando de forma solitária.  |

---

# 🔹 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para entrar em desenvolvimento quando:

1. O requisito e o comportamento esperado da funcionalidade estiverem claros e sem ambiguidades. 
2. Os critérios de aceitação da funcionalidade estiverem explicitamente definidos. 
3. O cenário de teste (seja unitário ou BDD em linguagem Gherkin) já tiver sido rascunhado. 
4. Quaisquer dependências técnicas (bibliotecas externas, senhas, URLs da Vercel) estiverem mapeadas e acessíveis. 
5. A tarefa estiver devidamente registrada e priorizada na coluna "To Do" do Kanban do projeto. 

---

# 🔹 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

1. O código-fonte tiver sido completamente implementado sem erros de sintaxe ou warnings críticos. 
2. Todos os critérios de aceitação estipulados no requisito da funcionalidade tiverem sido atendidos. 
3. Todos os testes automatizados (unitários e/ou funcionais E2E no Playwright) passarem com sucesso (Green). 
4. O código tiver passado pela etapa de refatoração (remoção de código duplicado, variáveis legíveis, limpeza de comentários inúteis). 
5. O código finalizado for "commitado" com uma mensagem descritiva (ex: Conventional Commits) e enviado (Push) para a branch principal do repositório no GitHub. 