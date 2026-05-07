anterior = 0
nome_anterior = " " 

while True:
    nome, sal = (input().split(","))
    
    if nome != " " and nome != "Fim":
        nome_anterior = nome
    
    sal = float(sal)
    
    if (sal > anterior and nome != "Fim"):
        anterior = sal
    
    if nome == "Fim":
        break

if nome_anterior == " ":
    print ("Não tem")
else:
    print (f"{anterior:.2f}")
