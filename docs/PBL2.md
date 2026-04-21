# Diagnóstico de Qualidade – Startup Local Eats

**Disciplina:** Qualidade de Software
**Aula 3:** Papéis, Responsabilidades e Práticas de QA
**Integrante:** Tiago Jesus Pereira

---

## 1. Diagnóstico da Situação Atual

**1.1 Papéis atuais identificados**
Analisando o cenário de "funcionalidades chegando à produção com defeitos", é altamente provável que a startup conte apenas com o papel de **Desenvolvedor**. Talvez exista a figura de um **Fundador/Gerente** que solicita as demandas, mas sem formalização técnica. Não há indícios da existência de um Analista de QA, DevOps ou um Product Owner estruturado.

**1.2 Quem é responsável pela qualidade hoje?**
Atualmente, a qualidade não tem um responsável definido. Na prática, os próprios desenvolvedores estão testando o próprio código (o que gera viés e falhas) ou, pior ainda, os **próprios clientes e restaurantes** estão atuando como "testadores em produção" ao esbarrarem nos bugs.

**1.3 Problemas identificados**
* Inexistência de um fluxo de aprovação e testes antes do *deploy* em produção.
* Falta de rastreamento de bugs (não há onde registrar os pedidos duplicados formalmente).
* Testes viciados (o desenvolvedor testa apenas o "caminho feliz" da funcionalidade que ele mesmo criou).
* Ausência de critérios de aceite claros para definir quando uma funcionalidade está realmente "pronta".

**1.4 Impactos desses problemas**
* **Para os usuários (Clientes):** Frustração ao não conseguir finalizar pedidos, perda de confiança na plataforma e abandono do aplicativo.
* **Para os usuários (Restaurantes):** Prejuízo financeiro e logístico ao preparar pedidos duplicados, gerando desperdício de insumos e atrito com a plataforma.
* **Para o sistema/negócio:** Dano à reputação da Local Eats perante a associação de comerciantes locais, alto custo de retrabalho para os desenvolvedores (que precisam parar novas features para apagar incêndios) e risco de falência do projeto.

**1.5 A qualidade é responsabilidade de quem?**
A qualidade de software **deve ser uma responsabilidade compartilhada por toda a equipe**. Embora o Analista de QA seja o especialista em criar as estratégias, cenários e automações de testes, o desenvolvedor é responsável por entregar um código limpo e testado em nível de unidade, e o Analista de Requisitos/PO é responsável por garantir que as regras de negócio estejam claras. O QA não "injeta" qualidade no fim do processo; a equipe constrói a qualidade desde a concepção.

---

## 2. Papéis da Equipe Propostos

**2.1 Lista de papéis**
1. Desenvolvedor (Front-end/Back-end/Full-Stack)
2. Analista de Qualidade de Software (QA)
3. Analista de Requisitos / Product Owner (PO)
4. Analista de Infraestrutura / DevOps

**2.2 Descrição dos papéis**

* **Desenvolvedor**
  * **Responsabilidades principais:** Escrever o código-fonte, criar a arquitetura técnica, corrigir bugs reportados.
  * **Relação com a qualidade:** Garantir a qualidade técnica do código, realizar testes unitários e aplicar boas práticas de desenvolvimento estruturado.

* **Analista de Qualidade de Software (QA)**
  * **Responsabilidades principais:** Planejar cenários de teste, executar testes manuais/automatizados, registrar bugs.
  * **Relação com a qualidade:** É o guardião dos processos de teste. Valida se o software atende aos requisitos do cliente antes de ir para produção.

* **Analista de Requisitos / Product Owner (PO)**
  * **Responsabilidades principais:** Entender as necessidades dos clientes/restaurantes, escrever histórias de usuário e regras de negócio.
  * **Relação com a qualidade:** Garante a "Adequação Funcional" (construir o sistema certo). Evita que os desenvolvedores criem funcionalidades incorretas.

* **DevOps / Analista de Infraestrutura**
  * **Responsabilidades principais:** Cuidar dos servidores, banco de dados e esteiras de *deploy* (CI/CD).
  * **Relação com a qualidade:** Garante a "Confiabilidade e Desempenho". Cria ambientes separados (homologação e produção) para que os testes ocorram com segurança.

---

## 3. Práticas de QA Sugeridas

**3.1 Lista de práticas**
1. Criação de um Ambiente de Homologação (Staging)
2. Registro e Rastreamento de Bugs em ferramentas ágeis
3. Testes Exploratórios e de Regressão
4. Code Review (Revisão de Código) por pares

**3.2 Explicação das práticas**

* **Prática 1: Criação de um Ambiente de Homologação (Staging)**
    * **Descrição:** O DevOps/Infraestrutura deve criar uma réplica do ambiente de produção (um servidor de testes). Nenhuma funcionalidade nova vai para o cliente final sem antes passar por esse ambiente seguro, onde o QA poderá testar exaustivamente sem afetar os restaurantes reais.
