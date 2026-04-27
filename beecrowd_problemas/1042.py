#sort simples 
#solucao semana 7 
lista = list(map(int, input().split()))

original = lista[:]

lista.sort()

for v in lista:
    print(v)
    
print() 

for v in original:
    print(v)
