import pytest
from src.pedido import calcular_total_pedido

def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 30

def test_deve_lancar_erro_quando_valor_abaixo_do_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 20
    
    with pytest.raises(ValueError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)