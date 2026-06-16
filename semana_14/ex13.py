#Consultas de intervalo na string
n = int(input())
lista = []

for i in range(n):
    l, r, s = input().split()
    
    l = int(l)
    r = int(r)
    
    ns = s[l:r+1]
    lista.append(ns)
    
for e in lista:
    print(e)
