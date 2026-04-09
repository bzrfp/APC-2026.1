num = float(input())

if (num >= 0 and num <  1):
    
    d1 = int(num*2)
    d2 = int((num*2-d1)*2)
    d3 = int(((num*2-d1)*2-d2)*2)
    
    print(f"0.{d1}{d2}{d3}")

else:
    
    print("Valor invalido")
