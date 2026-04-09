consumo = int(input("Informe o consumo (kWh)"))
    
if (consumo <= 100):
    valor_conta = consumo*0.5
elif (consumo <= 300):
    valor_conta = consumo*0.85
else:
    valor_conta = consumo*1.2
    
print("O total a pagar é ", valor_conta)
