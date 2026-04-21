# Estratégia Inicial de Testes – LocalEats

**Disciplina:** Qualidade de Software
**Integrantes:** Tiago Jesus Pereira

---

## 1. Funcionalidades principais

1. Busca e filtro de restaurantes (por culinária, local, preço)
2. Visualização de cardápios e informações do local
3. Sistema de avaliações (escrever review e postar fotos)
4. Favoritar restaurantes

---

## 2. Níveis de Teste

**Funcionalidade 1: Busca e filtro de restaurantes**
* **Unitário:** Validar a lógica dos filtros (ex: se o usuário filtra preço "$$", o código barra os de "$$$").
* **Integração:** Verificar se a API de busca consegue consultar o banco de dados corretamente e retornar o JSON com os restaurantes.
* **Sistema:** O fluxo de abrir a tela, digitar "Pizza", clicar em buscar e ver a lista renderizada.
* **Aceitação:** O usuário (turista) consegue achar rapidamente um restaurante que atenda ao seu gosto e bolso.

**Funcionalidade 2: Visualização de cardápios**
* **Unitário:** Garantir que a formatação de preços e horários de funcionamento não quebrem por erros de código.
* **Integração:** Checar o endpoint que busca as fotos e itens do cardápio do banco de dados.
* **Sistema:** Clicar em um restaurante da lista e verificar se a tela do cardápio carrega todas as informações visuais sem quebrar o layout.
* **Aceitação:** O cliente consegue entender claramente o que o restaurante serve antes de decidir ir até lá.

**Funcionalidade 3: Sistema de avaliações**
* **Unitário:** Validar regras básicas (não aceitar nota menor que 1 ou maior que 5, limite de caracteres no texto).
* **Integração:** Verificar se o "POST" da avaliação realmente grava os dados na tabela certa do banco.
* **Sistema:** Escrever uma avaliação, enviar, **dar um refresh na página (F5)** e confirmar se o texto continua lá (atacando o bug relatado).
* **Aceitação:** O usuário consegue compartilhar sua experiência de forma fácil.

**Funcionalidade 4: Favoritar restaurantes**
* **Unitário:** Testar a função que adiciona ou remove um item do array/estado de favoritos.
* **Integração:** Validar se o ID do restaurante é vinculado corretamente ao ID do usuário autenticado no banco.
* **Sistema:** Clicar no ícone de "coração", ir até a tela de perfil e ver o restaurante salvo lá.
* **Aceitação:** O usuário consegue montar sua lista pessoal de locais para visitar no evento gastronômico.

---

## 3. Prioridades e Riscos

**Alta prioridade: Busca e Cardápios**
* **Justificativa:** É o coração do negócio. Se a busca retorna resultados errados (que é um dos bugs atuais) ou o cardápio não abre, o aplicativo perde totalmente a utilidade. O impacto de erros aqui é a perda imediata do usuário, que vai fechar o app e procurar no Google Maps.

**Média prioridade: Sistema de Avaliações**
* **Justificativa:** É importante para o engajamento e para a comunidade, mas não impede a pessoa de achar um lugar para comer. O risco atual (perder dados no refresh) gera muita frustração, mas o impacto comercial direto é menor do que a quebra da busca.

**Baixa prioridade: Favoritar restaurantes**
* **Justificativa:** É apenas uma feature de conveniência. Se falhar, o usuário ainda pode usar as outras funções principais do app. O esforço de testes pesados aqui agora não compensa enquanto a busca estiver ruim.

---

## 4. Pirâmide de Testes

* **Maior foco (Base - Testes Unitários):** Devemos ter muitos testes aqui para blindar as regras de negócio. Como a startup desenvolveu o app muito rápido, deve ter muito código frágil. São testes baratos, rodam rápido e os próprios desenvolvedores fazem.
* **Médio foco (Meio - Testes de Integração):** Como existem *inconsistências entre a versão Web e Mobile*, testar a integração das APIs é fundamental. Garantindo que a API responde os dados certos, o Front-end (seja mobile ou web) só precisa se preocupar em exibir a informação.
* **Menor foco (Topo - Testes de Sistema/E2E):** Devemos automatizar apenas os fluxos mais críticos pelo lado da interface (ex: pesquisar um restaurante e abrir). Ter muitos testes de UI custa caro, demora muito para rodar e eles quebram toda hora que alguém muda a cor de um botão.

---

## 5. Testes em Produção

* **O sistema deveria usar testes em produção?** Sim, estrategicamente.
* **Em quais situações e Justificativa:**
  1. **Monitoramento e APM:** Como o sistema fica "lento em horários de pico", precisamos de ferramentas rodando em produção para monitorar o tempo de resposta do banco de dados e dos servidores enquanto o pico acontece de verdade.
  2. **Canary Release (Liberação Gradual):** Como "algumas telas são confusas", quando o time desenhar telas novas para corrigir a usabilidade, podemos liberar essa atualização em produção primeiro para apenas 10% dos usuários. Se eles conseguirem usar sem gerar erros, liberamos para o resto. Isso diminui o risco de quebrar o app pra todo mundo de uma vez durante o evento gastronômico.