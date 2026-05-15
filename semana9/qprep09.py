n, c = map(int, input().split()) 

soma = 0 

for i in range (n):

    x = int(input())
    
    soma = soma + x
    
    
print(f"Dados uteis: {soma} bytes")
print(f"Total transmitido: {soma + n*c} bytes")
print(f"Eficiencia: {((soma/(soma+n*c))*100):.2f}%")
