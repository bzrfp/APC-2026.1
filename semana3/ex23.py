renda = float(input().strip())
    
if (renda > 2000): 

    restricao = input().strip().lower() 
    if (restricao == "nao"):
        print("Parabéns, Vital! Crédito Aprovado.")
        
    elif(restricao == "sim"):
        print("Renda ok, mas crédito em análise humana devido à restrição.")
            
else:
    print("Renda insuficiente. Crédito Negado.")
