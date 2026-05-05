a, b, c = map(float, input().split())
op = input()

if (op == "P"):
    
    print("Ponderada") 
    
    p1, p2, p3 = map(int, input().split())
    
    M = (a*p1 + b*p2 + c*p3)/(p1+p2+p3)
    
    print(f"{M:.2f}")
    
elif (op == "H"):

    print("Harmonica")
    
    M = 3/(1/a + 1/b + 1/c)
    
    print(f"{M:.2f}")
    
elif (op == "A"):

    print("Aritmetica")
    
    M = (a+b+c)/3
    
    print(f"{M:.2f}")
    
else:
    print("Operacao inexistente")    
