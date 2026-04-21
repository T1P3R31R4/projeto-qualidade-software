# Aula 6 – Planejamento e Execução de Testes

**Disciplina:** Qualidade de Software
**Projeto:** LocalEats
**Aluno:** Tiago Jesus Pereira (Trabalho Individual)

---

## 1. Plano de Testes

**1.1 Objetivo**
Estruturar e executar uma validação prática das funções centrais do sistema LocalEats (Busca, Login e Pedidos). O objetivo é sair do teste exploratório aleatório (onde apenas "clicamos para ver se funciona") e aplicar uma abordagem metódica para identificar, reproduzir e documentar as falhas que estão impactando a experiência de clientes e restaurantes.

**1.2 Escopo**
* **O que será testado:** * Fluxo de autenticação de usuários (Login).
    * Mecanismo de busca de restaurantes por texto livre e filtros de categoria.
    * Visualização do histórico de transações/pedidos.
* **O que NÃO será testado:** * Integração com gateways de pagamento.
    * Disparo de e-mails reais de recuperação de senha.
    * Responsividade da interface em diferentes tamanhos de tela mobile (o foco atual é funcionalidade de negócio).

**1.3 Funcionalidades selecionadas**
* [Login/Cadastro]
* [Busca de restaurantes e Filtros]
* [Histórico de Pedidos]

**1.4 Estratégia de Testes**
* **Tipos de teste:** (X) Funcional
* **Abordagem:** Testes manuais de Caixa-Preta. Utilizarei casos de teste pré-definidos baseados em cenários de sucesso (Happy Path) e cenários de exceção/erro (Sad Path), escritos utilizando a estrutura BDD/Gherkin (Dado, Quando, Então) para maior clareza dos passos.

**1.5 Responsáveis**
* **Tiago Jesus Pereira:** Responsável exclusivo pelo planejamento dos cenários, execução real na plataforma web fornecida, coleta de evidências e análise crítica dos resultados.

---

## 2. Casos de Teste

**CT-01 – Login com credenciais válidas (Cenário de Sucesso)**
* **Pré-condição:** O usuário deve possuir um cadastro ativo no banco de dados.
* **Passos:**
    1. Dado que estou na página inicial do LocalEats.
    2. E clico na aba "Entrar" do formulário.
    3. Quando eu preencho o e-mail "tiagojesusp@homtmail.com" e uma senha válida.
    4. E clico no botão rosa "Entrar".
* **Resultado esperado:** Então o sistema autentica o usuário, redireciona para a tela principal (Explorar) e exibe o avatar com a saudação "Olá, Tiago" no menu superior direito.

**CT-02 – Login com senha incorreta (Cenário de Erro)**
* **Pré-condição:** O usuário possui cadastro, mas não lembra a senha.
* **Passos:**
    1. Dado que estou na página de login.
    2. Quando eu preencho o e-mail "tiagojesusp@homtmail.com", mas insiro uma senha errada.
    3. E clico no botão rosa "Entrar".
* **Resultado esperado:** Então o sistema não deve autenticar o usuário e deve exibir uma mensagem clara em português (ex: "E-mail ou senha incorretos") em um quadro vermelho, mantendo o usuário na mesma tela.

**CT-03 – Busca por termo exato com resultados (Cenário de Sucesso)**
* **Pré-condição:** O banco de dados deve conter restaurantes com o termo "Pizza" cadastrados.
* **Passos:**
    1. Dado que estou na página de busca do LocalEats.
    2. Quando eu digito "Pizza" na barra de pesquisa.
    3. E aperto a tecla Enter ou clico na lupa.
* **Resultado esperado:** Então o sistema carrega e exibe uma lista apenas com restaurantes que contenham "Pizza" no nome ou na categoria.

**CT-04 – Filtro rápido por Categoria (Cenário de Sucesso)**
* **Pré-condição:** Estar logado na página principal (Explorar) com restaurantes de diversas categorias disponíveis.
* **Passos:**
    1. Dado que estou na tela "Explorar".
    2. Quando eu clico no botão (chip) da categoria "Italiana".
    3. E aguardo o recarregamento automático da lista (sem necessidade de clicar em "Buscar").
* **Resultado esperado:** Então a interface deve atualizar automaticamente e exibir apenas os cards dos restaurantes que pertencem à categoria "Italiana" (ex: Restaurante Sabor 0, Sabor 3).

