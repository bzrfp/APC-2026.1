#fibonacci
def fib(n):
    lista[n] += 1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
n = int(input())
lista = [0] * (n+1)
print(f"Termo: {fib(n)}")
print("Quantidades:")

termo = 0
for i in lista:
    print(f"fibonacci({termo}) - {i}")
    termo += 1
