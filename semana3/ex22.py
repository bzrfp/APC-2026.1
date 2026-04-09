a, b, c = map(float, input().split())
    
if (a < b+c and b < a+c and c < a+b):
        
    if (a == b and a == c):
        tipo = "Equilátero"
        
    elif (a == b or a == c or c == b):
        tipo = "Isósceles"
            
    else:
        tipo = "Escaleno"
            
        
    print(f"Tipo: {tipo}.")
    
else:
    print("Não forma triângulo.")
