# Aula 9 – Testes Unitários e TDD - LocalEats

## 👥 Integrante
- Tiago Jesus Pereira

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── pedido.py  
│   └── desconto.py
└── tests/  
    ├── test_pedido.py  
    └── test_desconto.py 

---

## 🔹 1. Funcionalidades escolhidas

Como realizei o trabalho individualmente, optei por focar em duas regras de negócio centrais do sistema.

---

### 📦 Funcionalidade 1 – Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/pedido.py`  
**Arquivo de testes:** `/tests/test_pedido.py`

#### Descrição
Soma os valores dos itens do pedido em uma lista de dicionários e valida se o total atinge o valor mínimo exigido pelo restaurante.

#### Regras de negócio
- A soma da chave `preco` dos itens define o total.  
- O pedido deve atingir o valor mínimo.  
- Caso contrário, deve gerar um `ValueError`.  

---

### 💸 Funcionalidade 2 – Aplicação de desconto percentual

**Arquivo da implementação:** `/src/desconto.py`  
**Arquivo de testes:** `/tests/test_desconto.py`

#### Descrição
Aplica um desconto percentual sobre o valor total do pedido.

#### Regras de negócio
- O percentual deve estar estritamente entre 0 e 100.  
- Valores fora desse intervalo geram um `ValueError`.  
- O valor final não pode ser negativo.  

---

## 🔹 2. Testes Unitários e Ciclo TDD

Implementei os testes unitários utilizando o framework `pytest`. A estrutura dos arquivos de teste foi separada de acordo com cada regra de negócio na pasta `/tests`.

---

### 🧪 Testes (Pedido)

#### Teste 1 – Valor acima do mínimo (Happy Path)

- Cenário: Pedido válido onde a soma dos itens ultrapassa o mínimo.  
- Resultado esperado: Retorna o total correto (30).  

##### TDD
- **Red:** O teste `test_deve_calcular_total_quando_valor_minimo_atingido` falhou no Pytest pois a função `calcular_total_pedido` não existia.  
- **Green:** Implementação básica de soma para fazer o teste passar.  
- **Refactor:** Uso de _list comprehension_ `sum()` para somar a chave "preco" de forma dinâmica e limpa.  

#### Teste 2 – Valor abaixo do mínimo (Cenário de Borda)

- Cenário: Pedido inválido onde a soma não atinge o valor mínimo estipulado.  
- Resultado esperado: Lançar exceção `ValueError`.  

##### TDD
- **Red:** O teste utilizando `pytest.raises` falhou pois a função retornou o valor da soma em vez de gerar erro.  
- **Green:** Condicional `if` adicionada, lançando o erro.  
- **Refactor:** Melhoria na string da mensagem de erro para deixar explícito qual foi a falha da regra de negócio, facilitando o debug.  

---

### 🧪 Testes (Desconto)

#### Teste 1 – Aplicação de desconto válido (Happy Path)

- Cenário: Desconto de 20% aplicado sobre um pedido de 100.  
- Resultado esperado: Retornar 80.0.  

##### TDD
- **Red:** Erro `ImportError` ao rodar o Pytest por falta do módulo/função.  
- **Green:** Cálculo simples de subtração no código fonte.  
- **Refactor:** Transformação do cálculo em percentual real com `valor_total * (1 - (percentual / 100))` e arredondamento correto.  

#### Teste 2 – Percentual inválido (Cenário de Erro)

- Cenário: Tentativa de aplicar 110% de desconto.  
- Resultado esperado: Lançar exceção `ValueError`.  

##### TDD
- **Red:** O cálculo aceitou o valor acima de 100 e retornou um preço final negativo. O teste falhou.  
- **Green:** Condicional adicionada impedindo especificamente valores maiores que 100.  
- **Refactor:** Otimização da condicional para uma verificação encadeada `if not (0 <= percentual <= 100):`, que já blinda o sistema contra números negativos também.  

---

## 🔹 3. Execução dos Testes

- **Total de testes:** 4  
- **Quantos passaram:** 4  
- **Quantos falharam:** 0  

*(Nota: Print da execução do `pytest -v` no terminal anexado no repositório)*

---

## 🔹 4. Reflexão no contexto do LocalEats

### Foi difícil escrever testes antes do código?
Sim, no começo rola aquele desconforto. A gente que já tem o costume de sair codando a lógica direto, ter que parar, pensar na falha e fazer o teste primeiro exige uma mudança de chave na cabeça. Mas depois que pega o ritmo, faz muito sentido e ajuda a visualizar a entrada e saída de dados com muito mais clareza.

### O TDD ajudou no desenvolvimento?
Com certeza. Me forçou a entender exatamente o que a regra de negócio do LocalEats precisava antes de meter a mão no código. Evitou que eu criasse lógicas super complexas logo de cara, me mantendo focado no mínimo necessário pra fazer o teste passar.

### Os testes aumentaram a confiança no código?
Demais! Como venho focando bastante em criar sistemas que envolvem cálculos e painéis de controle, ter essa malha de testes rodando me dá a garantia de que, se eu precisar refatorar algo no backend no futuro, não vou quebrar o que já estava funcionando bem.

### O que melhoraria?
Eu tentaria cobrir mais alguns cenários de borda (por exemplo, lidar com itens vindo sem a chave "preco" no dicionário), além de explorar recursos mais avançados do próprio Pytest, como o `@pytest.mark.parametrize`, para testar várias entradas de uma vez só na mesma função e deixar o arquivo de testes mais limpo.

### Como isso ajuda no projeto?
Pensando no LocalEats e na arquitetura de aplicações reais, validações financeiras como pedido mínimo e descontos são pontos críticos. O TDD automatizado garante que o usuário não vai ter problemas de cobrança e que a aplicação pode escalar, receber novas features e manutenção contínua sem o medo constante de causar problemas em produção (regressão).