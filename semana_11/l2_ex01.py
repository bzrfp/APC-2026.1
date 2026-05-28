#Dada uma lista de inteiros a e dois inteiros i,j (i≤j), imprima duas novas listas, 
#a primeira é uma lista dos elementos de a que estão no intervalo [i,j] e a segunda é uma lista dos que não estão nesse intervalo

a = list(map(int,(input().split())))
i, j = map(int, input().split())

l_int = []
l_fora_int = []

for num in a:
    if num >= i and num <= j:
        l_int.append(num)
        
for num in a:
    if num not in l_int:
        l_fora_int.append(num)
        
print(l_int)
print(l_fora_int)
