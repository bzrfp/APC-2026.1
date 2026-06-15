#Calcula polinômio
exp, x = map(int, input().split())

coefs = list(map(int, input().split()))
coefs.reverse()

l = []

for i in range(exp+1):
    num = coefs[i] * x**i
    l.append(num)
    
print(sum(l))
