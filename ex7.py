salario_bruto = float(input("Informe o salário bruto: "))
filhos = int(input("Informe a quantidade de dependentes: ")) 

descontos = salario_bruto*0.08 + salario_bruto*0.1

descontos = descontos + (salario_bruto - descontos)*0.005 

acrescimos = filhos*50

salario_liquido = salario_bruto - descontos + acrescimos

print ("O salário líquido é: ", salario_liquido)
print ("O total de descontos é: ", descontos)
print ("O total de acréscimos é: ", acrescimos)