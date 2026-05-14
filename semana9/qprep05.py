#calcular checksum 

mensagem = input()

n = len(mensagem)

soma = 0 

for i in range (n):
    soma = soma + ord(mensagem[i])
    
    
checksum = soma%256
    
print (f"Checksum: {checksum}")
