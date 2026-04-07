p = 0.001
r = 2

x = int(input("Informe um número inteiro: ")) 

while (abs(r*r - x) > p):
    r = (r + x / r) / 2  

print (f'A raiz quadrada de {x} é aproximadamente {r}')