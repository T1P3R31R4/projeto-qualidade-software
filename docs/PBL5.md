# Aula 6 – Planejamento e Execução de Testes

**Disciplina:** Qualidade de Software
**Projeto:** LocalEats
**Aluno:** Tiago Jesus Pereira (Trabalho Individual)

---

## 1. Plano de Testes

**1.1 Objetivo**
Estruturar e executar uma validação prática das funções centrais do sistema LocalEats (Busca e Login). O objetivo é sair do teste exploratório aleatório (onde apenas "clicamos para ver se funciona") e aplicar uma abordagem metódica para identificar, reproduzir e documentar as falhas que estão impactando a experiência de clientes e restaurantes.

**1.2 Escopo**
* **O que será testado:** * Fluxo de autenticação de usuários (Login).
    * Mecanismo de busca de restaurantes por texto livre.
    * Filtros de categoria na pesquisa.
* **O que NÃO será testado:** * Integração com gateways de pagamento.
    * Disparo de e-mails reais de recuperação de senha.
    * Responsividade da interface em diferentes tamanhos de tela mobile (o foco atual é funcionalidade de negócio).

**1.3 Funcionalidades selecionadas**
* [Login/Cadastro]
* [Busca de restaurantes]

**1.4 Estratégia de Testes**
* **Tipos de teste:** (X) Funcional
* **Abordagem:** Testes manuais de Caixa-Preta. Utilizarei casos de teste pré-definidos baseados em cenários de sucesso (Happy Path) e cenários de exceção/erro (Sad Path), escritos utilizando a estrutura BDD/Gherkin (Dado, Quando, Então) para maior clareza dos passos.

**1.5 Responsáveis**
* **Tiago Jesus Pereira:** Responsável exclusivo pelo planejamento dos cenários, execução manual simulada na plataforma web, coleta de evidências e análise crítica dos resultados.

---

## 2. Casos de Teste

**CT-01 – Login com credenciais válidas (Cenário de Sucesso)**
* **Pré-condição:** O usuário deve possuir um cadastro ativo no banco de dados.
* **Passos:**
    1. Dado que estou na página inicial do LocalEats.
    2. E clico no botão de "Entrar/Login".
    3. Quando eu preencho o e-mail "cliente@teste.com" e a senha "Senha123".
    4. E clico no botão "Acessar".
* **Resultado esperado:** Então o sistema autentica o usuário, redireciona para a tela principal (Dashboard) e exibe o nome do usuário no canto superior da tela.

**CT-02 – Login com senha incorreta (Cenário de Erro)**
* **Pré-condição:** O usuário possui cadastro, mas não lembra a senha.
* **Passos:**
    1. Dado que estou na página de login.
    2. Quando eu preencho o e-mail válido "cliente@teste.com", mas insiro a senha errada "SenhaErrada999".
    3. E clico no botão "Acessar".
* **Resultado esperado:** Então o sistema não deve autenticar o usuário e deve exibir uma mensagem clara em vermelho indicando "E-mail ou senha incorretos", mantendo o usuário na mesma tela.

**CT-03 – Busca por termo exato com resultados (Cenário de Sucesso)**
* **Pré-condição:** O banco de dados deve conter restaurantes com o termo "Pizza" cadastrados.
* **Passos:**
    1. Dado que estou na página de busca do LocalEats.
    2. Quando eu digito "Pizza" na barra de pesquisa.
    3. E aperto a tecla Enter ou clico na lupa.
* **Resultado esperado:** Então o sistema carrega e exibe uma lista apenas com restaurantes que contenham "Pizza" no nome ou na categoria.

**CT-04 – Busca com filtros cruzados (Cenário de Sucesso)**
* **Pré-condição:** Existência de restaurantes de diversas categorias no sistema.
* **Passos:**
    1. Dado que estou na página de busca.
    2. Quando eu seleciono o filtro de categoria "Japonesa".
    3. E seleciono o filtro de faixa de preço "$$".
    4. E clico em "Aplicar Filtros".
* **Resultado esperado:** Então a lista de resultados é atualizada para exibir *apenas* restaurantes que sejam de comida japonesa E que tenham o preço médio estabelecido.

**CT-05 – Busca por termo com caracteres especiais (Cenário de Erro)**
* **Pré-condição:** O sistema está online.
* **Passos:**
    1. Dado que estou na página de busca.
    2. Quando eu digito caracteres especiais inválidos como "<script> %&*" na barra de pesquisa.
    3. E tento realizar a busca.
