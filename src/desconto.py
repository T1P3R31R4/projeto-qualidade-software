def aplicar_desconto(valor_total, percentual):
    valor_com_desconto = valor_total * (1 - (percentual / 100))
    return round(valor_com_desconto, 2)