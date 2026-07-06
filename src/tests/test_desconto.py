import pytest
from src.desconto import aplicar_desconto

def test_deve_aplicar_desconto_valido():
    valor = 100
    percentual = 20
    resultado = aplicar_desconto(valor, percentual)
    assert resultado == 80.0