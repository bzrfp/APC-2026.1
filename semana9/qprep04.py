#Paridade de uma mensagem 

mensagem = input()

n = len(mensagem)

soma = 0 

for i in range (n):
    
    soma = soma + int(mensagem[i])
    
if soma%2 == 0:
    print("Paridade par.")
else:
    print("Paridade impar.")
