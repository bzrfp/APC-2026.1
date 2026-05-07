#positivo ou negativo 
t = int(input())

for i in range(t):
    valor = int(input())
    if valor > 0:
        print("+")
    elif valor < 0:
        print("-")
    else:
        print("?") 
