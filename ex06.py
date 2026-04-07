total_em_dias = int(input("Informe a idade em dias: "))

anos = int(total_em_dias /365) 
 
if (total_em_dias % 365 == 0):
    meses = 0
    dias = total_em_dias - anos*365
else:
    meses = int((total_em_dias % 365)/30)
    dias =  total_em_dias - meses*30 - anos*365 

print(f"A idade é {anos} anos, {meses} meses e {dias} dias.")
