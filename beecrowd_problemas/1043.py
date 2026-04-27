#triangulo ou trapezio 
#solucao semana 7
a, b, c = map(float, input().split())

if (a + b > c and a + c > b and b + c > a):
    
    doisp = a + b + c
    print(f"Perimetro = {doisp:.1f}")
    
else:
    
    areatrap = ((a+b)*c)/2
    print (f"Area = {areatrap:.1f}")
