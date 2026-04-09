num = int(input())


if (num >= 1 and num <= 15): 
    
    d1 = num % 2
    d2 = (num//2)%2
    d3 = (num//4)%2
    d4 = (num//8)%2
    
    if (f"{d4}{d3}{d2}{d1}" == "0000"):
        y = 0

    elif (f"{d4}{d3}{d2}{d1}" == "1111"):
        y = 4
        
    elif (f"{d4}{d3}{d2}{d1}" == "0111" or f"{d4}{d3}{d2}{d1}" == "1110" or f"{d4}{d3}{d2}{d1}" == "1011" or f"{d4}{d3}{d2}{d1}" == "1101"):
        y = 3
        
    elif (f"{d4}{d3}{d2}{d1}" == "0011" or f"{d4}{d3}{d2}{d1}" == "1100" or f"{d4}{d3}{d2}{d1}" == "0110" or f"{d4}{d3}{d2}{d1}" == "1001" ):
        y = 2
        
    elif (f"{d4}{d3}{d2}{d1}" == "0101" or f"{d4}{d3}{d2}{d1}" == "1010" ):
        y = 2
        
    else:
        y = 1

    print (f"Binario: {d4}{d3}{d2}{d1}")
    print (f"Quantidade de 1s: {y}")
    
else:
    print("Valor invalido")
