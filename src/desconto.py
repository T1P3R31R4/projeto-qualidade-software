def aplicar_desconto(valor_total, percentual):
    valor_com_desconto = valor_total * (1 - (percentual / 100))
    return round(valor_com_desconto, 2)

def aplicar_desconto(valor_total, percentual):
    if not (0 <= percentual <= 100):
        raise ValueError("Percentual de desconto inválido")
    valor_com_desconto = valor_total * (1 - (percentual / 100))
    return round(valor_com_desconto, 2)