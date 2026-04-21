# 🧪 Aula 5 – Testes Funcionais vs Estruturais

**Projeto:** LocalEats
**Disciplina:** Qualidade de Software

👥 **Integrantes do Grupo**
* Tiago Jesus Pereira

---

🎯 **1. Funcionalidade escolhida**

* **Funcionalidade selecionada:** Busca e Filtro de Restaurantes.
* **Descrição da funcionalidade:** Permite ao usuário pesquisar estabelecimentos por texto livre (ex: "Pizza", "Burguer"), combinando com filtros de tipo de culinária, localização (bairro ou raio de distância) e faixa de preço ($ a $$$$).
* **O que o usuário espera:** Que ao pesquisar por "Sushi barato perto de mim", o sistema retorne rapidamente apenas restaurantes japoneses, com preço baixo, abertos no momento e na sua região, sem misturar com pizzarias caras do outro lado da cidade.

---

🔍 **2. Testes Caixa-Preta (Visão do Usuário)**

**Quais testes vocês fariam sem conhecer o código?**
Aqui assumimos a postura do cliente (turista ou morador) usando o app. O foco é cruzar dados de entrada no formulário de busca e validar a resposta da tela, sem saber como o banco de dados funciona.

🔹 **Cenários de teste**
* **Cenário 1 (Caminho Feliz):** Pesquisar uma categoria existente (ex: "Italiana"), filtro de preço "$$" e validar se a lista exibe apenas restaurantes italianos de preço médio.
* **Cenário 2 (Filtros Conflitantes):** Selecionar categoria "Vegano" e digitar "Churrascaria" na barra de texto. O sistema deve informar elegantemente que não encontrou resultados, em vez de travar ou retornar uma lista aleatória.
* **Cenário 3 (Comportamento Extremo):** Enviar a busca com caracteres especiais (`%`, `'`, `&`) ou emojis na barra de texto.
* **Cenário 4 (Usabilidade/Pico):** Tentar aplicar múltiplos filtros ao mesmo tempo e limpar os filtros logo em seguida, verificando se a tela atualiza corretamente (sem precisar dar o famoso "refresh" que está apagando dados no sistema atual).

🔹 **Possíveis erros identificados**
* O sistema ignorar o filtro de preço e trazer os restaurantes que pagam anúncio primeiro (erro de regra de negócio).
* O aplicativo fechar sozinho (crash) ao receber emojis na busca.
* Lentidão extrema na tela do usuário enquanto a busca processa.

---

🔧 **3. Testes Caixa-Branca (Visão do Sistema)**

**Como essa funcionalidade poderia estar implementada internamente?**
Pela ótica de Desenvolvedor/Analista de Código. Sabemos que a pressa para o evento gastronômico fez a equipe codar rápido, então provavelmente as "gambiarras" estão na lógica de cruzamento de dados.

🔹 **Lógica hipotética (pseudo-código ou descrição)**
Imaginamos que a API no backend receba os parâmetros da tela e monte uma consulta (Query) dinâmica no banco de dados.
```javascript
// Pseudo-código hipotético da startup:
let query = "SELECT * FROM restaurantes WHERE status = 'ativo'";

if (filtroCategoria != null) {
    query += " AND categoria = " + filtroCategoria;
}
if (filtroPreco != null) {
    query += " OR preco = " + filtroPreco; // ALERTA: Esse 'OR' em vez de 'AND' explicaria as buscas incorretas do case!
}
```

🔹 **Situações a serem testadas**
* **Situação 1 (Cobertura de Desvios/Condicionais):** Testar se os blocos `IF` dos filtros opcionais são executados corretamente quando vazios. O sistema trata variáveis `null` ou `undefined` sem quebrar a consulta?
* **Situação 2 (Performance do Algoritmo):** Analisar se a consulta ao banco de dados está fazendo *Full Table Scan* (lendo todos os restaurantes da cidade de uma vez) em vez de usar paginação (ex: trazer de 10 em 10). Isso explica a lentidão em horários de pico.
* **Situação 3 (Segurança e Sanitização):** Inspecionar se o código limpa os inputs do usuário antes de ir para o banco (para evitar ataques de SQL Injection na barra de pesquisa).

🔹 **Possíveis erros identificados**
* Uso de operadores lógicos errados (`OR` no lugar de `AND`), causando o bug relatado de "resultados incorretos nas buscas".
* Consultas não otimizadas no banco de dados (queries pesadas), que estrangulam o servidor nos horários de pico.

---

⚖️ **4. Comparação entre as abordagens**

* **Qual a principal diferença entre testar sem ver o código e com acesso ao código?**
A diferença é a perspectiva. A Caixa-Preta foca na **Validação** (O sistema faz o que o negócio e o usuário precisam?). A Caixa-Branca foca na **Verificação** (O código foi construído de forma eficiente, segura e lógica?).

* **Que tipo de problema cada abordagem ajuda a encontrar?**
    * **Caixa-preta:** Encontra falhas de usabilidade, requisitos não atendidos, fluxos de tela quebrados e respostas bizarras do sistema a partir de ações do usuário (ex: botão de buscar não clica).
    * **Caixa-branca:** Encontra gargalos de performance, vulnerabilidades de segurança, trechos de código que nunca são executados (código morto) e falhas lógicas em cálculos matemáticos ou condicionais.

---

💡 **5. Reflexão no contexto do LocalEats**

* **Qual abordagem parece mais importante neste momento do projeto?**
Para "estancar o sangramento" e salvar a reputação da startup a curto prazo, a **Caixa-Preta** é mais urgente. Os comerciantes e clientes estão reclamando do que *veem e sentem* (telas confusas, buscas que não funcionam). Precisamos mapear as falhas visíveis para priorizar correções.

* **Apenas uma abordagem seria suficiente? Por quê?**
Não. Embora a Caixa-Preta mapeie a dor do usuário, ela não resolve o problema de "lentidão em horários de pico" de forma eficiente. Testar exaustivamente a interface não vai revelar que o banco de dados está mal modelado. Para garantir que o LocalEats aguente o grande evento gastronômico sem cair, a **Caixa-Branca** será essencial para refatorar e otimizar o código feito às pressas.

---

🚀 **Conclusão**

Compreendi que testar não é apenas clicar em botões para ver se a tela muda. A atividade deixou claro que os bugs relatados pelos usuários da LocalEats (como as buscas inconsistentes) geralmente são sintomas Caixa-Preta gerados por uma doença Caixa-Branca (um "IF" mal colocado ou banco lento). Para garantir um produto de qualidade, as duas técnicas precisam trabalhar juntas: uma garante que construímos o produto certo, e a outra garante que construímos o produto do jeito certo.