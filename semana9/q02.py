#Dado um número N inteiro e positivo, faça um programa que imprima todos os números de 0 a N
#incluindo o 0 e o N que são divisíveis por 3 e 7.

n = int(input())
lista = ""

if n != 0:
    
    for i in range (n+1):
    
        if i%3 == 0 and i%7 == 0:
    
            lista = f"{lista}{i} "
            
else:
    
    lista = "0"
            
print (lista)
