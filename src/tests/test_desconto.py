import pytest
from src.desconto import aplicar_desconto

def test_deve_aplicar_desconto_valido():
    valor = 100
    percentual = 20
    resultado = aplicar_desconto(valor, percentual)
    assert resultado == 80.0

def test_deve_lancar_erro_para_percentual_invalido():
    valor = 100
    percentual = 110
    with pytest.raises(ValueError, match="Percentual de desconto inválido"):
        aplicar_desconto(valor, percentual)