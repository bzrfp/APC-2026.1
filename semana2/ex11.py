iof = 0.035

valor_brl = float(input("Informe o valor em reais: "))
cotacao = float(input("Informe a cotação do dólar: "))

valor_usd = valor_brl/cotacao
    
print("O valor obtido em dolares é ", valor_usd - valor_usd*iof)