* **Prática 2: Registro e Rastreamento de Bugs**
    * **Descrição:** Utilizar uma ferramenta (como Jira, Trello ou GitHub Issues) para que todo erro encontrado seja documentado com passos para reproduzir, evidências (prints) e severidade. Isso tira a resolução de bugs do "boca a boca" e cria métricas claras.
* **Prática 3: Code Review (Revisão de Código)**
    * **Descrição:** Antes de uma funcionalidade ser mesclada (*merged*) ao código principal, outro desenvolvedor da equipe deve revisar o código. Isso pega erros lógicos cedo e garante a padronização e qualidade da escrita do software.
* **Prática 4: Testes de Regressão**
    * **Descrição:** Sempre que uma nova funcionalidade for finalizada, o QA deve re-testar as funcionalidades antigas (como o carrinho de compras) para garantir que o código novo não quebrou o que já funcionava anteriormente (como evitar os pedidos duplicados).

---

## 4. Anúncios de Contratação

**4.1 Vaga 1 – Analista de Qualidade de Software (QA)**

* **Descrição da vaga:** A Local Eats busca um QA apaixonado por excelência para estruturar nossos processos de testes. Você será fundamental para garantir que moradores e turistas tenham uma experiência impecável ao fazer pedidos nos restaurantes locais, reduzindo nossos bugs em produção a zero.
* **Local:** Pelotas – RS (Híbrido)
* **Responsabilidades:**
    * Planejar, modelar e executar testes manuais em aplicações Web e Mobile.
    * Criar relatórios detalhados de bugs e atuar junto aos desenvolvedores para resolução.
    * Validar regras de negócio e realizar testes de regressão antes de cada lançamento.
    * Ajudar a disseminar a cultura de qualidade dentro da startup.
* **Requisitos obrigatórios:**
    * Experiência prática com testes manuais de software.
    * Capacidade analítica para investigar cenários complexos (ex: falhas em pagamentos e concorrência de pedidos).
    * Conhecimento em metodologias ágeis (Scrum/Kanban).
* **Requisitos desejáveis:**
    * Conhecimento em Postman para testes de API.
    * Noções de automação de testes (Cypress ou Selenium).
* **Certificações desejáveis:**
    * CTFL (Certified Tester Foundation Level) - ISTQB.

**4.2 Vaga 2 – Desenvolvedor Full-Stack (Foco em Qualidade)**

* **Descrição da vaga:** Procuramos um Desenvolvedor Full-Stack focado na criação de soluções robustas. Na Local Eats, você não vai apenas "entregar features", mas construir uma arquitetura escalável e resiliente que suporte os horários de pico dos restaurantes da nossa região.
* **Local:** Pelotas – RS (Híbrido)
* **Responsabilidades:**
    * Desenvolver e manter o aplicativo Mobile e a plataforma Web.
    * Escrever testes unitários para garantir a estabilidade das regras de negócio (evitando pedidos duplicados).
    * Participar ativamente das sessões de Code Review.
    * Colaborar com o QA para construir códigos altamente testáveis.
* **Requisitos obrigatórios:**
    * Sólida experiência com desenvolvimento Front-end (React) e Back-end (Node.js, Python ou similar).
    * Cultura de testes (conhecimento em Jest, PyTest ou similares para testes unitários).
    * Domínio de versionamento de código (Git/GitHub).
* **Requisitos desejáveis:**
    * Conhecimentos em infraestrutura, Docker e ferramentas de monitoramento.
    * Conhecimento de banco de dados relacionais e controle de concorrência.
* **Certificações desejáveis:**
    * Certificações AWS, Azure ou formações sólidas em desenvolvimento de sistemas.

---

## 5. Conclusão da Equipe

* **O que a equipe aprendeu com a atividade:** Aprendi que a qualidade de software vai muito além da codificação. Sem uma estrutura organizacional clara, definição de papéis e ambientes controlados, até mesmo os melhores códigos estão sujeitos a falhas críticas em produção.
* **Principais dificuldades encontradas:** Mapear a transição de um ambiente caótico para um estruturado sem engessar a agilidade que uma startup precisa.
* **Principais melhorias propostas para a startup:** A introdução do papel dedicado de QA, a implementação de um ambiente de homologação separado da produção e a adoção do rastreamento formal de bugs e code review, descentralizando a qualidade e tornando-a parte da cultura da empresa.

---

> **📌 Observações (opcional)**
> Acredito que a implementação destas práticas não apenas resolverá os problemas imediatos com os restaurantes, mas preparará a plataforma Local Eats para escalar e atender o grande evento gastronômico com estabilidade.