* **Resultado esperado:** Então o sistema sanitiza a busca ou exibe uma mensagem amigável de "Nenhum resultado encontrado para este termo", sem quebrar o layout da tela ou retornar um erro genérico de servidor (Erro 500).

---

## 3. Execução dos Testes

Abaixo estão os resultados registrados após a execução simulada no ambiente web:

* **CT-01 (Login válido):** * **Resultado:** Passou. 
    * **Evidência:** O redirecionamento ocorreu normalmente e o token de sessão foi gerado na aplicação.
* **CT-02 (Login inválido):** * **Resultado:** Passou. 
    * **Evidência:** Mensagem de alerta apareceu corretamente, impedindo o acesso.
* **CT-03 (Busca simples):** * **Resultado:** Passou. 
    * **Evidência:** A lista carregou as pizzarias da região em um tempo de resposta aceitável.
* **CT-04 (Filtros cruzados):** * **Resultado:** Falhou. 
    * **Evidência:** O sistema trouxe restaurantes de comida japonesa ($$), mas também misturou churrascarias caras na lista. A lógica do filtro parece estar usando a condição "OU" (OR) em vez de "E" (AND) no backend.
* **CT-05 (Caracteres especiais):** * **Resultado:** Falhou. 
    * **Evidência:** A tela ficou em "loop" de carregamento infinito e o console do navegador retornou um erro "500 Internal Server Error" vindo da API, indicando falta de tratamento de dados de entrada.

---

## 4. Análise dos Resultados

* **Quantidade de testes executados:** 5
* **Quantidade de testes que passaram:** 3
* **Quantidade de testes que falharam:** 2

**Principais problemas encontrados:**
1.  **Lógica de Filtros Quebrada:** A funcionalidade de pesquisa avançada não cruza os parâmetros corretamente (CT-04). Isso explica a reclamação constante dos usuários sobre "resultados incorretos nas buscas" mapeada nos diagnósticos anteriores da startup.
2.  **Falta de Tratamento de Exceções na API:** O sistema não sabe lidar com buscas atípicas ou inputs maliciosos (CT-05). Em vez de devolver uma resposta tratada para o front-end, o servidor trava, o que contribui diretamente para a lentidão e instabilidade relatada nos horários de pico.

---

## 5. Reflexão

* **O plano de testes ajudou a organizar melhor o processo? Por quê?**
    Sim, fundamentalmente. Sem o plano, eu provavelmente apenas digitaria "Pizza", veria que funcionou e daria a busca como "OK". O plano me forçou a pensar nos "Cenários Tristes" (Sad Paths) antes de abrir a tela, o que me guiou a encontrar as falhas críticas nos filtros e na segurança das requisições.

* **Algum problema só foi identificado durante a execução? Explique.**
    Sim. Durante a execução do CT-05, não apenas a busca falhou, como percebi que não há *feedback* visual (como um Toast ou Modal de aviso) informando ao usuário que ocorreu um erro de conexão. Para o usuário comum, o site simplesmente parece "congelado".

* **O que eu melhoraria no processo de testes?**
    Anotar os passos na mão toma muito tempo. Para as próximas iterações (especialmente para testar os filtros complexos de busca), eu proporia criar scripts de testes automatizados (usando bibliotecas de teste de front-end) para garantir que essas funções centrais não quebrem a cada nova atualização que a equipe subir para produção.

**Conclusão desta etapa:**
O comportamento do Login foi considerado aceitável, mas a funcionalidade de Busca foi considerada **inaceitável**. Como a busca é a "espinha dorsal" da conexão entre clientes e restaurantes, esses defeitos bloqueiam diretamente a geração de valor do produto.

---

## 6. Conclusão Geral

* **Qualidade geral do sistema testado:** O sistema apresenta um estado de maturidade incipiente (MVP). Ele executa os fluxos básicos, mas falha gravemente quando as variáveis fogem do caminho perfeito.
* **Principais pontos positivos:** O controle de acesso (autenticação) demonstrou estar funcionando conforme os requisitos, sem expor dados.
* **Principais problemas identificados:** A lógica de cruzamento de dados na base de dados/API está falha. O sistema confia excessivamente nas entradas do usuário e não trata as exceções, gerando travamentos que arruínam a usabilidade.
* **Impressão geral sobre o processo de testes:** Executar esta atividade consolidou o entendimento de que ser QA não é ter o papel de "quebrar o software", mas sim aplicar um método científico para expor os comportamentos reais do sistema sob estresse, garantindo que a equipe de desenvolvimento saiba exatamente onde agir para salvar a reputação do produto.