#Crie um programa que lê 10 números inteiros maiores que 0 e os armazena em uma lista
#Em seguida, substitua todos os números pares pelo número 1
#Por fim, imprima a lista com os números ímpares restantes.

l = []

for i in range (10):
    l.append(int(input()))
    
for i in range (len(l)):
    if l[i]%2 == 0:
        l[i] = 1
        
print(l)
