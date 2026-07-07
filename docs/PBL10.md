# Aula 15 – Modelos de Maturidade
# Entrega PBL – LocalEats

## 👥 Integrante

- Tiago Jesus Pereira

---

# 🔹 1. Diagnóstico de Maturidade

Abaixo está o diagnóstico do processo de desenvolvimento atual, considerando o contexto de um projeto realizado individualmente, mas que adotou práticas formais de QA (TDD e BDD).

| Critério | Sim | Parcial | Não |
|-----------|-----|----------|-----|
| Os requisitos são documentados? | X | | |
| Existe controle de mudanças? | | X | |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | X | |
| Existe padronização para implementação de funcionalidades? | X | | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | | X |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | X | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | X | | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | X | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X |

### Nível de maturidade estimado

**Nível 2: Gerenciado (CMMI)** ### Justificativa

O processo do LocalEats atingiu o nível **Gerenciado** porque o trabalho já não é reativo ou caótico. O uso de repositórios (GitHub), padronização de arquitetura (Page Object Model) e a obrigatoriedade de executar testes (Pytest) antes de qualquer entrega garantem que os requisitos (descritos em Gherkin) sejam atendidos. No entanto, o processo ainda não atinge o nível "Definido" ou "Quantitativamente Gerenciado" porque, por ser um projeto individual, carece de revisões por pares, gestão formal de defeitos (Issue Tracker) e medição estatística de qualidade (Métricas).

---

# 🔹 2. Lacunas Identificadas

Considerando o diagnóstico, os seguintes pontos representam gargalos que impedem a evolução da maturidade do processo:

| Lacuna | Impacto |
|---------|----------|
| **Ausência de métricas de cobertura de código** | Sem métricas numéricas, é impossível saber se os testes criados cobrem 50% ou 100% das regras de negócio do sistema. |
| **Falta de validação e revisão de código (Code Review)** | Como o trabalho é individual, vícios de programação e lógicas subotimizadas podem passar despercebidos sem um segundo olhar. |
| **Gestão informal de defeitos** | Os bugs encontrados durante o desenvolvimento são corrigidos imediatamente no ciclo Red-Green-Refactor, perdendo-se o histórico e a documentação das falhas. |

---

# 🔹 3. Propostas de Melhoria

Para elevar o processo para os próximos níveis de maturidade, as seguintes ações podem ser implementadas para suprir as lacunas listadas:

| Melhoria | Benefício |
|-----------|-----------|
| **Implementar o `pytest-cov` no projeto** | Gerar relatórios automatizados de cobertura de código, fornecendo a primeira **métrica quantitativa** de qualidade para o projeto. |
| **Integrar análise estática de código (ex: SonarQube / Flake8)** | Substituir a ausência de "revisão humana" por uma ferramenta que aponte code smells, falhas de segurança e anti-patterns no momento do commit. |
| **Adotar o GitHub Issues para controle de defeitos** | Criar um fluxo formal onde todo bug encontrado vira um ticket rastreável, garantindo controle de mudanças e registro histórico antes da correção. |

---

## 💡 Conclusão

O diagnóstico revelou que as práticas técnicas de qualidade (TDD, BDD, automação) introduzidas no LocalEats geraram uma base sólida e controlada. Contudo, a qualidade de processo exige olhar além do código. A implementação de ferramentas de medição (cobertura) e análise estática compensariam a falta de uma equipe maior, elevando o projeto individual a um patamar de maturidade profissional compatível com o nível "Definido".