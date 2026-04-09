idade = int(input("Informe a idade: "))
    
if (idade < 5):
    print ("Não há classificação para essa faixa etária")
else:
    if (idade < 8):
        classe = "Infantil A"
    elif (idade < 11):
        classe = "Infantil B"
    elif (idade < 14):
        classe = "Juvenil A"
    elif (idade < 18):
        classe = "Juvenil B"
    else:
        classe = "Adulta"
            
    print("O nadador pertence à classe ", classe)   
