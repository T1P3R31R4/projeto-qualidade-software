# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos
# Entrega PBL – LocalEats

## 👥 Integrante

- Tiago Jesus Pereira

---

## 🔹 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-laboratorio |
| Link do repositório | [https://github.com/T1P3R31R4/localeats-ci-laboratorio.git](https://github.com/T1P3R31R4/localeats-ci-laboratorio.git) |

### Estrutura de Diretórios

```text
localeats-ci-laboratorio/
├── .github/
│   └── workflows/
│       └── quality.yml
├── tests/
│   └── test_order.py
└── order.py
```

---

## 🔹 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido no carrinho. |
| Link da Issue | [https://github.com/T1P3R31R4/localeats-ci-laboratorio/issues/1](https://github.com/T1P3R31R4/localeats-ci-laboratorio/issues/1) |

---

## 🔹 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar se a função de cálculo soma corretamente uma lista de valores. |
| Link para o arquivo do teste | [https://github.com/T1P3R31R4/localeats-ci-laboratorio/blob/main/tests/test_order.py](https://github.com/T1P3R31R4/localeats-ci-laboratorio/blob/main/tests/test_order.py) |

```python
from order import calculate_total

def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60
```

---

## 🔹 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o arquivo do workflow | [https://github.com/T1P3R31R4/localeats-ci-laboratorio/blob/main/.github/workflows/quality.yml](https://github.com/T1P3R31R4/localeats-ci-laboratorio/blob/main/.github/workflows/quality.yml) |
| Link de uma execução do workflow | [https://github.com/T1P3R31R4/localeats-ci-laboratorio/actions](https://github.com/T1P3R31R4/localeats-ci-laboratorio/actions) |

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest

      - run: pytest
```

---

## 🔹 5. Indicadores de Qualidade

Após executar o pipeline, os seguintes indicadores foram registrados:

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 🔹 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo do valor total |
| Severidade | Alta |
| Link da Issue | [https://github.com/T1P3R31R4/localeats-ci-laboratorio/issues/2](https://github.com/T1P3R31R4/localeats-ci-laboratorio/issues/2) |

**Descrição do Defeito:**
O defeito foi simulado alterando a função de cálculo para retornar um valor estático incorreto. O problema foi identificado imediatamente pelo pipeline de Integração Contínua (GitHub Actions), que acusou falha no `test_calculate_total`. O erro foi corrigido restaurando a função nativa `sum()` no código-fonte, o que fez o pipeline voltar ao status de sucesso na execução seguinte.