**CT-05 – Visualização do Histórico de Transações / Pedidos (Cenário de Erro/Falha de Usabilidade)**
* **Pré-condição:** O usuário deve estar logado e possuir pelo menos um pedido realizado no sistema.
* **Passos:**
    1. Dado que estou logado no LocalEats.
    2. Quando eu clico no menu superior "Meus Pedidos".
    3. E visualizo o card de um pedido recente (ex: Pedido #46).
* **Resultado esperado:** Então o sistema deve exibir os detalhes amigáveis do pedido, mostrando claramente o Nome do Restaurante, o Nome do Produto/Prato escolhido, o valor total e um status traduzido. O card também deveria ser clicável para ver os detalhes da entrega.

---

## 3. Execução dos Testes

Abaixo estão os resultados registrados após a execução real no ambiente web fornecido (https://local-eats-unisenac.vercel.app/):

* **CT-01 (Login válido):** * **Resultado:** Passou. 
    * **Evidência:** O redirecionamento ocorreu normalmente e o sistema exibiu a saudação "Olá, Tiago".
* **CT-02 (Login inválido):** * **Resultado:** Falhou. 
    * **Evidência:** Bug de internacionalização. O sistema impediu o login, mas exibiu a mensagem de erro "Invalid credentials" em inglês.
* **CT-03 (Busca por texto):** * **Resultado:** Falhou. 
    * **Evidência:** A barra de pesquisa retorna "Nenhum restaurante encontrado" para qualquer input, indicando que a API de texto está inoperante.
* **CT-04 (Filtro por categoria):** * **Resultado:** Passou. 
    * **Evidência:** Ao clicar no botão "Italiana", o sistema filtrou corretamente a lista de forma automática, sem necessidade de usar o botão "Buscar".
* **CT-05 (Detalhes do Pedido):** * **Resultado:** Falhou. 
    * **Evidência:** A tela de "Meus Pedidos" exibe dados crus do banco de dados (Ex: "Restaurante ID: 8" e "1x Item Id #26") em vez dos nomes reais. Além disso, o status está em inglês ("PENDING") e o card não permite clique.

---

## 4. Análise dos Resultados

* **Quantidade de testes executados:** 5
* **Quantidade de testes que passaram:** 2
* **Quantidade de testes que falharam:** 3

**Principais problemas encontrados:**
1.  **Exposição de Dados Técnicos (Falta de Relacionamento de Banco):** A tela de pedidos exibe "IDs" (identificadores numéricos internos) ao invés do nome do restaurante e do prato, demonstrando falhas na integração Front-end x Back-end.
2.  **Módulo de Busca Inoperante:** A busca por digitação de texto está inativa, limitando o usuário a usar apenas os cliques nas categorias pré-definidas.
3.  **Bugs de Internacionalização (i18n):** Múltiplos textos vazando do backend em inglês ("Invalid credentials" no login, "PENDING" nos pedidos).

---

## 5. Reflexão

* **O plano de testes ajudou a organizar melhor o processo? Por quê?**
    Sim. Sem o plano, eu teria focado apenas na barra de pesquisa quebrada. Ter um roteiro estruturado me forçou a isolar o que não funcionava (a busca por texto no CT-03) e pivotar os testes para validar outras áreas de negócio fundamentais, como os filtros de categoria (CT-04) e a tela de pós-venda dos pedidos (CT-05).

* **Algum problema só foi identificado durante a execução? Explique.**
    Sim, os defeitos de usabilidade e internacionalização (i18n). Lendo os requisitos, eu assumi que os erros estariam nas regras de negócio, mas durante a execução percebi que o sistema expõe dados técnicos ("Item Id #26") para o usuário final e não traduz mensagens do sistema ("Invalid credentials"), o que afasta o cliente comum.

* **O que eu melhoraria no processo de testes?**
    Anotar os passos na mão toma muito tempo. Para as próximas iterações eu proporia criar scripts de testes automatizados E2E (End-to-End) com ferramentas como Cypress, garantindo que o módulo de busca (quando for consertado) não volte a quebrar em futuras atualizações.

**Conclusão desta etapa:**
A funcionalidade de Busca e o Histórico de Pedidos foram considerados **inaceitáveis**. O Core Business de um app de delivery é achar a comida e acompanhar a compra. Com a busca inoperante e os pedidos ilegíveis, o aplicativo não consegue reter o usuário.

---

## 6. Conclusão Geral

* **Qualidade geral do sistema testado:** O sistema apresenta um estado de maturidade de "rascunho" (MVP muito inicial).
* **Principais pontos positivos:** O controle de acesso e o filtro estático de categorias funcionam de maneira fluida.
* **Principais problemas identificados:** Módulo de busca textual inoperante, vazamento de dados estruturais na tela do cliente (IDs de banco de dados em vez de nomes) e falta de adequação do idioma para o mercado local.
* **Impressão geral sobre o processo de testes:** A atividade consolidou o entendimento de que testes reais revelam problemas que a teoria não prevê. O planejamento evitou que eu perdesse tempo tentando "fazer a busca funcionar" e garantiu que eu cobrisse outras partes críticas do sistema de forma profissional.