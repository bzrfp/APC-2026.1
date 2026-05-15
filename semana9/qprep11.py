#Calcule o valor de uma jornada de trabalho diário 

turno, dia, horas = input().split()

horas = int(horas) 

if turno == "diurno":
    
    pagamento = horas*5.51
    
elif turno == "noturno":
    
    pagamento = horas*5.51*1.2
    
    
    
if dia == "domingo":
    
    pagamento = 2*pagamento
    
    
print(f"{pagamento:.2f}")
