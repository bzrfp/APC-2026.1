faltas = int(input("Informe o percentual de faltas (0 - 100 (%)): "))
nota_final = float(input("Informe a nota final: "))

if (faltas > 25):
    mencao = "SR"
else:
    if (nota_final >= 9):
        mencao = "SS"
    elif (nota_final >= 7):
        mencao = "MS"
    elif (nota_final >=5):
        mencao = "MM"
    elif (nota_final >= 3):
        mencao = MI
    else:
        mencao = II 

print("A menção do aluno é:", mencao) 